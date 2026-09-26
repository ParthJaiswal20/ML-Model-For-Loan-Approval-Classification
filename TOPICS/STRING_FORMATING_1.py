# THIS IS DONE USING THE FORMAT FUNCTION OF THE PYTHON
a = 10
b = 2
sum = a+b

# but when using the format and giving it a value then the value will go to that place only
# where the {} this is present and no where else
print("the sum is {}".format(sum))

# another way like this
print("{} now it will come here".format(sum))

# default way
print("the sum of {} & {} is {}".format(a, b, sum))

# index based formatting like this .
# in this the value that is written at any postn in the format i can decide
# where it will come BEFORE IT WAS WORKIKING DEFAULT jo aya usse pahale {} vala
# mill gaya but now i can change it , like thisi
print("the sum of {1} & {0} is {2}".format(a, b, sum))

# value based formating , is done like this 
print("the vlaue of new chnaged values of variables are {a} & {b}".format(a=1,b=2))