from fastapi import APIRouter
from app.models.schemas import UserProfile
from app.services.conversation_generator import ConversationGenerator
from app.services.history_logger import HistoryLogger
router = APIRouter()

generator = ConversationGenerator()

@router.post("/generate-conversation")
def generate_conversation(profile: UserProfile):
    return {
        "conversation": generator.generate_conversation({
            "name": profile.name,
            "profession": profile.profession,
            "interests": profile.interests,
            "event": profile.event_name
        })
    }
@router.get("/history")
def get_history():
    logger = HistoryLogger()
    return logger.load_history()