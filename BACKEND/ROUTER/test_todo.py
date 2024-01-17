# このコードは、FastAPIとSQLAlchemyを使用して、ToDoリストの項目を更新するためのAPIルーターを定義しています。
from fastapi import APIRouter,Depends   # FastAPIからAPIRouterとDependsをインポートします。

# APIルーターのインスタンスを作成します。
router=APIRouter()

# "/router"のパスでPATCHリクエストを処理するエンドポイントを定義します。
# Swagger UIなどで表示される際にはタグや説明が付与されます。
@router.post("/test",tags=['test'],description='これはテストのAPIです。')
def post(weight:float,height:float):
    bmi = weight / (height/100)**2
    result = {"BMI": bmi}
    # データベースに更新したToDoリストを返します。
    return result