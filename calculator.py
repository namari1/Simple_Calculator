running = True
print("Welcome to the simple calculator! Enter q or quit to stop.")
while running:
    x = input("Enter first number: ").lower()
    if x == "q" or x == "quit":
        running = False
        print("Thanks for running this program! If you need to reuse the calculator, just run the program again!")
        break

    y = input("Enter second number: ").lower()
    if y == "q" or y == "quit":
        running = False
        print("Thanks for running this program! If you need to reuse the calculator, just run the program again!")
        break
    operation = input("Add, subtract, multiply, or divide? ").lower()

    if operation == "q" or operation == "quit":
        running = False
        print("Thanks for running this program! If you need to reuse the calculator, just run the program again!")
        break

    result = None

    if not x.replace(".", "").isnumeric() or not y.replace(".", "").isnumeric():
        print("Error! You did not enter a number or quit the program, please try again")
        x = input("Enter first number: ")
        y = input("Enter second number: ")
        operation = input("Add, subtract, multiply, or divide? ").lower()

    x = float(x)
    y = float(y)

    if operation == "add":
        result = x + y
    elif operation == "subtract":
        result = x - y
    elif operation == "multiply":
        result = x * y
    elif operation == "divide":
        result = x/y

    print(result)

