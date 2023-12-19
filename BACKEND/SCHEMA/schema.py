# このコードは、pydanticライブラリを使用してデータモデル（スキーマ）を定義しています。Pydanticは、データのバリデーションと設定管理に使われるPythonライブラリです。
from pydantic import BaseModel  # PydanticのBaseModelをインポートします。
import datetime # datetimeモジュールをインポートします。

# ToDoリストの項目を表すデータモデル（スキーマ）を定義します。
class class_schema(BaseModel):
    # 期日を表すフィールドです。datetime.date型を使用します。
    deadline:datetime.date
    # ToDoリストの項目内容を表すフィールドです。文字列型を使用します。
    todo:str
    # 優先度を表すフィールドです。整数型を使用します。
    priority:int
    # カテゴリを表すフィールドです。文字列型を使用します。
    genre:str
    # 完了フラグを表すフィールドです。ブール型を使用します。
    completed_flag:bool
    # 作成日を表すフィールドです。datetime.date型を使用します。
    nowdate:datetime.date
    # Pydanticモデルの設定クラスです。
    class Config:
        # ORMモードを有効にします。これにより、ORMオブジェクトとの互換性が向上します。
        orm_mode = True