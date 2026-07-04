import google.generativeai as genai
from app.config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


class FactChecker:

    def verify(self, text):

        prompt = f"""
You are an AI fact-checking assistant.

Review the following networking advice.

Tasks:
1. State whether it is Verified or Needs Correction.
2. Explain why.
3. If needed, provide a corrected version.
4. Give one additional networking tip.

Networking Advice:
{text}
"""

        response = model.generate_content(prompt)

        return response.text