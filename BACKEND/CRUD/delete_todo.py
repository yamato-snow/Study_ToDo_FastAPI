# このファイルにdelete_todolist関数を記述しています。
# この関数は、todolistテーブルからデータを削除する関数です。
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
import datetime

# todolistテーブルからデータを削除する関数です。
def delete_todolist(deadline:datetime.date,todo:str,priority:int,genre:str,completed_flag:bool,nowdate:datetime.date,db:Session):
    # todolistテーブルからデータを削除します。
    sql=text('delete from todolist where "deadline"=%s and "todo"=%s and \n\
             "priority"=%s and "genre"=%s and "completed_flag"=%s and "nowdate"=%s;'\
             %(repr(deadline),repr(todo),repr(priority),repr(genre),repr(completed_flag),repr(nowdate)))
    # SQLを実行します。
    db.execute(sql)
    # 保存します。
    db.commit()

    # todolistテーブルのデータを全て取得します。
    sql2=text('select * from todolist order by "deadline" asc')
    # SQLを実行します。
    result=db.execute(sql2).all()
    # 取得したデータを返します。
    return result