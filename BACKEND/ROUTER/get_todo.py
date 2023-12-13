from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from DB import db
from CRUD import get_todo
from SCHEMA.schema import class_schema

router=APIRouter()

@router.get("/router",response_model=list[class_schema],tags=['todo'],description='get_todo')
def get(db:Session=Depends(db.get_db)):
    result=get_todo.get_todolist(db=db)
    return result