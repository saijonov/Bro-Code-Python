num1 = int(input("enter the first number: "))
op = input("enter the operator (+ - * /): ")
num2 = int(input("enter the first number: "))

if op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
elif op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
else:
    print("Invalid")