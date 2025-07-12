# OOPS : Object-Oriented Programming System
# OOP in python
# To map with real world scenarios, we started using objects in code.
# This is called object orinted programming

# Class & Object in python
# class is a blueprint for creating objects.
class Student:
    name = "nephx"

# creating object (instance)
s1 = Student()
# print(s1.name)

class Stock:
    SRIN = "NP1243521"
    symbol = "ST123"
    share = 123456245

stock1 = Stock()
# print("Stock class :\n", stock1.share)

# __init__ function
# Constructor 
# All classes have a function called _init_(), which is always executed when the object is being initiated.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database..")

st1 = Student("nephx", 97)
# print(st1.name, st1.marks)

s2 = Student("neps", 0)
# print(s2.name)


class Student:


    # Default Constructors
    def __init__(self):
        pass

    # parameterized constructrs
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database..")

st1 = Student("nephx", 97)
# print(st1.name, st1.marks)

s2 = Student("neps", 0)
# print(s2.name)

# Class & Instance Attributes
# Class.attr
# obj.attr

class Student:

    college_name = "ABC college"
    name = "annonymous"    # class attr

    # parameterized constructrs
    def __init__(self, name, marks):
        self.name = name # obj attr > class attr
        self.marks = marks
        print("adding new student in database..")


s1 = Student("nephx", 90)
# print("printing S1 :\n", s1.name)

# Methods
# methods are function that belong to objects.
# class is a collection of two property methods and data attributes.

class Student:
    college_name = "ABC College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def welcome(self):
        print("Welcome student", self.name)

    def get_marks(self):
        return self.marks

    
s1 = Student("nephx", 98)
s1.welcome()
print(s1.get_marks())


# Let's Practice

# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "Your avg score is : ", sum/3)

s1 = Student("nephx", [99,96,86])
print(s1.name)
print(s1.get_avg())

# Static Methods
# Methods tht don't use the self parameter (work at class level)

class Student:
    @staticmethod #decorator
    def college():
        print("ABC College")


# Important
# Abstraction : Hiding the implemention detais of a class and only showing the essential features to the user.


# Encapsulation : Wrapping data and function into a single unit (object)

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = \n", self.get_bal())
    
    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = \n", self.get_bal())
    
    # total method
    def get_bal(self):
        return self.balance
    
acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(5000)
