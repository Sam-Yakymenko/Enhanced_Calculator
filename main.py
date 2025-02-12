a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
oper = input("Enter the operator: ")

if oper == '+':
    print(round(a + b, 2))
elif oper == '-':
    print(round(a - b),2)
elif oper == '*':
    print(round(a * b),2)
elif oper == '/':
    if b != 0:
        print(round(a / b, 2))
    else:
        print("Error: Division by zero is not allowed.")