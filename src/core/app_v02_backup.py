from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>CognitOS</title>
</head>
<body style="font-family:Arial;text-align:center;padding:40px;background:#111;color:white;">
    <h1>🚀 CognitOS</h1>
    <h2>Web UI is Running!</h2>
    <p>Your FastAPI server is working successfully.</p>
</body>
</html>
"""
