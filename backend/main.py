from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from asyncpg import create_pool
from app.config.settings import psql_details
from app.api.contact import router as contact_router
from app.api.wordle import router as wordle_router
from app.api.chat import router as chat_router

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

async def create_db_pool():
    try:
        pool = await create_pool(dsn=psql_details)
        return pool
    except Exception as e:
        print(f"Failed to create pool: {e}")

@app.on_event("startup")
async def startup():
    app.state.db_pool = await create_db_pool()

@app.on_event("shutdown")
async def shutdown_event():
    await app.state.db_pool.close()

app.include_router(contact_router, prefix=API_PREFIX)
app.include_router(wordle_router, prefix=API_PREFIX)
app.include_router(chat_router, prefix=API_PREFIX)

@app.get("/api")
def read_root():
    return {"Hello": "World"}
