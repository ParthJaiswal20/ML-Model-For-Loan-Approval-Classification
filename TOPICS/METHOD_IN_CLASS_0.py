class student:
    # DEFINING A CONSTRUCTOR METHOD TO GIVE NAME TO ALL THE NEW OBEJCT THAT I WILL CREATE + TAKE VALUE IF THEY GIVE
    # CONSTRUCT METHOD BELOW 👇
    def __init__(self, name):
        self.name = name
    # DECLARED A NAME TO STORE THE VAUE THAT IS BEING PASSED TO ME , TO HAVE IT 

# CREATING AN OBJECT OF THE CLASS + PASSING THE VALUE TO STORE
student1 = student("PARTH")
student2 = student("VAIBHAV")

print(student1.name)
print(student2.name)