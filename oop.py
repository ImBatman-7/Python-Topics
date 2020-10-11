class Laptop:
    discount_percent = 10
    count_instance = 0
    def __init__(self, brand, ram, price):
        Laptop.count_instance += 1
        self.brand = brand
        self.ram = ram
        self.price = max(price,0) 
        self.full_specs = f'{self.brand} {self.ram} {self.price}'

    @classmethod
    def from_string(cls,string):
        brand,ram,price = string.split(',') 
        return cls(brand,ram,price)

    @classmethod
    def count_instances(cls):
        return f'you have created {cls.count_instance} instances of {cls.__name__} class. '

    @staticmethod
    def hello():
        print('hey there !!')

    def costlier(self):  #instance method
        return self.price>40000

    def applied_discount(self):
        new_price = (self.discount_percent/100)*self.price
        return self.price-new_price
    


l1 = Laptop('acer', '8 gb', 45000)
l2 = Laptop('asus', '4 gb', 26000) 
l2.discount_percent = 90

l3 = Laptop.from_string('MSI gf63,12 gb,69900 ')

print(l3.brand)

print(l2.full_specs)


print(l2.costlier())


print(l2.applied_discount())

print(l2.__dict__)

print(Laptop.count_instances())


Laptop.hello()
# _________________________________________


class Laptops:
    count_instance = 0  # class variable
    def __init__(self, brand, ram, price):
        Laptops.count_instance += 1
        self.brand = brand
        self.ram = ram
        self.price = price 


l1 = Laptops('acer', '8 gb', 45000)
l2 = Laptops('asus', '4 gb', 26000) 

print(Laptops.count_instance)
        

# _________________________________________________


class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = max(price,0) 
        # self.full_specs = f'{self.brand} {self.ram} {self.price}'


    @property
    def full_specs(self):
        return f'{self.brand} {self.ram} {self.price}'

    @property
    def effective_price(self):
        return self.price

    @effective_price.setter
    def effective_price(self,new_price):
        self.price = max(new_price,0)    

l1 = Laptop('acer', '8 gb', 45000)
l2 = Laptop('asus', '4 gb', 26000)   

print(l2.full_specs)  
l2.price = -10000

print(l2.effective_price)

print(l2.full_specs)


# _________________________________________________

#inheritance in oop
class Laptop: #base class / parent class
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = max(price,0)

class Superlaptop(Laptop):
    def __init__(self,brand, ram, price,refresh_rate,display_resolutiion,graphics):


        super().__init__(brand, ram, price)
        self.refresh_rate = refresh_rate
        self.display_resolutiion = display_resolutiion
        self.graphics = graphics



s1 = Superlaptop('acer predator', '16gb', 109809, '240hz', '8k', 'nvidia rtx 4080ti')

print(s1.graphics)
print(s1.price)
print(s1.display_resolutiion)
print(s1.refresh_rate)


# _______________________________________________________


#inheritance in oop
class Laptop: #base class / parent class
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = max(price,0)

class Superlaptop(Laptop):
    def __init__(self,brand, ram, price,refresh_rate,display_resolutiion,graphics):


        super().__init__(brand, ram, price)
        self.refresh_rate = refresh_rate
        self.display_resolutiion = display_resolutiion
        self.graphics = graphics



s1 = Superlaptop('acer predator', '16gb', 109809, '240hz', '8k', 'nvidia rtx 4080ti')

print(s1.graphics)
print(s1.price)
print(s1.display_resolutiion)
print(s1.refresh_rate)
# print(help(Superlaptop))

print(isinstance('acer predator', Laptop))


# _________________________________________________


class Phone: #base class / parent class
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def phone_name(self):
        return f'{self.brand} {self.model}'

    def __add__(self,other): #operator overloading
        return self.price + other.price 

    def __str__ (self):#for normal users
        return f'{self.brand} {self.model} and price is {self.price}'      

    def __repr__(self): #for developers
        return f'Phone({self.brand}, {self.model}, {self.price})'

my_phone = Phone('nokia', '1100', 1000)
my_phone2 = Phone('nokia', '1200', 1900)


print(str(my_phone))    
print(repr(my_phone))   


print(my_phone  + my_phone2)

# _______________________________________________

# exception handling exercise
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "this number can't be divisible by zero."
    except TypeError:
        return "this number can't be divisible by str values."
    except:
        return "unexpected error."    

print(divide(10,2)) 