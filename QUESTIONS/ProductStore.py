class product:
    count = 0  # CLASS VARIABLE

    def __init__(self, name, price):  # THIS IS CONSTRUCTOR METHOD
        # THIS IS CALLED EVERYTIME WHEN AN OBJECT IS CREATED AND THIS WILL
        # HELP US TO KNOW THE NUMBER OF OBEJCT IS CREATED WHEN IT WILL BE CALLED
        self.name = name
        self.price = price
        product.count += 1  # BCZ OF THE CONSTRUCTOR DECLARING THIS HERE

    def get_info(self):
        print(f"price of {self.name} is Rs.{self.price}")

    # AS THE COUNT IS CLASS VARIABLE THATS WHY CREATING A CLASS METHOD TO
    # GET THE ACCESS OF THE CLASS VARIABLE
    @classmethod
    def getCount(cls):
        print(f"total number of products in the store is = {cls.count}")


prod_1 = product("phone", 10000)
prod_2 = product("laptop", 60000)

prod_1.get_info()

product.getCount()  # AS THIS IS A CLASS METHOD THATS WHY I AM ACCESING IT
# USING THE CLASS NAME
