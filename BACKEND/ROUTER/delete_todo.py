from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from DB import db
from CRUD import delete_todo
from SCHEMA.schema import class_schema

router=APIRouter()

@router.delete("/router",response_model=list[class_schema],tags=['todo'],description='delete_todo')
def delete(deadline:str,todo:str,priority:int,genre:str,completed_flag:bool,nowdate:str,db:Session=Depends(db.get_db)):
    result=delete_todo.delete_todolist(deadline=deadline,todo=todo,priority=priority,genre=genre,completed_flag=completed_flag,nowdate=nowdate,db=db)
    return result