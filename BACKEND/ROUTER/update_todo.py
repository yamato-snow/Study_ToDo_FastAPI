from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from DB import db
from CRUD import update_todo
from SCHEMA.schema import class_schema

router=APIRouter()

@router.patch("/router",response_model=list[class_schema],tags=['todo'],description='update_todo')
def update(deadline:str,todo:str,priority:int,genre:str,nowdate:str,db:Session=Depends(db.get_db)):
    result=update_todo.update_todolist(deadline=deadline,todo=todo,priority=priority,genre=genre,nowdate=nowdate,db=db)
    return result