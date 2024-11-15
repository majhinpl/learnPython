# String is data type that stores a sequesce of characters.

str1 = "This is a string"
str2 = 'This is a string'
str3 = """This is a string"""

strNewline =  "This is a string. \n we are writing in python"

# print(strNewline)
# print(len(strNewline))

# indexing
idx = "This is indexing"
# print(idx[3])

# Slicing
# str[starting_idx : ending_idx] ending idx is not incuded

str = "Slicing"
# print(str[1:4])

# Negative index
# print(str[-6:-1])

# StringFunctions
str = "i am studying python from ApnaCollege"
# print(str.endswith("app"))
# print(str.capitalize())
# print(str.replace("o", "a"))
# print(str.find("o"))
# print(str.count("o"))

# QS Practice
# WAP to input user's first name & print its length.

# firstName = input("enter your first name :")
# print("Length of your first name is : ", len(firstName))

# WAP to find the occurrence of "$" in a string
# print(firstName.count("s"))

# Conditional statements
# light = "red"

# if(light == "red") :
#     print("stop")
# elif(light == "green"):
#     print("go")
# elif(light == "yello"):
#     print("look")
# else:
#     print("light is broken")

# print("end of code")

# marks = int(input("enter student marks : "))

# if(marks >= 90):
#     grade = "A"
# elif(marks >=80 and marks <90):
#     grade = "B"
# elif(marks >= 70 and marks <80):
#     grade = "C"
# else:
#     grade = "D"

# print("grade of the student =>", grade)

# Nesting

# QS practice

# WAP to check if a number entered by the user is odd or even.

# inputNum = int(input("Your number"))

# if(inputNum % 2 == 0):
#     print("number is even")
# else: 
#     print("number is odd")

# WAP to find the greatest of 3 number by the user.

# a = int(input("Your first number"))
# b = int(input("Your second number"))
# c = int(input("Your third number"))

# if(a >= b and a >= c):
#     print("first number is largest", a)
# elif(b >= c):
#     print("second number is largest", b)
# else:
#     print("third number is largest", c)


# WAP to check if a number is a multiple of 7 or not.

yourNum = int(input("Your number"))

if(yourNum % 7 == 0):
    print("your number is a multiple of 7")
else:
    print("your number isn't a multiple of 7")