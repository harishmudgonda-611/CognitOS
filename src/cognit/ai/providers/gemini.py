import json
import time
from pathlib import Path

import requests


class GeminiProvider:

    def __init__(self):

        config_path = Path("config/models.json")

        with config_path.open("r", encoding="utf-8") as f:
            config = json.load(f)

        self.api_key = config["gemini"]["api_key"]
        self.model = config["gemini"]["model"]

    def generate(self, prompt: str):

        if not self.api_key:
            return {
                "status": "error",
                "message": "Gemini API key not configured."
            }

        url = (
            "https://generativelanguage.googleapis.com/v1beta/models/"
            f"{self.model}:generateContent?key={self.api_key}"
        )

        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ]
        }

        retries = 3

        for attempt in range(retries):

            try:
                response = requests.post(
                    url,
                    json=payload,
                    timeout=60
                )

                if response.status_code == 200:
                    data = response.json()

                    text = data["candidates"][0]["content"]["parts"][0]["text"]

                    return {
                        "status": "success",
                        "provider": "gemini",
                        "text": text
                    }

                if response.status_code == 503:
                    if attempt < retries - 1:
                        print(f"Gemini busy... retry {attempt + 1}/{retries}")
                        time.sleep(2)
                        continue

                return {
                    "status": "error",
                    "code": response.status_code,
                    "response": response.text
                }

            except requests.RequestException as e:
                if attempt < retries - 1:
                    print(f"Network error... retry {attempt + 1}/{retries}")
                    time.sleep(2)
                    continue

                return {
                    "status": "error",
                    "message": str(e)
                }
                
