import os
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

# Debug print
api_key = os.getenv("GEMINI_API_KEY")
print("GEMINI_API_KEY loaded:", "YES" if api_key else "NO")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment")

# Create client
client = genai.Client(api_key=api_key)

print("\nAvailable models:\n")
for m in client.models.list():
    print(m.name)
