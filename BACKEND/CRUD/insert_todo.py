# このコードは、SQLAlchemyを使用してToDoリストに新しい項目を挿入し、その後でToDoリストの全項目を取得する関数です。
from sqlalchemy.orm import Session  # SQLAlchemyからSessionをインポートします。
from sqlalchemy.sql import text # SQLAlchemyでSQL文を表現するためのtext関数をインポートします。
import datetime # datetimeモジュールをインポートします。

# ToDoリストに新しい項目を挿入する関数を定義します。
def insert_todolist(deadline:datetime.date,todo:str,priority:str,genre:str,db:Session):
    # 完了フラグをFalse（未完了）に設定します。
    completed_flag=False
    # 現在の日付を取得し、適切な形式に変換します。
    nowdate=datetime.datetime.today().strftime("%Y-%m-%d")
    # SQL文を作成します。このSQL文はToDoリストに新しい項目を挿入します。
    sql=text('insert into todolist values (%s,%s,%s,%s,%s,%s);'\
             %(repr(deadline),repr(todo),repr(priority),repr(genre),repr(completed_flag),repr(nowdate)))
    # 作成したSQL文をデータベースで実行します。
    db.execute(sql)
    # データベースに対する変更をコミットします。
    db.commit()

    # ToDoリストの全項目を取得するためのSQL文を作成します。
    sql2=text('select * from todolist order by "deadline" asc;')
    # 作成したSQL文を実行し、結果を取得します。
    result=db.execute(sql2).all()

    # 取得した結果を返します。
    return result