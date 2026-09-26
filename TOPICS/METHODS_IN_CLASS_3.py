class laptop:
    storage_type = "SSD"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    # USING THE CLASS DECORATOR TO MAKE THE BELOW METHOD AS THE CLASS METHOD
    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

    def get_info(self):  # INSTANCE METHOD as it contains self as the 1st parameter
        print(
            f"laptop has {self.RAM} RAM  & {self.storage} {self.storage_type}")

    @staticmethod
    def cal_final_price(price, discount):
        finalPrice = price - (discount * price / 100)
        print("finalPrice =", finalPrice)


l1 = laptop("16gb", "512gb")
l2 = laptop("16gb", "512gb")

# CALLING THE CLASS METHOD USING THE CLASS NAME AND THE DOT . OPERATOR
laptop.get_storage_type()

# AND CAN ALSO CALL IT USING THE OBJECT NAME --> BCZ WE LEARNT BEFORE THAT OBJECT CANNOT ONLY ACCESS ITS
#  OWN METHODS BUT CAN ALSO ACCESS THE CLASS METHODS , BCZ WHATEVER IS IN THE CLASS IS FOR THE OBJECT ALSO .
l1.get_storage_type()

# CALLING THE STATIC METHOD  + PASSING THE VALUE TO IT TO GET CALCULATE
l1.cal_final_price(40_000, 10)