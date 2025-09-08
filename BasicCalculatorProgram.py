def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Impossible, division by zero"
    else:
        return a / b
    

operations = {"+": add, "-": subtract, "*": multiply, "/": divide }

first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))
operation = input("Enter the operation (+, -, *, /) : ")

result = operations[operation](first_number, second_number)

print("The result of ", first_number, operation, second_number, " is ", result)


"""
a = int(input("First number : "))
b = int(input("Second number : "))
operation = input("Mathematique opération (+, -, * or /) : ")

if operation == '+':
    print(a, " + ", b, " = ", a+b)
    
if operation == '-':
    print(a, " - ", b, " = ", a-b)
    
if operation == '*':
    print(a, " * ", b, " = ", a*b)
    
if operation == '/':
    print(a, " / ", b, " = ", a/b)
"""