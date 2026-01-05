import subprocess
import json

def content_agent(weather_data: dict):
    prompt = f"""
You are a professional weather reporter.

Write a clear, simple paragraph explaining the following weather data
for a normal person.

{json.dumps(weather_data, indent=2)}
"""

    result = subprocess.run(
        ["ollama", "run", "llama3.1"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()
