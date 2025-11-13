import subprocess
import os
from openai import OpenAI

# Try to detect Ollama (local model)
def has_ollama():
    try:
        subprocess.run(["ollama", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False


def query_ai(prompt: str):
    """
    Runs the query through Ollama (if available) or falls back to OpenAI API.
    """

    # Use Ollama if installed locally
    if has_ollama():
        try:
            result = subprocess.run(
                ["ollama", "run", "llama3.2", prompt],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except Exception as e:
            return f" Error using Ollama: {e}"

    #  Otherwise, use OpenAI API (for cloud deployment)
    else:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return "OpenAI API key not found. Please set it in environment or Streamlit secrets."

        try:
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
            )
            return response.choices[0].message.content.strip()

        except Exception as e:
            return f" Error querying OpenAI: {e}"
