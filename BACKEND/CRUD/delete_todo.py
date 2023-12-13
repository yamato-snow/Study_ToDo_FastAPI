from sqlalchemy.orm import Session
from sqlalchemy.sql import text
import datetime

def delete_todolist(deadline:datetime.date,todo:str,priority:int,genre:str,completed_flag:bool,nowdate:datetime.date,db:Session):
    sql=text('delete from todolist where "deadline"=%s and "todo"=%s and \n\
             "priority"=%s and "genre"=%s and "completed_flag"=%s and "nowdate"=%s;'\
             %(repr(deadline),repr(todo),repr(priority),repr(genre),repr(completed_flag),repr(nowdate)))
    db.execute(sql)
    db.commit()

    sql2=text('select * from todolist order by "deadline" asc')
    result=db.execute(sql2).all()

    return result