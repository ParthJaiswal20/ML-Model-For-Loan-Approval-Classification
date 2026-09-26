list_a = [1, 5, 6]

list_b = [4, 2, 3]

# CREATION OF A NEW LIST 
sorted_list = []

for int in list_a:
    sorted_list.append(int)

for int in list_b:
    sorted_list.append(int)

# INSERTED BOTH THE LIST VALUES IN THE NEW LIST CREATED  
print("this is before the sorting being done in the list: ")
print(sorted_list)

# NOW SORTING IT 
sorted_list.sort()
print("this is after when the list is sorted completely: ")
print(sorted_list)