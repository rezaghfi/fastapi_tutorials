from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello_world():
   return 'hello im get method api'

# می تونی نام دو تا تابع رو شبیه هم بنویسی
@app.get('/status')
def hello_world(status: str = '201'):
   return "get method with diffrent status code"
# The function returns a JSON response, however, it can return dict, list, str, int, etc. It can also return Pydantic models.


# uvicorn get:index --reload