
from fastapi import APIRouter
from ..models.contact_message import ContactMessage
from ..config.settings import motor_details, DISCORD_CONTACT_WEBHOOK_URL, DISCORD_HEADERS
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
    # message_dump = message.model_dump_json()
    discord_message = {"content": f"From: {message.sender_name}\nContact information: {message.contact_info}\nMessage: ```{message.message}```"}
    discord_response = requests.post(DISCORD_CONTACT_WEBHOOK_URL, data=json.dumps(discord_message), headers=DISCORD_HEADERS)

    # Return the inserted message with its new ID
    return {"_id": str(result.inserted_id), **message.model_dump()}
