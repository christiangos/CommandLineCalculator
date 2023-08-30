x1 = input("Enter your first number: ")
operation = input ("Enter the operation you want to perform (+ , - , * , /)")
x2 = input("Enter your second number: ")


x1F = float(x1)
x2F = float(x2)

if operation == "/":
    result = x1F / x2F
    print(x1 + operation + x2 + "=" + str(result))

if operation == "*":
    result = x1F * x2F
    print(x1 + operation + x2 + "=" + str(result))

if operation == "+":
    result = x1F + x2F
    print(x1 + operation + x2 + "=" + str(result))

if operation == "-":
    result = x1F - x2F
    print(x1 + operation + x2 + "=" + str(result))