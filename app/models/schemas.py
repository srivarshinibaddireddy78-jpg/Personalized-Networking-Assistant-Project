from pydantic import BaseModel
from typing import List

class UserProfile(BaseModel):
    name: str
    profession: str
    interests: List[str]
    event_name: str

class ConversationResponse(BaseModel):
    introduction: str
    conversation_starters: List[str]
    closing_message: str
    fact_check: str