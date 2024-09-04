from fastapi import APIRouter, HTTPException
from ..models.chat_message import ChatRequest
from ..config.settings import motor_details, DISCORD_CHAT_WEBHOOK_URL, DISCORD_HEADERS
from motor.motor_asyncio import AsyncIOMotorClient
import ollama
import requests
import json

router = APIRouter()

client = AsyncIOMotorClient(motor_details)
db = client.chat
chat_collection = db.chat_messages


@router.post("/chat")
async def send_message(request: ChatRequest):
    try:
        # Insert the message into the collection asynchronously
        message_dict = request.messages[0].dict(exclude_unset=True)
        message_dict['text'] = f"Only respond to the question between the backticks if the question is about Ryan. Respectfully decline to answer if the question is unrelated. Answer briefly. Do not make up or give inaccurate information.\n`{message_dict['text']}`"
        discord_user_message = {"content": f"User asked: {message_dict['text']}"}
        discord_response = requests.post(DISCORD_CHAT_WEBHOOK_URL, data=json.dumps(discord_user_message), headers=DISCORD_HEADERS)
        message_insert_result = await chat_collection.insert_one(message_dict)

        generation = ollama.generate(model='ryan', prompt=message_dict['text'])
        message_response: str = generation['response']
        response_dict = {
            'role': 'ai',
            'text': message_response
        }
        response_insert_result = await chat_collection.insert_one(response_dict)
        # if not response_insert_result.acknowledged:
        #     raise HTTPException(status_code=500, detail="Response insertion failed")
        discord_agent_message = {"content": f"Agent replied: {message_response}"}
        discord_response = requests.post(DISCORD_CHAT_WEBHOOK_URL, data=json.dumps(discord_agent_message), headers=DISCORD_HEADERS)
        
        return {
            "text": message_response
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
