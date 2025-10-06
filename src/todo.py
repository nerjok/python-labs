# todos = []
while True:
    userAction = input("Type add, show, edit or exit: ")
    userAction = userAction.strip()
    match userAction:
        case "add":
            todo = input("Enter todo: ") +"\n"

            # file = open("src/files/todos.txt", "r")
            # todos = file.readlines()
            # file.close()

            with open("src/files/todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            # file = open("src/files/todos.txt", "w")
            # file.writelines(todos)
            # file.close()

            with open("src/files/todos.txt", "w") as file:
                file.writelines(todos)
        case "show":
            with open("src/files/todos.txt", "r") as file:
                todos = file.readlines()
    
            newTodos = [itm.strip("\n") for itm in todos]
            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index+1} - {item}")
        case "exit":
            break
        case "edit":
            number = input("Number of the todo to edit:")
            number = int(number) - 1

            with open("src/files/todos.txt", "r") as file:
                todos = file.readlines()

            existingTodo = todos[number]
            newTodo = input("enter new todo: ")
            todos[number] = newTodo + "\n"
            # print("edit", existingTodo, todos[number])
            with open("src/files/todos.txt", "w") as file:
                file.writelines(todos)
        case "complete":
            number = input("Number of todo to complete")
            number = int(number)
            with open("src/files/todos.txt", "r") as file:
                todos = file.readlines()
            todos.pop(number)
            with open("src/files/todos.txt", "w") as file:
                file.writelines(todos)
            print("completed")

print("bye")
var1 = "sad"
row = f"{var1}asdas"

print(len(todos))