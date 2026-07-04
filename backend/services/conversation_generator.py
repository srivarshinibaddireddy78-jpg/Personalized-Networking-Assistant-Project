import google.generativeai as genai
from backend.config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


class ConversationGenerator:

    def generate_conversation(self, profile):

        prompt = f"""
        You are a networking assistant.

        Name: {profile['name']}
        Interests: {profile['interests']}
        Event: {profile['event']}

        Generate:
        1. A professional introduction.
        2. Three networking conversation starters.
        3. One closing message.
        """

        response = model.generate_content(prompt)

        return response.text
