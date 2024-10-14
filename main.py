#Number 1
num1 = int(input("Enter First Number: "))

#Number 2
num2 = int(input("Enter Second Number: "))

#Operation
op = input("[ + - * / ]: ")

#Add
if op == "+":
    print(f"The Answer is: {num1 + num2}")

#Subtract
if op == "-":
    print(f"The Answer is: {num1 - num2}")

#Multiply
if op == "*":
    print(f"The Answer is: {num1 * num2}")

#Divide
if op == "/":
    print(f"The Answer is: {num1 / num2}")
