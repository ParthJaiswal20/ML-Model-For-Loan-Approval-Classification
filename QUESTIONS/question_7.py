string = input("enter the string to check , here : ")

rev = ''
for char in string:
# below line the most important line , bcz when adding its adding like this in rev
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# BCZ REV IS IN THE RIGHT AND CHAR IS IN THE LEFT SIDE
    rev = char + rev
    # THE ABOVE LINE IS BEING USED TO ADD THE WORDS IN BACKWARD DIRECTION 
# SUPPOSE THE INDEX OF THE WROD IN STIRNG IS 0 1 2 3 4 BUT IN REV THEY ARE 4 3 2 1 0
# BCA OF DOING OF --> char + rev

if(rev == string):
    print("its palindrome")
else:
    print("not palindrome")