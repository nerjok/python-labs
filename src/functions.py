FILEPATH="src/files/todos.txt"
def get_todos(filepath=FILEPATH):
    """"Something from file returned as list"""
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(todos, filepath=FILEPATH):
    """Write something to file"""
    with open(filepath, "w") as file:
        file.writelines(todos)