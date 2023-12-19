# このソースコードを実行すると、サーバーが起動します。
# サーバーが起動したら、ブラウザで http://localhost:8000/docs にアクセスしてください。
# そうすると、Swagger UIが表示されます。
# Swagger UIを使うと、APIの仕様を確認したり、APIを実行したりすることができます。
# また、 http://localhost:8000/redoc にアクセスすると、ReDocが表示されます。
# ReDocもSwagger UIと同様に、APIの仕様を確認したり、APIを実行したりすることができます。
# どちらも同じことができるので、好きな方を使ってください。

# FastAPIライブラリをインポートします。
from fastapi import FastAPI
# 別のファイルからToDoリストに関連する関数をインポートします。
from ROUTER import get_todo,insert_todo,delete_todo,update_todo

# FastAPIのインスタンスを作成します。これがアプリケーションのメインオブジェクトになります。
app=FastAPI()

# ルートURLへのGETリクエストを処理するためのエンドポイントを定義します。
@app.get("/")
def read_root():
    # この関数は、単純なJSONレスポンスを返します。
    return {"Hello": "World"}

# "/helloworld"のパスでGETリクエストを処理するためのエンドポイントを定義します。
@app.get("/helloworld")
def read_root():
    # 簡単な計算を行います。
    hello = 10 + 10
     # 計算結果を含むJSONレスポンスを返します。
    return {"Hello": hello}

# ToDoリスト関連の各ルーターをアプリケーションに含めます。
# これらはToDoリストの操作（取得、挿入、削除、更新）を処理するためのエンドポイントを提供します。
app.include_router(router=get_todo.router)
app.include_router(router=insert_todo.router)
app.include_router(router=delete_todo.router)
app.include_router(router=update_todo.router)