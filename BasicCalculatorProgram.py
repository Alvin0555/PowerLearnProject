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