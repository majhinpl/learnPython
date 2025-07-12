# Functions in Python
# Block of statement that perform a specific task.
"""
# function defination 
def calc_sum(a, b): #parameters
    sum = a + b
    print(sum)
    return

calc_sum(1,6) #Arguments

def calc_sum(a, b):
    return a + b

sum = calc_sum(1,6)
print(sum)


def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()
print_hello()

output = print_hello()
print(output) # none - if function not returns output will be none.



# agerage of 3 numbers

def avg(a,b,c):
   average =  (a + b + c) / 3
   print(average)
   return
    

avg(98,87,93)

"""

"""

# types of function
# Built-in Functions,  User defined Functions

# print("nephx","altitute") #sep = " "
print("nephx", end=" ")
print("altitute") #end = "\n"



# Default argument
def cal_prod(a, b=2): #default values starts from last.
    print(a *b)
    return a * b

cal_prod()

"""

# Practice
# WAP to print the length of a list. (list is the parameter)
"""
lists = [1,1,2,3,4,5,6,]
def print_len(list):
    print(len(list))
print_len(lists)


# WAF to print the elements of a list in a single line. (list is the parameter)

names = ["ram", "shyam", "hari"]
def print_ele(list):
    for item in list:
        print(item, end=" ")
print_ele(names)


# WAP to find the factorial of n. (n is the parameter)
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(9)

# WAF to convert USD to INR
def convertor(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

convertor(73)

your_num = int(input("input your number"))

def find_numtype(your_num):
    if (your_num % 2 == 0):
        print("EVEN")
    else:
        print("ODD")

find_numtype(your_num)


"""

# Recursion
# when a function calls itself repeatedly
"""

def show(n):
    if (n == 0): #Base case
        return
    print(n)
    show(n-1)

show(5) #5, 4, 3, 2, 1



def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(4))

"""

# Practice
# Write a recursive function to calculate the sum of first n natural numbers.
"""
def calc_sum(n):
    if (n == 0):
        return 0
    return calc_sum(n-1) + n
print(calc_sum(10))

"""

# Write a recursive function to print all elements in a list. Hint : use list & index as parameters.

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango", "litchi", "apple", "banana"]

print_list(fruits)