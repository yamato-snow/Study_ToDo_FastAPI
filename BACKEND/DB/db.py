# このコードは、Pythonでのデータベース接続設定を行うためのものです。
import os   # 標準ライブラリosをインポートします。これは環境変数やファイルパスの操作に使用されます。
from posixpath import dirname   # posixpathモジュールからdirname関数をインポートします。これはファイルパスのディレクトリ名を取得するのに使用されます。
from dotenv import load_dotenv  # dotenvライブラリからload_dotenv関数をインポートします。これは環境変数を読み込むために使用されます。
from sqlalchemy import create_engine    # SQLAlchemyからcreate_engine関数をインポートします。これはデータベースへの接続を管理するエンジンを作成するために使用されます。
from sqlalchemy.ext.declarative import declarative_base # SQLAlchemyからdeclarative_base関数をインポートします。これはモデルクラスの基底クラスを作成するために使用されます。
from sqlalchemy.orm import sessionmaker # SQLAlchemyからsessionmaker関数をインポートします。これはセッションを作成するファクトリ関数を作成するために使用されます。
from os.path import join,dirname    # os.pathモジュールからjoinとdirname関数をインポートします。これらはファイルパスの操作に使用されます。

# .envファイルのパスを作成します。
dotenv_path=join(dirname(__file__),'../.env')
# 環境変数を読み込みます。
load_dotenv(dotenv_path)

# データベースの接続情報を環境変数から取得します。
DB_USER=os.environ.get("DB_USER")
DB_PASS=os.environ.get("DB_PASS")
DB_HOST=os.environ.get("DB_HOST")
DB_NAME=os.environ.get("DB_NAME")

# SQLAlchemyデータベースURLを作成します。
SQLALCHEMY_DATABASE_URL='postgresql+psycopg2://{}:{}@{}:5433/{}'.format(
    DB_USER,
    DB_PASS,
    DB_HOST,
    DB_NAME
)

# データベース接続エンジンを作成します。
engine=create_engine(SQLALCHEMY_DATABASE_URL)

# セッションファクトリを作成します。これはデータベースセッションを生成するために使用されます。
Sessionlocal = sessionmaker(autocommit=False,autoflush=True,bind=engine)
# データベースモデルの基底クラスを作成します。
Base=declarative_base()

# データベースセッションを取得する関数を定義します。
def get_db():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close()