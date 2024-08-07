
from dotenv import load_dotenv
import os
import urllib.parse


load_dotenv()

MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_SOCKET = os.getenv("MONGO_SOCKET")

motor_details = f"mongodb://{MONGO_USERNAME}:{urllib.parse.quote(MONGO_PASSWORD)}@{MONGO_SOCKET}/contact?authSource=admin"

PSQL_USERNAME = os.getenv("PSQL_USERNAME")
PSQL_PASSWORD = os.getenv("PSQL_PASSWORD")
PSQL_SOCKET = os.getenv("PSQL_SOCKET")
PSQL_DATABASE = "wordle_words"
psql_details = f"postgresql://{PSQL_USERNAME}:{PSQL_PASSWORD}@{PSQL_SOCKET}/{PSQL_DATABASE}"

DISCORD_CONTACT_WEBHOOK_URL = os.getenv("DISCORD_CONTACT_WEBHOOK_URL")
DISCORD_CHAT_WEBHOOK_URL = os.getenv("DISCORD_CHAT_WEBHOOK_URL")
DISCORD_HEADERS = {"Content-Type": "application/json"}