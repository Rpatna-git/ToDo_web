FILEPATH="todo_list.txt"

def get_todos(FILEPATH):
    with open(FILEPATH,'r') as new_file:
        return new_file.readlines()

def write_todos(todos_list,FILEPATH):
    with open(FILEPATH,'w') as write_items:
        write_items.writelines(todos_list)