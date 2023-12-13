from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from DB import db
from CRUD import insert_todo
from SCHEMA.schema import class_schema

router=APIRouter()

@router.post("/router",response_model=list[class_schema],tags=['todo'],description='insert_todo')
def insert(deadline:str,todo:str,priority:str,genre:str,db:Session=Depends(db.get_db)):
    result=insert_todo.insert_todolist(deadline=deadline,todo=todo,priority=priority,genre=genre,db=db)
    return result