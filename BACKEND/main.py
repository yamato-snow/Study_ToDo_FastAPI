from fastapi import FastAPI
from ROUTER import get_todo,insert_todo,delete_todo,update_todo

app=FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/helloworld")
def read_root():
    hello = 10 + 10
    return {"Hello": hello}

app.include_router(router=get_todo.router)
app.include_router(router=insert_todo.router)
app.include_router(router=delete_todo.router)
app.include_router(router=update_todo.router)