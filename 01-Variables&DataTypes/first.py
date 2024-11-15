name = "neps majhi"
age = 31
price = True

# print(type(name))
# print(type(age))
# print(type(price))


# Data types
# Integers, Strings, Float, Boolean, None

# Types of operators
# Arithmetic operators (+, -, *, /, %, **)
# Relational / Comparison operators (==, !=, >, <, >=, <=)
# Assignment operators (=, +=, -=, *=, /=, %=, **=)
# Logical operators (not, and or)

# Arithmetic operators (+, -, *, /, %, **)
a = 5
b = 6

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b) # remainder
# print(a ** b) # a^b


# Relational / Comparison operators (==, !=, >, <, >=, <=)

a = 50
b = 30

# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)


# Assignment operators (=, +=, -=, *=, /=, %=, **=)

num = 10
num += 11
# print("num : ", num)


# Logical operators (not, and or)
a = 50
b = 30

val1 = True
val2 = False

# print(not False)
# print(not(a > b))

# print("AND operators :", val1 and val2 )

# print("OR operators :", val1 or val2 )

# print("OR operators : ", (a == b) and (a > b))


# Type conversion (cnversion, casting)

a = "2" 
b = 4.25

# print(int(a) + b)

# Input in python

# name = input("Enter your name : ")
# print("Welcome ", name)

# val = input("Type some value :")
# print(type(val), val)

# val = int(input("Type some value :"))
# print(type(val), val)


# val = float(input("Type some value :"))
# print(type(val), val)

# name = input("enter your name : ")
# age = input("enter your age :")
# marks = input("enter your marks")

# print("Welcome ", name)
# print("your age = ", age)
# print("your marks = ", marks)


# Practice questions
# Write a program to input two number and print their sum

# firstNum = int(input("input a number you want to sum with :"))
# secNum = int(input("input a number you want to sum with :"))

# print("Your total sum is : ", firstNum + secNum)

# WAP to input side of a square & print its area.

# side = float(input("enter side"))

# print("side of a square = ", side **2)

# WAP to input 2 floating point number & print their average.

# firstPoint = float(input("enter a first point"))
# secPoint = float(input("enter a second point"))

# print("Average of points : ", (firstPoint + secPoint) / 2)

# WAP to input 2 int numbers, a and b.
# Print true if a is greater than or equal to b. if not print false.

a = int(input("enter num a "))
b = int(input("enter num b "))

print(a >= b)