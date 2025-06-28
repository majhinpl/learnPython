name = "NEPHX"
age = 31
price = True

# print(f"i am: {name}")
# print(type(age))
# print(type(price))

#  Rules for Identifiers
''' 
    1. Identifiers can be combimation of uppercase and lowercase letters, digits or an underscore(_).
    so myVariable, variable_1, variable_for_print all are valid python identifiers.

    2.  An Identifier can not start with digit. So while veriable1 is valid, 1variable is not valid.

    3. we can't use special symbols like !,#,$,%,@.

    4. Identifier can be of any length.

 '''



# Data types
# Integers, Strings, Float, Boolean, None

# boolean data type
age = 32
old = False
a = None

'''
print(age, old, a)
print(type(age))
print(type(old))
print(type(a))

'''
# Keywords
# keywords are reserved word in python.

# Types of Tokens
# Punctuators
# Punctuators are symbol to organize sentence structure in programming.

"""
(), {}, @, [], #, etc.
-=, +=, /=, *=, //=, == etc.

"""

# Expression Execution
'''
String and numeric values can operate togather with *
'''
A,B = 2,3
Txt = "@"
# print(2*Txt*3)
result = "@@@@@@"

'''
String and string can operate with +
# concatenation
'''
A,B = "2",3
Txt = "@"
# print((A+Txt)*B)
# result = "2@2@2@"

'''
Numeric values can operate with all arithmetic operators.
# Arithmetic operators (+, -, *, /, %, **)
'''
A,B=2,3
C=4
# print(A+B*C)

'''
Arithmetic expression with Integer and float will result in float.

'''
A,B=10,5.0
C=A*B
# print(C)

'''
Result of division operator with two integer will be float.

'''
A,B=1,2
C=A/B
# print(C)

'''
Integer division with float and integer will give int display in a float.

'''
A,B=1.5,3
C=A//B
# print(C, A/B)

'''
floor gives closest integer, which is lesser than or equal to the float value.
'''
A,B = 12, 5
C=A//B
# print(C)

A,B = -12, 5
C=A//B
# print(C)

A,B = 12, -5
C=A//B
# print(C)

'''
Remainder is negative when denominator is nagative.
'''

A,B = -5, 2
C=A%B
# print(C)

A,B = 5, 2
C=A%B
# print(C)

A,B = 5, -2
C=A%B
# print(C)

# Input in python
'''
input() statement is used to accept values (using keyboard) from user. 
'''
# string input

"""
name = input("Your name is :")

age = int(input("Your age is :"))

price = float(input("Your have float int :"))
# print(f"My name is {name}, and i'm {age} years old. my price is {price}")

"""


# Conditional Statement
"""
if-elif-else (SYNTAX)

if(condition):
    Statement1
elif(condition):
    Statement2
    else:
StatementN

"""

"""
# traffic lights.
light = input("What is the color of traffic lights: ")
if (light == "red"):
    print("stop")
elif (light == "yellow"):
    print("look and wait")
elif (light == "green"):
    print("Go")

else :
    print("The lights is broken")

"""

"""

A = int(input("A : "))
G = input("M/F : ")

if ((A == 1 or A == 2) and G == "M"):
    print("fee is 100")

elif (A == 3 or A == 4  or G == "F"):
    print("fee is 200")

elif (A == 5 and G == "M"):
    print("fee is 300")

else:
    print("no fee")

"""

# Single Line if / Ternary operator

"""
<var> = <val1> if <condition> else <val2>
"""

"""
food = input("food :")
eat = "Yes" if food == "cake" else "no"
 print(eat)

"""

# Clever if/Ternary Operator
# <var> = (false_val, true_val) [<condition>]

"""
age = int(input("age : "))
vote = ("yes", "no") [age <= 18]

sal = float(input("salary : "))
tax = sal * (0.1, 0.2) [sal>= 50000]
print(f"Your tax is {tax}")

"""

# Types of operators
'''
An operator is a symbol that performs a certain operation between operands
    - Arithmetic operators (+, -, *, /, %, **)
    - Relational / Comparison operators (==, !=, >, <, >=, <=)
    - Assignment operators (=, +=, -=, *=, /=, %=, **=)
    - Logical operators (not, and or)

'''

# Arithmetic operators (+, -, *, /, %, **)
a = 5
b = 6

"""
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # remainder
print(a ** b) # a^b

"""


# Relational / Comparison operators (==, !=, >, <, >=, <=)

a = 50
b = 30

"""
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

"""

# Assignment operators (=, +=, -=, *=, /=, %=, **=)

"""
num = 10
num += 11
num -= 11
num *= 11
num /= 11
num %= 11

print("num : ", num)

"""


# Logical operators (not, and or)
a = 50
b = 30

# print(not False)
# print(not(a > b))

# and
val1 = True
val2 = True

# print("AND operators :", val1 and val2 )

# print("OR operators :", val1 or val2 )

# print("OR operators : ", (a == b) and (a > b))


# Type conversion (cnversion, casting)

a = "2" 
b = 4.25

# print(int(a) + b)

# Input in python

"""
name = input("Enter your name : ")
print("Welcome ", name)

val = input("Type some value :")
print(type(val), val)

val = int(input("Type some value :"))
print(type(val), val)


val = float(input("Type some value :"))
print(type(val), val)

"""

"""
name = input("enter your name : ")
age = input("enter your age :")
marks = input("enter your marks")

print("Welcome ", name)
print("your age = ", age)
print("your marks = ", marks)

"""


# Practice questions

"""
# Write a program to input two number and print their sum

firstNum = int(input("input a number you want to sum with :"))
secNum = int(input("input a number you want to sum with :"))

print("Your total sum is : ", firstNum + secNum)

"""


"""
# WAP to input side of a square & print its area.

side = float(input("enter a dimantions of square side"))

print("Areas of side square = ", side **2)

"""


"""
# WAP to input 2 floating point number & print their average.

firstPoint = float(input("enter a first point"))
secPoint = float(input("enter a second point"))

print("Average of points : ", (firstPoint + secPoint) / 2)

"""


# WAP to input 2 int numbers, a and b. Print true if A is greater than or equal to B. if not print false.

a = int(input("enter num a "))
b = int(input("enter num b "))

if (a >= b):
    print("True")

else: 
    print("False")

