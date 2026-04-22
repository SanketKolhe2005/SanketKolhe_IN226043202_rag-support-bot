import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key safely
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(query, docs):
    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
You are a customer support assistant.

STRICT RULES:
- Answer ONLY from the given context
- Do NOT guess
- If answer is not found, say: "I don't know"

Context:
{context}

Question:
{query}

Answer:
"""

    chat = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant"
    )

    return chat.choices[0].message.content