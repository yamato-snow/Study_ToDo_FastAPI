# このコードは、FastAPIとSQLAlchemyを使用して、ToDoリストの項目を更新するためのAPIルーターを定義しています。
from fastapi import APIRouter,Depends   # FastAPIからAPIRouterとDependsをインポートします。
from sqlalchemy.orm import Session  # SQLAlchemyからSessionをインポートします。
from DB import db   # DB.pyからdbモジュールをインポートします。これはデータベースの接続設定などを含みます。
from CRUD import update_todo    # CRUD.pyからupdate_todo関数をインポートします。これはToDoリストの更新に関連する操作を行う関数です。
from SCHEMA.schema import class_schema  # SCHEMA/schema.pyからclass_schemaをインポートします。これはデータモデルのスキーマを表すクラスです。

# APIルーターのインスタンスを作成します。
router=APIRouter()

# "/router"のパスでPATCHリクエストを処理するエンドポイントを定義します。
# このエンドポイントはToDoリストの項目を更新するための処理を行います。
# Swagger UIなどで表示される際にはタグや説明が付与されます。
@router.patch("/router",response_model=list[class_schema],tags=['todo'],description='update_todo')
def update(deadline:str,todo:str,priority:int,genre:str,nowdate:str,db:Session=Depends(db.get_db)):
    # SQLAlchemyのセッションを依存性として注入します。これにより、データベース操作が可能になります。
    result=update_todo.update_todolist(deadline=deadline,todo=todo,priority=priority,genre=genre,nowdate=nowdate,db=db)
    # データベースに更新したToDoリストを返します。
    return result