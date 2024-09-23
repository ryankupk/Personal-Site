from fastapi import APIRouter, HTTPException, Depends
from asyncpg import Connection
from app.config.database import get_books_db
from pydantic import BaseModel
import jwt
from datetime import datetime, timedelta

router = APIRouter()

SECRET_KEY = "your_secret_key"  # In a real app, store this securely
ALGORITHM = "HS256"

class User(BaseModel):
    username: str
    password: str

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

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