class item:
    def __init__(self,name, price , quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

item1 = item('phone',100,5)
print(item1.name )