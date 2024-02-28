from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.contact import router as contact_router
from app.api.wordle import router as wordle_router


app = FastAPI()
origins = [
    "http://localhost:5174",
    "https://ryankupka.dev",
    "https://www.ryankupka.dev",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contact_router, prefix="/api")
app.include_router(wordle_router, prefix="/api")
    

@app.get("/api")
def read_root():
    return {"Hello": "World"}
