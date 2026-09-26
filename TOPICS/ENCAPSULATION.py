class bankAccount:
    def __init__(self, name, balance):
        self.name = name  # THIS IS A PUBLIC ATTRIBUTE
       # self._balance = balance # THIS IS A PROTECTED ATTRIBUTE
        self.__balance = balance  # THIS IS A PRIVATE ATTRIBUTE NOW
    
    # DEFINIG A GETTER FUNCTION TO GET THE VALUE OF THE PRIVATE ATTRIBUTE
        def get_balance(self):
            return self.__balance
        
    # DEFINIG A SETTER FUNCTION TO GET UPDATE THE VALUE
    # OF THE PRIVATE ATTRIBUTE
    def set_balance(self,newBalance):
        self.__balance = newBalance

acc_1 = bankAccount("Parth Jaiswal", 20000)

print(acc_1.name, acc_1.__balance)
