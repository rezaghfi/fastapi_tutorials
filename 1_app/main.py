from typing import Union

from fastapi import FastAPI

# instance of my application and start for use urls
app = FastAPI()

# this function with annotation
@app.get('/')
def read_root():
    return {"hello"}




# for run app call uvicorn
# uvicorn main:app --reload