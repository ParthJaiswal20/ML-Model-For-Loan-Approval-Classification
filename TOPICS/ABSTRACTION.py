from abc import ABC, abstractmethod
# ABC IS ABSTRACTION BASE CLASSES

# CREATING A SIMPLE CLASS , BUT PUTTING THE ABC WHICH IS
# ABSTRACTION BASE CLASS IN IT TO MAKE IT ABSTRACT CLASS , like this
class animal(ABC):
    # HERE DEFINING THE FUNCTION HERE , BUT I DONT WANT TO IMPLEMENT IT HERE
    # SO WE USE THE PASS KEYWORD , like this
    @abstractmethod
    def make_sound(self):
        pass
# --------------------------------------------------------------------------------------------------
class LION(animal): # DOING THE INHERITANCE 
    # IMPLEMENTING THE SOUND FUNCTION FROM THE ANIMAL CLASS BY INHERITANCE LIKE THIS
    def make_sound(self):
        print("ROAR")

class CAT(animal):  # DOING THE INHERITANCE 
    # IMPLEMENTING THE SOUND FUNCTION FROM THE ANIMAL CLASS BY INHERITANCE LIKE THIS
    def make_sound(self):
        print("MEOW")
# --------------------------------------------------------------------------------------------------   
# OBJECT CREATION AND CALLING THE MAKE SOUND FUNCTION 
lion = LION()
lion.make_sound()
cat = CAT()
cat.make_sound()