from sqlalchemy.orm import Session
from sqlalchemy.sql import text
import datetime

def update_todolist(deadline:datetime.date,todo:str,priority:int,genre:str,nowdate:datetime.date,db:Session):
    sql=text('update todolist set "completed_flag"=True where "deadline"=%s and "todo"=%s and \n\
             "priority"=%s and "genre"=%s and "nowdate"=%s;'\
             %(repr(deadline),repr(todo),repr(priority),repr(genre),repr(nowdate)))
    db.execute(sql)
    db.commit()

    sql2=text('select * from todolist order by "deadline" asc')
    result=db.execute(sql2).all()

    return result