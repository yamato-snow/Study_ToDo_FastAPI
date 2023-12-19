# このソースコードを実行すると、サーバーが起動します。
# サーバーが起動したら、ブラウザで http://localhost:8000/docs にアクセスしてください。
# そうすると、Swagger UIが表示されます。
# Swagger UIを使うと、APIの仕様を確認したり、APIを実行したりすることができます。
# また、 http://localhost:8000/redoc にアクセスすると、ReDocが表示されます。
# ReDocもSwagger UIと同様に、APIの仕様を確認したり、APIを実行したりすることができます。
# どちらも同じことができるので、好きな方を使ってください。

from fastapi import FastAPI
from ROUTER import get_todo,insert_todo,delete_todo,update_todo

app=FastAPI()

# このAPIは、{"Hello": "World"}というJSONを返します。
@app.get("/")
def read_root():
    return {"Hello": "World"}

# このAPIは、{"Hello": 20}というJSONを返します。
@app.get("/helloworld")
def read_root():
    hello = 10 + 10
    return {"Hello": hello}

# get_todo.pyのrouterを読み込みます。
app.include_router(router=get_todo.router)
# insert_todo.pyのrouterを読み込みます。
app.include_router(router=insert_todo.router)
# delete_todo.pyのrouterを読み込みます。
app.include_router(router=delete_todo.router)
# update_todo.pyのrouterを読み込みます。
app.include_router(router=update_todo.router)