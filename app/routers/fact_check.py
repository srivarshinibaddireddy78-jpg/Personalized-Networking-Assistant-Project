from fastapi import APIRouter
from pydantic import BaseModel
from app.services.fact_checker import FactChecker

router = APIRouter()

checker = FactChecker()

class FactRequest(BaseModel):
    query: str

@router.post("/fact-check")
def fact_check(request: FactRequest):

    result = checker.verify(request.query)

    return {
        "summary": result
    }