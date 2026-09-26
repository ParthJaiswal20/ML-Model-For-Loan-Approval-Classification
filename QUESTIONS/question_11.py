string = input("enter the string with spaces: ")

count = 0
for var in string:
    if(var == " "):
        count = count+1
        
print(count)