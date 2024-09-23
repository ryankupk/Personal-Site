from fastapi import APIRouter, HTTPException, Depends, Header
from asyncpg import Connection
from app.config.database import get_books_db
from pydantic import BaseModel
from typing import List, Optional
import jwt
from app.api.auth import SECRET_KEY, ALGORITHM

router = APIRouter()

class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    genre: Optional[str] = None
    pages: Optional[int] = None
    rating: Optional[float] = None

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