from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    profession: str
    interests: str
    event_name: str


class ConversationResponse(BaseModel):
    introduction: str
    conversation_starters: list[str]