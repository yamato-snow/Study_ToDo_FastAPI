# このコードは、FastAPIとSQLAlchemyを使用してデータベース操作を行うためのAPIルーターを定義しています。
from fastapi import APIRouter,Depends   # FastAPIからAPIRouterとDependsをインポートします。
from sqlalchemy.orm import Session  # SQLAlchemyからSessionをインポートします。
from DB import db   # DB.pyからdbモジュールをインポートします。これはデータベースの接続設定などを含みます。
from CRUD import get_todo   # CRUD.pyからget_todo関数をインポートします。これはToDoリストの取得に関連する操作を行う関数です。
from SCHEMA.schema import class_schema  # SCHEMA/schema.pyからclass_schemaをインポートします。これはデータモデルのスキーマを表すクラスです。

# APIルーターのインスタンスを作成します。
router=APIRouter()

# "/router"のパスでGETリクエストを処理するエンドポイントを定義します。
# このエンドポイントはToDoリストを返し、Swagger UIなどで表示される際にタグや説明が付与されます。
@router.get("/router",response_model=list[class_schema],tags=['todo'],description='get_todo')
def get(db:Session=Depends(db.get_db)):
    # SQLAlchemyのセッションを依存性として注入します。これにより、データベース操作が可能になります。
    result=get_todo.get_todolist(db=db)
    # データベースから取得したToDoリストを返します。
    return result