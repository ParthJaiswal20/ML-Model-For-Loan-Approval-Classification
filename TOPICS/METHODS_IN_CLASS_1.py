class student:
    def __init__(self):
        # HERE SELF MEANS THAT IT IS STORING THE CURRENT INSTANCE OF THE CLASS , BASCIALLY
        # IT MEANS THAT IT IS STORING THE REFERNCE TO THE CURRENT OBJECT
        print("constructor was called bcz the new object was created and will occur for one time")
        print("for each of the creation of the new object\n")


#  CREATION OF A NEW OBJECT + DEMO ON HOW THE CONSTRUCTOR IS CALLED FOR EACH TIME WHEN A NEW
# OBJECT IS CREATED EACH TIME
print("OBJECT_1CONSTRUCTOR WAS CALLED")
obj_1 = student()

print("OBJECT_2 CONSTRUCTOR WAS CALLED")
obj_2 = student()
