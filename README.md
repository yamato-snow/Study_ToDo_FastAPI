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

## 5. データベースの作成

```bash
python app/models/db.py
```
## 6. アプリケーションの起動

```bash
Streamlitを起動します。
streamlit run app.py
```

## 7. アプリケーションの終了

```bash
deactivate
```

## 8. 使用方法
PostgreSQLとは
FastAPIとは