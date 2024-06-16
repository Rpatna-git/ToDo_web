import streamlit as st
import functions as ft

st.title("My ToDo App ")
st.header("This is my ToDo App list")
st.write("This is very useful for day to day activities")


todo_list=ft.get_todos("todo_list.txt")
def add_todo():
    todo_item=st.session_state['new_todo'] + '\n'
    print(st.session_state)
    print(todo_item)
    todo_list.append(todo_item)
    ft.write_todos(todo_list,"todo_list.txt")

for index,item in enumerate(todo_list):
    checkbox=st.checkbox(item,key=item)
    if checkbox:
        print("delete this item from list")
        todo_list.pop(index)
        ft.write_todos(todo_list,"todo_list.txt")
        del st.session_state[item]
        st.rerun()

st.text_input(label="ToDo item",on_change=add_todo,placeholder="Enter new todo item here",key='new_todo')


print("Hello")
st.session_state
