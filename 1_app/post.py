from fastapi import FastAPI

app = FastAPI()

app.post("/post", status_code=201)
def read():
    return {f"hello"}

#