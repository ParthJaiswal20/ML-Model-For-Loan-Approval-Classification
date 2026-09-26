salary = int(input("enter the salary here:"))

if (salary < 30000):
    print("5% tax ")
elif (salary > 30000 and salary < 70000):
    print("15% tax")
else:
    print("25% tax")
