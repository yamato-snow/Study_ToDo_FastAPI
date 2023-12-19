# このコードは、SQLAlchemyを使用してToDoリストの特定の項目を削除し、その後でToDoリストの全項目を取得する関数です。
from sqlalchemy.orm import Session  # SQLAlchemyからSessionをインポートします。
from sqlalchemy.sql import text # SQLAlchemyでSQL文を表現するためのtext関数をインポートします。
import datetime # datetimeモジュールをインポートします。

# ToDoリストの特定の項目を削除する関数を定義します。
def delete_todolist(deadline:datetime.date,todo:str,priority:int,genre:str,completed_flag:bool,nowdate:datetime.date,db:Session):
    # SQL文を作成します。このSQL文はToDoリストから特定の条件を満たす項目を削除します。
    sql=text('delete from todolist where "deadline"=%s and "todo"=%s and \n\
             "priority"=%s and "genre"=%s and "completed_flag"=%s and "nowdate"=%s;'\
             %(repr(deadline),repr(todo),repr(priority),repr(genre),repr(completed_flag),repr(nowdate)))
    # 作成したSQL文をデータベースで実行します。
    db.execute(sql)
    # データベースに対する変更をコミットします。
    db.commit()

    # ToDoリストの全項目を取得するためのSQL文を作成します。
    sql2=text('select * from todolist order by "deadline" asc')
     # 作成したSQL文を実行し、結果を取得します。
    result=db.execute(sql2).all()
    # 取得した結果を返します。
    return result