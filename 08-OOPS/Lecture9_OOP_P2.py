# Inheritance
# When one class(child/derived) drives the properties & methods of another class(parent/base)

class Car:
    @staticmethod
    def start():
        print("car started ..")


    @staticmethod
    def stop():
        print("car stopped. ..")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name
    
car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")
print(car1.start())

# inheritance
"""
# Types
- Single inheritance
- multi-level inheritance
- Multiple inheritance

"""
# - multi-level inheritance
class Car:
    @staticmethod
    def start():
        print("car started ..")

    @staticmethod
    def stop():
        print("car stopped. ..")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand
    
class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()


# - Multiple inheritance
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

# Super method
# super() method is used to access methods of the parent class.

class Car:
    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("prius", "electric")
print(car1.type)


# class method
# A class method is bound to the cass & receives the class as an implicit first argument.

# Note - static method can't access or modify class state & generally for utility.

class Student:
    @staticmethod
    def college(cls):
        pass

class Person:
    name = "anonymous"

    # def changeName(obj, name):
    #     self.__class__.name = "nephx"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("nephx")
print(p1.name)
print(Person.name)


# Property
# We use @property decorator on any method in the class to use the method as a property.

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    @property
    def calc_percentage(self):
         return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(96, 97, 99)
print(stu1.calc_percentage)

stu1.phy = 86
print(stu1.calc_percentage)


# Polymorphism : Operator Overloading
# When the same operator is allowed to have different meaning accourding to the context.

print(1 + 2)
print([1,2,3] + [4,5,6]) # merge
print(type([1,2,3]))

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def show_num(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self, num2):
        new_real = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(new_real, newImg)

num1 = Complex(1, 3)
num1.show_num()

num2 = Complex(4, 6)
num1.show_num()

num3 = num1 + num2
num3.show_num()

# Operators & Dunder functions
# a+b # addition  a. __add__(b)

# Practice QS
"""
# Qs. Define a Circle class to create a circle with radius r using the constructor.

Define an Area() method of the class which calculates the area of the circle.

Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

"""

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    

c1 = Circle(1.2)
print(c1.area())
print(c1.perimeter())


"""
# QS. Define a Employeeclass with attributes role, department & salary. This class also has a showDetails() methd.

"""

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        print("role =", self.role)
        print("role =", self.dept)
        print("role =", self.salary)


e1 = Employee("planner", "planning", "1254")
e1.show_details()

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

eng1 = Engineer("nephx", 40)
eng1.show_details()


"""
# QS. Creat a class called Order which stores item & its price.
Use Dunder function __gt__() to convey that:
order1>order2 if price of order1>price of order2

"""
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price

odr1 = Order("chips", 20)
odr2 = Order("tea", 15)

print(odr1 > odr2)