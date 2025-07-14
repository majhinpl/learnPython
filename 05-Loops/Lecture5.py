# Loops in python
# Loops are used to repeat instrunctions.

# while Loops 
"""
 while condition:
   #some work

"""
"""
count = 1 # iterator
while count <= 10 :
    print("hi")
    count += 1 # iteration

print(count)


count = 1 # iterator
while count <= 10 :
    print("hi", count)
    count += 1 # iteration

print(count)


i = 1 
while i <= 5 :
    print(i, i)
    i += 1 # iteration

print("loop ended")


i = 5
while i >= 1 :
    print(i, i)
    i -= 1 # iteration

print("loop ended")

"""

# Practice
# Print numbers from 1 to 100.
"""
n = 1
while n <= 100 :
    print(n)
    n += 1
print(n)


# Print numbers from 100 to 1

n = 100
while n >= 1 :
    print(n)
    n -= 1
print(n)


# Ptint the multiplication table of a number n.
n = int(input("enter your number : "))
i = 1
while i <= 10 :
    print(f"{n} X {i} = {n * i}")
    i += 1



# Print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]

# traverse
idx = 0
while idx < len(nums) :
    print(nums[idx])
    idx += 1



heroes = ["ironman", "thor", "superman", "batman"]
i = 0
while i < len(heroes) :
    print(heroes[i])
    i += 1

# Search for a number x in this tuple using loop: (1,4,9,16,25,36,49,64,81,100)

nums = (1,4,9,16,25,36,49,64,81,100)

x = int(input("Your number is : "))

i = 0 

while i < len(nums) :
    if (nums[i] == x): 
        print(f"found at idx : {i}")
    i += 1



# Break & Continue 
# Break : used to terminate the loop encounterd.

# Continue : terminates execution in the current iteration and continues execution of the loop with the next iteration.

i = 1
while i <= 5:
    print(i)
    if (i == 3):
        break
    i += 1

print("end of loops")



nums = (1,4,9,16,25,36,49,64,81,100)

x = int(input("Your number is : "))

i = 0 

while i < len(nums) :
    if (nums[i] == x): 
        print(f"found at idx : {i}")
        break
    else :
        print("finding...")
    i += 1
print("end of loop")


i = 0 
while i <= 5:
    if(i == 3):
        i += 1
        continue # skip
    print(i)
    i += 1
"""

# For loops
# For loops are used for sequential. For traversing list, string, tuples etc.
"""
nums = [1,2,3,4,5]
for val in nums :
  print(val)

 """

"""
# Practice Qs
# Print the elements of the following list using a for loop.
ele = [1,4,9,16,25,36,49,64,81,100]
for num in ele :
    print(num) 


# Search for a number x in this tuple using loop.
# [1,4,9,16,25,36,49,64,81,100] # Linear search
tup = [1,4,9,16,25,36,49,64,81,100] 
x = 36
idx = 0

for num in tup :
    if (num == x) :
        print(f"found in idx: {idx}, x = {num}" )
        break
    idx += 1

"""

# range()
# Range function returns a sequence of numbers, string from 0 by default, and increments by 1 (by default), and stops before a specifed number.

# range(start?, stop, step?)
"""
seq = range(10) #range(stop)
for i in seq :
    print(i)


for i in range(2, 10) : # range(start, stop)
    print(i)


for i in range(2, 10, 2) : # range(start, stop, step)
    print(i)



for i in range(1, 100, 5) : # range(start, stop, step)
    print(i)

    
"""

# Practice question
# using for & range()

"""
# Print numbers from 1 100
for num in range(1, 101):
    print(num)


# Print numbers from 100 1

for num in range(100, 0, -1):
    print(num)

 

# Print the multiplication table of a number n.

n = int(input("input a number :"))

for i in range(1, 11) :
    print(i * n)



# pass Statement
# pass is a null statement that does nothing. it is use as a placeholder for future code.

for i in range(5):
    pass


if i > 5:
    pass

print("some useful work")


# Qs 
# WAP to find the sum of first n numbers. (using while)

n = 5
sum = 0
i = 1

while i <= n:
    sum += i 
    i += 1

print(f"Total sum = {sum}")

"""

# WAP to find the factorial of first n numbers. (using for)
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"factorial = {fact}")
