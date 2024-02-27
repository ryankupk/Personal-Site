
from dotenv import load_dotenv
import os
import urllib.parse


load_dotenv()

MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_SOCKET = os.getenv("MONGO_SOCKET")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

motor_details = f"mongodb://{MONGO_USERNAME}:{urllib.parse.quote(MONGO_PASSWORD)}@{MONGO_SOCKET}/contact?authSource=admin"