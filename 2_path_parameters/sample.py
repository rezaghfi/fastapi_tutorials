import uvicorn
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def index():
   return {"message": "Hello World"}

#path parameter
@app.get("/hello/{name}")
async def hello(name: str):
   return {f"hello my lazy {name} you are my best friend:)"}

@app.get('/{name}/{age}')
async def hello2(name: str, age: int):
   return (f"hello {name}, you are {age} years olds.")

if __name__ == "__main__":
   uvicorn.run('sample:app', host="127.0.0.1", port=8000, reload=True)