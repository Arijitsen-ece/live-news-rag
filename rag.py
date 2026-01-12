import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)
MODEL_NAME = "models/gemini-flash-latest"

def answer(question, news):
    context = ""
    for n in news:
        context += f"- {n['title']}: {n['description']}\n"

    prompt = f"""
You are a news assistant.
Answer ONLY using the news below.
If not found, say "Not found in current news".

News:
{context}

Question: {question}
Answer:
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text
