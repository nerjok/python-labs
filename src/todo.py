# todos = []

def get_todos():
    with open("src/files/todos.txt", "r") as file:
        todos = file.readlines()
    return todos

while True:
    userAction = input("Type add, show, edit or exit: ")
    userAction = userAction.strip()
    if userAction.startswith("add"):
        # todo = input("Enter todo: ") +"\n"
        todo = userAction[4:]

        # file = open("src/files/todos.txt", "r")
        # todos = file.readlines()
        # file.close()

        # with open("src/files/todos.txt", "r") as file:
        #     todos = file.readlines()
        todos = get_todos()

        todos.append(todo + "\n")

        # file = open("src/files/todos.txt", "w")
        # file.writelines(todos)
        # file.close()

        with open("src/files/todos.txt", "w") as file:
            file.writelines(todos)
    elif "show" in userAction:
        with open("src/files/todos.txt", "r") as file:
            todos = file.readlines()

        newTodos = [itm.strip("\n") for itm in todos]
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index+1} - {item}")
    elif userAction.startswith("edit"):
        # number = input("Number of the todo to edit:")
        try:
            number = userAction[5:]
            number = int(number) - 1

            todos = get_todos()

            existingTodo = todos[number]
            newTodo = input("enter new todo: ")
            todos[number] = newTodo + "\n"
            # print("edit", existingTodo, todos[number])
            with open("src/files/todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Your commands is not valid")
            continue
    elif "complete" in userAction:
        try:
            # number = input("Number of todo to complete")
            number = userAction[9:]
            number = int(number) - 1
            todos = get_todos()
            todos.pop(number)
            with open("src/files/todos.txt", "w") as file:
                file.writelines(todos)
            print("completed")
        except ValueError:
            print("Your commands is not valid")
            continue
    elif  "exit" in userAction:
        break
    else:
        print("Command is not valid")

print("bye")
var1 = "sad"
row = f"{var1}asdas"

print(len(todos))