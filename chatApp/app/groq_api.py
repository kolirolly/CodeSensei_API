import os
import httpx
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "meta-llama/llama-4-scout-17b-16e-instruct")

async def ask_groq(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }

    async with httpx.AsyncClient() as client:
        res = await client.post(
            "https://api.groq.com/openai/v1/chat/completions",
            json=payload,
            headers=headers
        )

        if res.status_code != 200:
            print(f"Error: {res.status_code}")
            print(res.text)
            return f"Error: {res.status_code}\n{res.text}"

        data = res.json()
        if "choices" not in data:
            print("Unexpected response:", data)
            return "Groq API returned an unexpected response."

        return data["choices"][0]["message"]["content"]
