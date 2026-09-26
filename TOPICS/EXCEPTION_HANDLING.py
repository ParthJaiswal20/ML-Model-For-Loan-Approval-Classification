try:
    x = int(input("enter the vlaue: "))
    ans = 10/x

except ZeroDivisionError:
    print("division by zero is not allowed")
except ValueError:
    print("using string in dividing is prohibited")

else:
    print(ans)
    
finally:
    print("THIS WILL BE RUNNED EVERYTIME")
