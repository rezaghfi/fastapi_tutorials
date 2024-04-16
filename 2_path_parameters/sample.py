import uvicorn
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def index():
   return {"message": "Hello World"}
@app.get("/hello/{name}")
async def hello(name):
   return {"name": name}

if __name__ == "__main__":
   uvicorn.run('sample:app', host="0.0.0.0", port=8000, reload=True)