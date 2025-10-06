todos = []
while True:
    userAction = input("Type add, show, edit or exit: ")
    userAction = userAction.strip()
    match userAction:
        case "add":
            todo = input("Enter todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                print(f"{index+1} - {item}")
        case "exit":
            break
        case "edit":
            number = input("Number of the todo to edit:")
            number = int(number) - 1

            existingTodo = todos[number]
            newTodo = input("enter new todo: ")
            todos[number] = newTodo
            print("edit", existingTodo, todos[number])
        case "complete":
            number = input("Number of todo to complete")
            number = int(number)
            todos.pop(number)
            print("completed")

print("bye")
var1 = "sad"
row = f"{var1}asdas"

print(len(todos))