def calculator(a, b, operation):
    if (operation == "+"):
        return a+b
    elif (operation == "-"):
        return a-b
    elif (operation == "*"):
        return a*b
    elif (operation == "/"):
        return a/b
    else:
        print("invalid choice sir :(")


a = int(input("enter the number 1: "))
b = int(input("enter the number 2: "))
operation = input("enter the operation either + or - or * or /: ")
output = calculator(a, b, operation)
print(output)
