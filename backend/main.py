from typing import Union

from dotenv import load_dotenv

import requests
import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import urllib.parse
from motor.motor_asyncio import AsyncIOMotorClient 
import os

load_dotenv()
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_SOCKET = os.getenv("MONGO_SOCKET")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

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

motor_details = f"mongodb://{MONGO_USERNAME}:{urllib.parse.quote(MONGO_PASSWORD)}@{MONGO_SOCKET}/contact?authSource=admin"
client = AsyncIOMotorClient(motor_details)
db = client.contact
contact_collection = db.contact_messages


class Message(BaseModel):
    message: str
    sender_name: str
    contact_info: str
    

@app.get("/api")
def read_root():
    return {"Hello": "World"}

@app.post("/api/contact")
async def send_message(message: Message):
    # Insert the message into the collection asynchronously
    result = await contact_collection.insert_one(message.model_dump(exclude={"id"}))

    # Send the message to Discord
    discord_message = {"content": message.model_dump_json()}
    discord_headers = {"Content-Type": "application/json"}
    discord_response = requests.post(DISCORD_WEBHOOK_URL, data=json.dumps(discord_message), headers=discord_headers)

    # Return the inserted message with its new ID
    return {"_id": str(result.inserted_id), **message.model_dump()}