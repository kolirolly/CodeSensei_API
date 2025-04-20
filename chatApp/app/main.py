from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.groq_api import ask_groq

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": ""})

@app.post("/", response_class=HTMLResponse)
async def get_response(request: Request, user_input: str = Form(...)):
    response = await ask_groq(user_input)
    return templates.TemplateResponse("index.html", {"request": request, "response": response})
