import uvicorn
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def index():
   return {"message": "Hello World"}
@app.get("/hello/{name}")
async def hello(name: str):
   return {f"hello my lazy {name} you are my best friend:)"}

if __name__ == "__main__":
   uvicorn.run('sample:app', host="0.0.0.0", port=8000, reload=True)