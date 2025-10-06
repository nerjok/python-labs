def greet(name: str) -> str:
    return f"Hello, {name}!"

promt = "Enter somthing: "
userText = input(promt)
print(userText)
if __name__ == "__main__":
    print(greet("World"))

list = ["abs", "two"]

text = input(promt)
leng = len(text)
print(leng)