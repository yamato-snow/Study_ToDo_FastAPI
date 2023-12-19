# この関数は、SQLAlchemyを使用してToDoリストの特定の項目を更新し、その後でToDoリストの全項目を取得する機能を提供します。
from sqlalchemy.orm import Session  # SQLAlchemyのSessionをインポートします。
from sqlalchemy.sql import text # SQLAlchemyでSQL文を表現するためのtext関数をインポートします。
import datetime # datetimeモジュールをインポートします。

# ToDoリストの特定の項目を更新する関数を定義します。
def update_todolist(deadline:datetime.date,todo:str,priority:int,genre:str,nowdate:datetime.date,db:Session):
    # SQL文を作成します。このSQL文はToDoリストの特定の項目の「completed_flag」をTrue（完了）に更新します。
    sql=text('update todolist set "completed_flag"=True where "deadline"=%s and "todo"=%s and \n\
             "priority"=%s and "genre"=%s and "nowdate"=%s;'\
             %(repr(deadline),repr(todo),repr(priority),repr(genre),repr(nowdate)))
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