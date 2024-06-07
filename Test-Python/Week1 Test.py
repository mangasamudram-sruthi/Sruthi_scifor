#!/usr/bin/env python
# coding: utf-8

# # 1)Encapsulation
# It is a OOPs concept that protects data integrity and promote modularity.
# 

# In[9]:


class Smartphone:
    def __init__(self, brand, os):
        self.brand = brand
        self.os = os

iphone = Smartphone("Apple", "iOS 17")
realme=Smartphone("Realme P1", "Android 14")
iphone.os = "Android"
print(realme.brand)
print(iphone.os)



# # 2)Polymorphism
# Polymorphism means many forms, i.e same functions can be used for differnt types. Used in code readability and efficiency. 

# In[43]:


class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

def calculate_area(shape):
    print("Area:", shape.area())

circle = Circle(3)
 
calculate_area(circle)     


# # 3)Single Level Inheritance
# It means child class inherits from single parent class.

# In[27]:


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_info(self):
        print("Brand:", self.brand)

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_info(self):
        super().display_info()
        print("Model:", self.model)

car = Car("Toyota", "Corolla")
car.display_info()


# # 4)Multiple Inheritance
# 
# Here inheritance goes on in multiple levels.

# In[33]:


class Engine:
    def start_engine(self):
        return "Engine started"
class Wheels:
    def start_moving(self):
        return "Wheels are moving"

class Car(Engine, Wheels):
    def drive(self):
        return f"{self.start_engine()} and {self.start_moving()}"
car = Car()
print(car.start_engine())  
print(car.start_moving())  
print(car.drive())  


# # 5)Multi-Level Inheritance 
# 
# A child class inherits from another child class and this intermidiate child class inherits from parent class.

# In[38]:


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_brand(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_model(self):
        print(f"Model: {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def display_battery_capacity(self):
        print(f"Battery Capacity: {self.battery_capacity} kWh")

tesla = ElectricCar("Tesla", "Model S", 100)

tesla.display_brand()            
tesla.display_model()            
tesla.display_battery_capacity()  


# # 6)Conditional Statements
# Executes only specific blocks of codes based on the true condition
# 1)if-else
# 2)nested if
# 3)match case

# In[24]:


num1 = int(input('Enter first number  : '))
num2 = int(input('Enter second number : '))

if num1 > num2 :
    print("num1 is larger than num2")
else:
    print("num2 is larger than num1")


# # 7) Decision making statements
# same as conditional Statements
# 

# In[42]:


y = 13

if y > 0:
    print("y is positive")
elif y == 0:
    print("y is zero")
else:
    print("y is negative")


# # 8)Factorial in python

# In[40]:


num = int(input("Enter a non-negative integer: "))
fact = 1
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, num + 1):
        fact *= i

    print(f"The factorial of {num} is {fact}")


# # 9)Functions
# Blocks of reusable codes are called as function
# 

# In[39]:


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


num = 7
result = even_or_odd(num)
print(f"{num} is {result}")


# # 10)Pillars in OOps 
# There are 3 pillars in python :
#     1)Encapsulation
#     2)polymorphism
#     3)Inheritance
#     
