
from pydantic import BaseModel


class ContactMessage(BaseModel):
    """ 
    {
        "message": "Hello, World!",
        "sender_name": "John Doe",
        "contact_info": "john.doe@example.com"
    }
    """
    message: str
    sender_name: str
    contact_info: str
