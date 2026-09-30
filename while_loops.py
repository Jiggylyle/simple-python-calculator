# Execute some code while a condition is true

name = input("Enter your name: ")

while name == "":
    print("You didn't enter a name.")
    name = input("Enter your name: ")

print(f"Hello, {name}!")
