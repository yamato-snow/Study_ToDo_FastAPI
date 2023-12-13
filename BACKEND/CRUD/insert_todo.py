from sqlalchemy.orm import Session
from sqlalchemy.sql import text
import datetime

def insert_todolist(deadline:datetime.date,todo:str,priority:str,genre:str,db:Session):
    completed_flag=False
    nowdate=datetime.datetime.today().strftime("%Y-%m-%d")
    sql=text('insert into todolist values (%s,%s,%s,%s,%s,%s);'\
             %(repr(deadline),repr(todo),repr(priority),repr(genre),repr(completed_flag),repr(nowdate)))
    db.execute(sql)
    db.commit()

    sql2=text('select * from todolist order by "deadline" asc;')
    result=db.execute(sql2).all()

    return result