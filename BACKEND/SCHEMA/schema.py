from pydantic import BaseModel
import datetime

class class_schema(BaseModel):
    #期日
    deadline:datetime.date
    #やること
    todo:str
    #優先度
    priority:int
    #カテゴリ
    genre:str
    #完了フラグ
    completed_flag:bool
    #作成日
    nowdate:datetime.date
    class Config:
        orm_mode = True