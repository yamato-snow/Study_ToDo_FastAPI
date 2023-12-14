import streamlit as st
import requests
import datetime

page=st.sidebar.selectbox('ページ名',['新規登録','未完了リスト','完了リスト'])

if page=='新規登録':
    st.title('新規登録')
    with st.form(key='新規登録'):
        deadline:datetime.date=st.date_input('期日').strftime('%Y-%m-%d')
        todo:str=st.text_input('Todo',max_chars=100)
        priority:int=st.number_input('優先度',0)
        genre:str=st.text_input('カテゴリ',max_chars=15)
        submit_button=st.form_submit_button(label='登録')

        if submit_button:
            url='http://127.0.0.1:8000/router?deadline=%s&todo=%s&priority=%s&genre=%s'\
                %(repr(deadline)[1:-1],repr(todo)[1:-1],repr(priority),repr(genre)[1:-1])
            res=requests.post(url=url)
            st.success('登録完了')

elif page=='未完了リスト':
    st.title('未完了リスト')
    url='http://127.0.0.1:8000/router'
    res=requests.get(url=url)
    records=res.json()
    i=0
    for record in records:
        i+=1
        if record.get('completed_flag')==False:
            with st.form(key=str(i)):
                st.subheader('・'+record.get('deadline'))
                st.write(record.get('todo'))
                submit_button_1=st.form_submit_button(label='完了')
                submit_button_2=st.form_submit_button(label='削除')
                if submit_button_1:
                    deadline:datetime.date=record.get('deadline')
                    todo:str=record.get('todo')
                    priority:int=record.get('priority')
                    genre:str=record.get('genre')
                    nowdate:datetime.date=record.get('nowdate')
                    url='http://127.0.0.1:8000/router?deadline=%s&todo=%s&priority=%s&genre=%s&nowdate=%s'\
                        %(repr(deadline)[1:-1],repr(todo)[1:-1],repr(priority),repr(genre)[1:-1],repr(nowdate)[1:-1])
                    res=requests.patch(url=url)
                    st.success('完了')

                if submit_button_2:
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

elif page=='完了リスト':
    st.title('完了リスト')
    url='http://127.0.0.1:8000/router'
    res=requests.get(url=url)
    records=res.json()
    for record in records:
        if record.get('completed_flag')==True:
            st.subheader('・'+record.get('deadline'))
            st.write(record.get('todo'))