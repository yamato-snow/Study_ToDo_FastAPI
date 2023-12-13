# setup.py
import os
import subprocess

# Pythonで提供されているosモジュールとsubprocessモジュールを利用して指定したディレクトリ構造と
# 空のPythonファイルを以下k津で作成するスクリプト

# ディレクトリリスト
dirs = [
    './.venv',
    './BACKEND',
    './BACKEND/CRUD',
    './BACKEND/DB',
    './BACKEND/ROUTER',
    './BACKEND/SCHEMA',
    './FRONTEND'
]

# ディレクトリを作成
for dir in dirs:
    os.makedirs(dir, exist_ok=True)

# Pythonファイルリスト
files = [
    './BACKEND/.env',
    './BACKEND/.gitignore',
    './BACKEND/main.py',
    './BACKEND/CRUD/delete_todo.py',
    './BACKEND/CRUD/get_todo.py',
    './BACKEND/CRUD/insert_todo.py',
    './BACKEND/CRUD/update_todo.py',
    './BACKEND/DB/db.py',
    './BACKEND/ROUTER/delete_todo.py',
    './BACKEND/ROUTER/get_todo.py',
    './BACKEND/ROUTER/insert_todo.py',
    './BACKEND/ROUTER/update_todo.py',
    './BACKEND/SCHEMA/schema.py',
    './FRONTEND/front.py',
    './requirements.txt'
]

# Pythonファイルを作成
for file in files:
    with open(file, 'w') as f:
        pass

# 仮想環境のセットアップ
subprocess.call(['python', '-m', 'venv', './.venv'])

print("Setup complete!")