import streamlit as st

st.title("ToDoリストアプリ")

if 'todos' not in st.session_state:
    st.session_state.todos = []

new_todo = st.text_input("新しいToDoを追加")

if st.button("追加"):
    st.session_state.todos.append(new_todo)

st.write("ToDoリスト")
for todo in st.session_state.todos:
    st.write(f" * {todo}")
