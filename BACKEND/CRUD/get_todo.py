# この関数は、SQLAlchemyを使用してデータベースからToDoリストの全項目を取得し、それらをリストとして返す機能を提供します。
from sqlalchemy.orm import Session  # SQLAlchemyのSessionをインポートします。
from sqlalchemy.sql import text # SQLAlchemyでSQL文を表現するためのtext関数をインポートします。

# ToDoリストの全項目を取得する関数を定義します。
def get_todolist(db:Session):
    # SQL文を作成します。このSQL文はToDoリストの全項目を締め切り日で昇順に取得します。
    sql=text('select * from todolist order by "deadline" asc;')
    # 作成したSQL文をデータベースで実行し、結果を取得します。
    result=db.execute(sql).all()
    # 取得した結果を返します。
    return result