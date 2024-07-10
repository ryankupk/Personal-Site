
from fastapi import APIRouter
from ..models.contact_message import ContactMessage
from ..config.settings import motor_details, DISCORD_WEBHOOK_URL
from motor.motor_asyncio import AsyncIOMotorClient
import requests
import json 

router = APIRouter()

client = AsyncIOMotorClient(motor_details)
db = client.contact
contact_collection = db.contact_messages


@router.post("/contact")
async def send_message(message: ContactMessage):
    # Insert the message into the collection asynchronously
    result = await contact_collection.insert_one(message.model_dump(exclude={"id"}))

    # Send the message to Discord
    discord_message = {"content": message.model_dump_json()}
    discord_headers = {"Content-Type": "application/json"}
    discord_response = requests.post(DISCORD_WEBHOOK_URL, data=json.dumps(discord_message), headers=discord_headers)

    # Return the inserted message with its new ID
    return {"_id": str(result.inserted_id), **message.model_dump()}