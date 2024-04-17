import uvicorn
from fastapi import FastAPI, Path
app = FastAPI()
@app.get("/{name}")
async def hello(name:str=Path(...,min_length=3, max_length=10)):
   return {"name": name}
# gt − greater than
# ge − greater than or equal
# lt − less than
# le − less than or equal

if __name__ == '__main__':
    uvicorn.run('valid:app', host='127.0.0.1', port=8000, reload=True)