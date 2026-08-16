import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Read API Key
api_key = os.getenv("GOOGLE_API_KEY")

# Create Gemini Client
client = genai.Client(api_key=api_key)


def ask_gemini(prompt):
    """
    Sends a prompt to Gemini and returns the response.
    """

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text