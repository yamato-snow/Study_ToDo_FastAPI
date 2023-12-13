# Ski Resort Info App

このアプリケーションは、指定したスキー場の情報を取得し表示するものです。天気予報、雪質、リフト券価格などの情報を一元的に確認することができます。

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

使用方法
Streamlitが起動すると、ブラウザが開きアプリケーションの画面が表示されます。
指定したスキー場の情報を検索し、表示します。
お気に入りのスキー場を保存したり、特定の情報を通知する設定も可能です。

現在
・スキー場一覧抽出機能（スクレイピングpy）
・スキー場と現在位置の距離計算機能（utils/web_crawler.py）
・スキー場と現在地の距離ソート機能（app.py）
・ユーザー登録機能の実装（app/models/user.py）
・ユーザーログイン機能の実装（app/models/user.py）
・お気に入り登録機能の実装（app/models/favorite.py）
・お気に入り表示機能の実装（app.py）

実装予定
・天気情報の取得
・天気情報の表示
・登録ユーザーへの天気お知らせ機能の実装

アップグレード予定
・ユーザー属性情報の追加（住んでいる地域、車の有無、家族構成等）

pip install streamlit beautifulsoup4 requests pandas numpy geopy sqlalchemy googlemaps flask flask_sqlalchemy streamlit-ace