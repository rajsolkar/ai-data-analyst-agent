import subprocess

def query_local_llm(prompt, model="phi3"):
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return result.stdout.decode().strip()
    except Exception as e:
        return f"Error querying model: {e}"
