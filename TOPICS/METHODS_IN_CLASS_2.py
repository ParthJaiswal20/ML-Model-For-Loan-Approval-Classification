class student:
    def __init__(self, name, cgpa): # THIS IS PARAMATERIZED CONSTRUCTOR
        # DECLARED THE NAME VARIABLE & THE CGPA VARIABLE SAME WAY
        self.name = name
        self.cgpa = cgpa
# ---------------------------------------------------------------------------------------
   
    # this function is also created within the class and is used to return the cgpa value of the
    # particular object that is calling it

    def get_cgpa(self):
        # AS WE ALEADY KNOW WHEN THIS FUNCTION WILL BE CALLED BY AN OBJECT ,
        # 1 SUPPOSE THEN THIS SELF == 1 BECOMES
        # AND NOW I WANT THE CGPA OF THAT OBJECT & AS WE ALREADY KNOW THAT IF
        # I WANT TO ACCESS A PARTICULAR VALUE OF THAT OBJECT THEN WE
        # USE THE . DOT OPERATOR , like this
        return self.cgpa
# ---------------------------------------------------------------------------------------

stu_1 = student("PARTH", 9.2)
stu_2 = student("PARTHIV", 9.9)
# ---------------------------------------------------------------------------------------

# PRINTING THE NAME FOR EACH OF THE OBJECT + THE CGPA FOR EACH OF THEM
print(stu_1.name, " ", stu_1.cgpa)
print(stu_2.name, " ", stu_2.cgpa)
# ---------------------------------------------------------------------------------------

# CALLING THE GET_CGPA FUNCTION TO GET THE CGPA OF A PARTICULAR OBEJCT ONE BY ONE
print("CALLED THE GET_CGPA FUNCTION WHERE SELF BECOMES THAT OBEJCT WHICH IS CALLING IT AT THAT PARTICULAR TIME")
print(stu_1.get_cgpa())
