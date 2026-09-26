words = ["apple", "banana", "kiwi", "cherry", "mango"]

# CREATED A NULL DICT TO STORE THE VALUE ONE BY ONE
dict = {}
# RUN THE LOOP TO ACCESS EACH ELEMENT OF THE WORD
for var in words:
    # FOUNDED THE SIZE
    size = len(var)
    # USED NEW ITEM LOGIC OF ADDING INSIDE THE DICTIONARY
    new_item = {var: size}
    # ADDING THE NEW VALUE IN THE DICTIONARY CREATED
    dict.update(new_item)

print(dict)