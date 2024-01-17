# このコードは、FastAPIとSQLAlchemyを使用して、ToDoリストの項目を更新するためのAPIルーターを定義しています。
from fastapi import APIRouter,Depends   # FastAPIからAPIRouterとDependsをインポートします。

# APIルーターのインスタンスを作成します。
router=APIRouter()

# "/router"のパスでPATCHリクエストを処理するエンドポイントを定義します。
# Swagger UIなどで表示される際にはタグや説明が付与されます。
@router.get("/test",tags=['test'],description='これはテストのAPIです。')
def get():
    hello = 10 + 10
    result = {"Hello": hello}
    # データベースに更新したToDoリストを返します。
    return result