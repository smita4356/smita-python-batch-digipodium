#class name should be in capital
#example of constructor
class IceCream:
    
    def __init__(self,flavour,price,brand,type):   #init takes double __
        self.flavour=flavour
        self.price=price
        self.brand=brand
        self.type=type
        print('created')


#object


ice1=IceCream('choco',30,'amul','bar')
ice2=IceCream('vanilla',25,'kwality walls','cone')
print(ice1.brand,ice1.flavour)
print(ice2.brand,ice2.flavour)