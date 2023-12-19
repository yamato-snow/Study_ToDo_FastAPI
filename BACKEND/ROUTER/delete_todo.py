# このコードは、FastAPIとSQLAlchemyを利用して、ToDoリストの項目を削除するためのAPIルーターを定義しています。
from fastapi import APIRouter,Depends   # FastAPIからAPIRouterとDependsをインポートします。
from sqlalchemy.orm import Session  # SQLAlchemyからSessionをインポートします。
from DB import db   # DB.pyからdbモジュールをインポートします。これはデータベースの接続設定などを含みます。
from CRUD import delete_todo    # CRUD.pyからdelete_todo関数をインポートします。これはToDoリストの削除に関連する操作を行う関数です。
from SCHEMA.schema import class_schema  # SCHEMA/schema.pyからclass_schemaをインポートします。これはデータモデルのスキーマを表すクラスです。

# APIルーターのインスタンスを作成します。
router=APIRouter()

# "/router"のパスでDELETEリクエストを処理するエンドポイントを定義します。
# このエンドポイントはToDoリストの項目を削除するための処理を行います。
# Swagger UIなどで表示される際にはタグや説明が付与されます。
@router.delete("/router",response_model=list[class_schema],tags=['todo'],description='delete_todo')
def delete(deadline:str,todo:str,priority:int,genre:str,completed_flag:bool,nowdate:str,db:Session=Depends(db.get_db)):
    # SQLAlchemyのセッションを依存性として注入します。これにより、データベース操作が可能になります。
    result=delete_todo.delete_todolist(deadline=deadline,todo=todo,priority=priority,genre=genre,completed_flag=completed_flag,nowdate=nowdate,db=db)
    # データベースでToDoリストの項目を削除した結果を返します。
    return result