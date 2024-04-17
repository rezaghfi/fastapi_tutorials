import fastapi
import uvicorn

app = fastapi.FastAPI()

@app.get('/')
def error1():
    return ("enter name like query in url")
#query is it in url after ? mark
@app.get('/')
def show_name(name):
    return f"your name is {name}"

if __name__ == '__main__':
    uvicorn.run('sample:app', host='127.0.0.1', port=8000, reload=True)