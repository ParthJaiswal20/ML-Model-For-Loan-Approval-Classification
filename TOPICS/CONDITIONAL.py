color = "red"

if color == "yellow":
    print("yay found out yellow")
    # above is the ONE condition been checked
    # below is the SECOND condition been checked
elif color == "blue":
    print("yay found out blue")
    # below is the THIRD condition been checked
elif color == "red":
    print("yay found out red")
    # below is the base condition been executed if no above condition is satisfied
else:
    print("not founded any color")