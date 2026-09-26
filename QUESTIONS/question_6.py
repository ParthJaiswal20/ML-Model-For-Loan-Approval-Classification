info = [
    ("PARTH", 'ENGLISH'),
    ("PARTH", "HINDI"),
    ("URJIT", "MATHS"),
    ("URJIT", "SOCIAL"),
    ("VAIBHAV", "GK"),
    ("VAIBHAV", "SCIENCE"),
]
# 1. now for unique values of the courses , i will push it in the set
# creating a set first , like this
unique_collection = set()

# adding the values in the set
for val in info:
    unique_collection.add(val[1])

# 2. listing students in the course english
for val in info:
    if (val[1] == "ENGLISH"):
        print(val[0])

# 3. creating a dictionary (student,set of courses)
dict = {}

for name,course in info:
    # checking if the name exist in the dictionary or not
    if (dict.get(name) == None):
        # if getting the none means key (name) doesnot exist in the
        # dictionary and u have to make the new key:value pair here in
        # dictionary

        # ceating a new key:value pair if key (name) is not present, like
        # this
        dict.update({name: set()})
        dict[name].add(course)
        # above accessing the name in the dictionary and
        # adding the --> course in it
    else:
        # if the key exist then directly access that particular key and
        # add the value in it
        dict[name].add(course)
print(dict)