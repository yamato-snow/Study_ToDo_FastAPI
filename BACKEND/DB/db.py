import os
from posixpath import dirname
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os.path import join,dirname

dotenv_path=join(dirname(__file__),'../.env')
load_dotenv(dotenv_path)

DB_USER=os.environ.get("DB_USER")
DB_PASS=os.environ.get("DB_PASS")
DB_HOST=os.environ.get("DB_HOST")
DB_NAME=os.environ.get("DB_NAME")

SQLALCHEMY_DATABASE_URL='postgresql+psycopg2://{}:{}@{}:5433/{}'.format(
    DB_USER,
    DB_PASS,
    DB_HOST,
    DB_NAME
)

engine=create_engine(SQLALCHEMY_DATABASE_URL)

Sessionlocal = sessionmaker(autocommit=False,autoflush=True,bind=engine)
Base=declarative_base()

def get_db():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close()