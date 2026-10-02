import os

def llm_available():
    return bool(os.getenv("GROQ_API_KEY"))

def generate_optional_summary(prompt: str):
    # Optional Groq integration. The deterministic pipeline remains usable without an API key.
    if not llm_available():
        return None
    try:
        from openai import OpenAI
        client = OpenAI(
            api_key=os.environ["GROQ_API_KEY"],
            base_url="https://api.groq.com/openai/v1",
        )
        response = client.chat.completions.create(
            model=os.getenv("GROQ_MODEL", "openai/gpt-oss-120b"),
            messages=[
                {"role": "system", "content": "You are a concise coordination assistant. Never invent availability or verification."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
        )
        return response.choices[0].message.content
    except Exception:
        return None
