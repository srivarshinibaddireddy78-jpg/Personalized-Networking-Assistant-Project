from app.services.history_logger import HistoryLogger
import google.generativeai as genai
from app.config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


class ConversationGenerator:

    def generate_conversation(self, profile):

        prompt = f"""
You are an AI Networking Assistant.

User Details:
Name: {profile['name']}
Profession: {profile['profession']}
Interests: {profile['interests']}
Event: {profile['event']}

Generate:

1. A professional self introduction.

2. Three networking conversation starters.

3. One ice breaker.

4. One professional closing message.

Return the response in a neat format.
"""
        response = model.generate_content(prompt)

        HistoryLogger().save_history(profile, response.text)

        return response.text

 