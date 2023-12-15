# Todoアプリケーション
このアプリケーションは[PostgreSQLとFastAPIで作るTODOアプリケーション](https://zenn.dev/tirimen/articles/7b5861c40e8a77)のサンプルコードです。<br>
このアプリケーションはtirimenさんのサンプルコードを元に作成しています。<br>

## インストール方法

1. このレポジトリをローカル環境にクローンします。

## 1. pyenvでのPythonバージョンの指定

指定したいPythonのバージョン（例：3.11.5）をpyenvを使用して指定します。

```bash
pyenv local 3.11.5
```
### 1.1 **注：** pyenvに指定したバージョンがない場合は、以下のコマンドでインストールします。

```bash
pyenv install 3.11.5
```

## 2. Python仮想環境の作成とアクティベーション
Pythonの仮想環境を作成します。
```bash
python -m venv .venv
```
### 2.1 Windowsでのアクティベーション
- パワーシェルの場合
```bash
.venv/Scripts/activate.ps1
```

- コマンドプロンプトの場合
```bash
.venv\Scripts\activate.bat
```
### 2.2 macOSでのアクティベーション

- 管理者権限の場合
```bash
source .venv/bin/activate
```

- 通常の場合
```bash
. .venv/bin/activate
```

## 3. pipのアップデート

仮想環境内のpipをアップデートします。

```bash
python -m pip install --upgrade pip
```

## 4. 必要なパッケージのインストール

```bash
pip install -r requirements.txt
```

## 5. 各ファイルの作成　※git cloneした場合は不要
```bash
python setup.py
```
## 6. アプリケーションの起動

```bash
FastAPIを起動する
uvicorn main:app --reload
```

## 7. アプリケーションの終了

```bash
deactivate
```

## 8. 使用方法
PostgreSQLとは
FastAPIとは

## ※注意
macバージョンでは、以下のエラーが発生する場合があります。
```bash
Installing build dependencies ... done

 Getting requirements to build wheel ... error

 error: subprocess-exited-with-error

  

 × Getting requirements to build wheel did not run successfully.

 │ exit code: 1

 ╰─&gt; [21 lines of output]

   running egg_info

   writing psycopg2.egg-info/PKG-INFO

   writing dependency_links to psycopg2.egg-info/dependency_links.txt

   writing top-level names to psycopg2.egg-info/top_level.txt

    

   Error: pg_config executable not found.

    

   pg_config is required to build psycopg2 from source. Please add the directory

   containing pg_config to the $PATH or specify the full executable path with the

   option:

    

     python setup.py build_ext --pg-config /path/to/pg_config build ...

    

   or with the pg_config option in 'setup.cfg'.

    

   If you prefer to avoid building psycopg2 from source, please install the PyPI

   'psycopg2-binary' package instead.

    

   For further information please check the 'doc/src/install.rst' file (also at

   &lt;https://www.psycopg.org/docs/install.html&gt;).

    

   [end of output]

  

 note: This error originates from a subprocess, and is likely not a problem with pip.

error: subprocess-exited-with-error

× Getting requirements to build wheel did not run successfully.

│ exit code: 1

╰─&gt; See above for output.

note: This error originates from a subprocess, and is likely not a problem with pip.
```
その場合は、以下の記事を参考にしてください。
[【小ネタ】Macにpsycopg2をインストールする時のメモ](https://dev.classmethod.jp/articles/mac-psycopg2-install/)


# プロジェクト実施時のメモ
- バックエンド・フロントエンドは`コマンドプロンプト、パワーシェル、ターミナル`はいずれかのコンソールを１つずつ開く必要がある。
## 1. バックエンド起動方法(FastAPI)
- 一つ目の`コマンドプロンプト、パワーシェル、ターミナル`いずれかを開き、バックエンドを起動する。
### 1.1 プロジェクトフォルダに移動
```bash
cd 02_todo_list_tool
```
### 1.2 仮想環境の立ち上げ
- windowsコマンドプロンプト
```bash
.venv\Scripts\activate.bat
```
-  windowsパワーシェル
```bash
.venv\Scripts\activate.ps1
```
-  macOS
```bash
. .venv/bin/activate
```
### 1.3 BACKENDを起動
```bash
uvicorn main:app --reload --app-dir BACKEND
```

## 2. フロントエンド起動方法(Streamlit)
- 二つ目の`コマンドプロンプト、パワーシェル、ターミナル`いずれかを開き、フロントエンドを起動する。
### 2.1 プロジェクトフォルダに移動
```bash
cd 02_todo_list_tool
```
### 2.2 仮想環境の立ち上げ
- windowsコマンドプロンプト
```bash
.venv\Scripts\activate.bat
```
-  windowsパワーシェル
```bash
.venv\Scripts\activate.ps1
```
-  macOS
```bash
. .venv/bin/activate
```
### 2.3 FRONTENDを起動
```bash
streamlit run FRONTEND/front.py
```
