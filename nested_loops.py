# Nested loop is a loop within a loop. The inner loop will be executed one time for each iteration of the outer loop.

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")


for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()  # This will print a new line after each iteration of the outer loop
