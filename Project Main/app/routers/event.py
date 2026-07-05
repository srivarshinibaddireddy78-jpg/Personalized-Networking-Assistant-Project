from fastapi import APIRouter
from app.models.schemas import UserProfile
from app.services.event_analyzer import ProfileAnalyzer

router = APIRouter()

analyzer = ProfileAnalyzer()

@router.post("/analyze-event")
def analyze_event(profile: UserProfile):
    return analyzer.analyze_profile(
        profile.name,
        profile.profession,
        profile.interests,
        profile.event_name
    )