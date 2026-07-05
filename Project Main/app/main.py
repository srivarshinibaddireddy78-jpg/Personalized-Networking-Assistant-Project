from fastapi import FastAPI
from app.routers import event, fact_check, conversation

app = FastAPI(title="Personalized Networking Assistant")

app.include_router(event.router)
app.include_router(fact_check.router)
app.include_router(conversation.router)

@app.get("/")
def root():
    return {"message": "Personalized Networking Assistant API is running"}