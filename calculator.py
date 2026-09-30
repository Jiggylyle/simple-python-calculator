while True:
    print("Select a operation")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Quit")

    choice = input("Enter your choice: ")

    if choice == '5':
        break
    elif choice in ('1', '2', '3', '4',):
        num_1 = float(input("Enter a number: "))
    num_2 = float(input("Enter another number: "))

    if choice == '1':
        result = num_1 + num_2
        print(f"ANSWER: {result}")
    elif choice == '2':
        result = num_1 - num_2
        print(f"ANSWER: {result}")
    elif choice == '3':
        result = num_1 * num_2
        print(f"ANSWER: {result}")
    elif choice == '4':
        result = num_1 / num_2
        print(f"ANSWER: {result}")
    elif choice < '5':
        print(f"{choice} is INVALID")
    else:
        break
