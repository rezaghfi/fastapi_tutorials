import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get("/hello/{name}", response_class=HTMLResponse)
async def hello(request: Request, name: str = "reza"):
   return templates.TemplateResponse("index.html", {"request": request, "name":name})


if __name__ == "__main__":
   uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)