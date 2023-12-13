from sqlalchemy.orm import Session
from sqlalchemy.sql import text

def get_todolist(db:Session):
    sql=text('select * from todolist order by "deadline" asc;')
    result=db.execute(sql).all()
    return result