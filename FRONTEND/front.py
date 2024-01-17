# このコードは、streamlitとrequestsライブラリを使用してWebベースのToDoリストアプリケーションのフロントエンドを構築するものです。
import streamlit as st
import requests
import datetime

# サイドバーでページ選択を行うためのセレクトボックスを作成します。
page=st.sidebar.selectbox('ページ名',['新規登録','未完了リスト','完了リスト','テスト'])

# 新規登録ページの処理です。
if page=='新規登録':
    st.title('新規登録')
    with st.form(key='新規登録'):
        # 入力フォームを作成します。
        deadline:datetime.date=st.date_input('期日').strftime('%Y-%m-%d')
        todo:str=st.text_input('Todo',max_chars=100)
        priority:int=st.number_input('優先度',0)
        genre:str=st.text_input('カテゴリ',max_chars=15)
        submit_button=st.form_submit_button(label='登録')

        # 登録ボタンが押された場合の処理です。
        if submit_button:
            # FastAPIサーバーにPOSTリクエストを送信します。
            url='http://127.0.0.1:8000/router?deadline=%s&todo=%s&priority=%s&genre=%s'\
                %(repr(deadline)[1:-1],repr(todo)[1:-1],repr(priority),repr(genre)[1:-1])
            res=requests.post(url=url)
            st.success('登録完了')

# 未完了リストページの処理です。
elif page=='未完了リスト':
    st.title('未完了リスト')
    # FastAPIサーバーからToDoリストを取得します。
    url='http://127.0.0.1:8000/router'
    res=requests.get(url=url)
    records=res.json()
    # 未完了の項目を表示します。
    i=0
    for record in records:
        i+=1
        if record.get('completed_flag')==False:
            with st.form(key=str(i)):
                st.subheader('・'+record.get('deadline'))
                st.write(record.get('todo'))
                submit_button_1=st.form_submit_button(label='完了')
                submit_button_2=st.form_submit_button(label='削除')
                 # 完了ボタンが押された場合の処理です。
                if submit_button_1:
                    # 項目を完了状態に更新します。
                    # 関連するデータを取得し、FastAPIサーバーにPATCHリクエストを送信します。
                    deadline:datetime.date=record.get('deadline')
                    todo:str=record.get('todo')
                    priority:int=record.get('priority')
                    genre:str=record.get('genre')
                    nowdate:datetime.date=record.get('nowdate')
                    url='http://127.0.0.1:8000/router?deadline=%s&todo=%s&priority=%s&genre=%s&nowdate=%s'\
                        %(repr(deadline)[1:-1],repr(todo)[1:-1],repr(priority),repr(genre)[1:-1],repr(nowdate)[1:-1])
                    res=requests.patch(url=url)
                    st.success('完了')
                # 削除ボタンが押された場合の処理です。
                if submit_button_2:
                    # 項目を削除します。
                    # 関連するデータを取得し、FastAPIサーバーにDELETEリクエストを送信します。
                    deadline:datetime.date=record.get('deadline')
                    todo:str=record.get('todo')
                    priority:int=record.get('priority')
                    genre:str=record.get('genre')
                    completed_flag:bool=record.get('completed_flag')
                    nowdate:datetime.date=record.get('nowdate')
                    url='http://127.0.0.1:8000/router?deadline=%s&todo=%s&priority=%s&genre=%s&completed_flag=%s&nowdate=%s'\
                        %(repr(deadline)[1:-1],repr(todo)[1:-1],repr(priority),repr(genre)[1:-1],repr(completed_flag),repr(nowdate)[1:-1])
                    res=requests.delete(url=url)
                    st.success('削除')
# 完了リストページの処理です。
elif page=='完了リスト':
    st.title('完了リスト')
    # FastAPIサーバーからToDoリストを取得します。
    url='http://127.0.0.1:8000/router'
    res=requests.get(url=url)
    records=res.json()
    # 完了した項目を表示します。
    for record in records:
        if record.get('completed_flag')==True:
            st.subheader('・'+record.get('deadline'))
            st.write(record.get('todo'))

# testページの処理です。
elif page=='テスト':
    st.title('テスト')
    # FastAPIサーバーからToDoリストを取得します。
    url='http://127.0.0.1:8000/test'
    res=requests.get(url=url)
    records=res.json()
    # 完了した項目を表示します。
    st.subheader(records.get('Hello'))