from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from asyncpg import create_pool
from app.config.settings import wordle_db_url, books_db_url
from app.api.contact import router as contact_router
from app.api.wordle import router as wordle_router
from app.api.chat import router as chat_router
from app.api.books import router as books_router  # New import

API_PREFIX = '/api'

app = FastAPI()

origins = [
    "http://localhost:5174",
    "https://ryankupka.dev",
    "https://www.ryankupka.dev",
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=["*"],
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def create_db_pools():
    try:
        wordle_pool = await create_pool(dsn=wordle_db_url)
        books_pool = await create_pool(dsn=books_db_url)
        return wordle_pool, books_pool
    except Exception as e:
        print(f"Failed to create pools: {e}")

@app.on_event("startup")
async def startup():
    app.state.wordle_pool, app.state.books_pool = await create_db_pools()

@app.on_event("shutdown")
async def shutdown_event():
    await app.state.wordle_pool.close()
    await app.state.books_pool.close()

app.include_router(contact_router, prefix=API_PREFIX)
app.include_router(wordle_router, prefix=API_PREFIX)
app.include_router(chat_router, prefix=API_PREFIX)
app.include_router(books_router, prefix=API_PREFIX)  # New router

@app.get("/api")
def read_root():
    return {"Hello": "World"}
