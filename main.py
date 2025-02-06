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
    print(round(a / b),2)