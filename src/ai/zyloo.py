import json
import urllib.request

API_KEY = "sk-zy-7da9d98429848580304800315abbe048b41e40a69e50a673"

def chat(prompt):
    data = {
        "model": "zyloo/kimi-k3",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    req = urllib.request.Request(
        "https://api.zyloo.io/v1/chat/completions",
        data=json.dumps(data).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
    )

    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode("utf-8"))
        return result["choices"][0]["message"]["content"]


