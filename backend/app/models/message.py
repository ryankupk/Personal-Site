
from pydantic import BaseModel


class Message(BaseModel):
    message: str
    sender_name: str
    contact_info: str
