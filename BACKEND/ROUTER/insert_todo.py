# このコードは、FastAPIとSQLAlchemyを用いて、ToDoリストに新しい項目を追加するためのAPIルーターを定義しています。
from fastapi import APIRouter,Depends   # FastAPIからAPIRouterとDependsをインポートします。
from sqlalchemy.orm import Session  # SQLAlchemyからSessionをインポートします。
from DB import db   # DB.pyからdbモジュールをインポートします。これはデータベースの接続設定などを含みます。
from CRUD import insert_todo    # CRUD.pyからinsert_todo関数をインポートします。これはToDoリストの挿入に関連する操作を行う関数です。
from SCHEMA.schema import class_schema  # SCHEMA/schema.pyからclass_schemaをインポートします。これはデータモデルのスキーマを表すクラスです。

# APIルーターのインスタンスを作成します。
router=APIRouter()

# "/router"のパスでPOSTリクエストを処理するエンドポイントを定義します。
# このエンドポイントはToDoリストに項目を追加し、Swagger UIなどで表示される際にタグや説明が付与されます。
@router.post("/router",response_model=list[class_schema],tags=['todo'],description='insert_todo')
def insert(deadline:str,todo:str,priority:str,genre:str,db:Session=Depends(db.get_db)):
    # SQLAlchemyのセッションを依存性として注入します。これにより、データベース操作が可能になります。
    result=insert_todo.insert_todolist(deadline=deadline,todo=todo,priority=priority,genre=genre,db=db)
    
    # データベースに挿入したToDoリストを返します。
    return result