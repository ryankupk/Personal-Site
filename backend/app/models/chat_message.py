from pydantic import BaseModel, Field
from typing import List, Optional

class MessageFile(BaseModel):
    # Define fields for MessageFile if needed
    pass

class MessageContent(BaseModel):
    role: Optional[str] = Field(default="ai")
    text: Optional[str] = Field(default=None)
    files: Optional[List[MessageFile]] = Field(default_factory=list)
    html: Optional[str] = Field(default=None)

class ChatRequest(BaseModel):
    messages: List[MessageContent]