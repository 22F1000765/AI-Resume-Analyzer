import os

from google import genai


def generate_llm_response(prompt: str) -> str:
    """
    Generate a response from the Gemini LLM.
    """

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is not configured.")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents=prompt,
    )

    return response.text