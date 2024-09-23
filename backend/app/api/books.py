from fastapi import APIRouter, HTTPException, Depends, Header
from asyncpg import Connection
from app.config.database import get_books_db
from pydantic import BaseModel
from typing import List, Optional
import jwt
from datetime import datetime, timedelta

router = APIRouter()

SECRET_KEY = "your_secret_key"  # In a real app, store this securely
ALGORITHM = "HS256"

class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    genre: Optional[str] = None
    pages: Optional[int] = None
    rating: Optional[float] = None  # Changed from int to float

class User(BaseModel):
    username: str
    password: str

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        return username
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    except IndexError:
        raise HTTPException(status_code=401, detail="Invalid token format")

@router.post("/register")
async def register(user: User, db: Connection = Depends(get_books_db)):
    query = "INSERT INTO users (username, password) VALUES ($1, $2) RETURNING id"
    try:
        user_id = await db.fetchval(query, user.username, user.password)
        return {"message": "User registered successfully", "user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Username already exists")

@router.post("/login")
async def login(user: User, db: Connection = Depends(get_books_db)):
    query = "SELECT id FROM users WHERE username = $1 AND password = $2"
    user_id = await db.fetchval(query, user.username, user.password)
    if not user_id:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/books", response_model=List[Book])
async def get_books(db: Connection = Depends(get_books_db), current_user: str = Depends(get_current_user)):
    query = "SELECT * FROM books WHERE user_id = (SELECT id FROM users WHERE username = $1) ORDER BY id"
    books = await db.fetch(query, current_user)
    return [Book(**book) for book in books]

@router.post("/books", response_model=Book)
async def create_book(book: Book, db: Connection = Depends(get_books_db), current_user: str = Depends(get_current_user)):
    query = """
    INSERT INTO books (title, author, genre, pages, rating, user_id)
    VALUES ($1, $2, $3, $4, $5, (SELECT id FROM users WHERE username = $6))
    RETURNING *
    """
    values = (book.title, book.author, book.genre, book.pages, book.rating, current_user)
    result = await db.fetchrow(query, *values)
    return Book(**result)

@router.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book: Book, db: Connection = Depends(get_books_db), current_user: str = Depends(get_current_user)):
    query = """
    UPDATE books
    SET title = $1, author = $2, genre = $3, pages = $4, rating = $5
    WHERE id = $6 AND user_id = (SELECT id FROM users WHERE username = $7)
    RETURNING *
    """
    values = (book.title, book.author, book.genre, book.pages, book.rating, book_id, current_user)
    result = await db.fetchrow(query, *values)
    if result is None:
        raise HTTPException(status_code=404, detail="Book not found or you don't have permission to update it")
    return Book(**result)

@router.delete("/books/{book_id}", status_code=204)
async def delete_book(book_id: int, db: Connection = Depends(get_books_db), current_user: str = Depends(get_current_user)):
    query = "DELETE FROM books WHERE id = $1 AND user_id = (SELECT id FROM users WHERE username = $2)"
    result = await db.execute(query, book_id, current_user)
    if result == "DELETE 0":
        raise HTTPException(status_code=404, detail="Book not found or you don't have permission to delete it")