from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.core.routes import router

app = FastAPI(title="CognitOS")

# API
app.include_router(router, prefix="/api")

# Static assets (dashboard CSS/JS/images)
app.mount("/static", StaticFiles(directory="src/static"), name="static")

# Generated projects
app.mount("/output", StaticFiles(directory="output"), name="output")

# HTML templates
templates = Jinja2Templates(directory="src/templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "CognitOS"
        }
    )
    
