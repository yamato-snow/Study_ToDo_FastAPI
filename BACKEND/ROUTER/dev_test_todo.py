# このコードは、FastAPIとSQLAlchemyを使用してデータベース操作を行うためのAPIルーターを定義しています。
from fastapi import APIRouter,Depends   # FastAPIからAPIRouterとDependsをインポートします。
from sqlalchemy.orm import Session  # SQLAlchemyからSessionをインポートします。
from DB import db   # DB.pyからdbモジュールをインポートします。これはデータベースの接続設定などを含みます。
from CRUD import dev_test_todo   # CRUD.pyからdev_test_todo関数をインポートします。これはToDoリストの取得に関連する操作を行う関数です。
from SCHEMA.schema import class_schema  # SCHEMA/schema.pyからclass_schemaをインポートします。これはデータモデルのスキーマを表すクラスです。

# APIルーターのインスタンスを作成します。
router=APIRouter()

# "/router"のパスでGETリクエストを処理するエンドポイントを定義します。
# このエンドポイントはToDoリストを返し、Swagger UIなどで表示される際にタグや説明が付与されます。
@router.get("/test",tags=['test'],description='これはデータベースから取得してきた値のBMIを計算するAPIです。')
def get(db:Session=Depends(db.get_db)):
    # SQLAlchemyのセッションを依存性として注入します。これにより、データベース操作が可能になります。
    result=dev_test_todo.dev_test_todo(db=db)
    # データベースから取得した値をもとに計算をします。
    # weightの値を取得します
    weight = result[0][0]
    # heightの値を取得します
    height = result[0][1]

    print("log：" + str(weight) + " " + str(height)) 

    bmi = weight / (height/100)**2
    result = {"BMI": bmi}

    print("log：" + str(result))

    # データベースから取得したToDoリストを返します。
    return result