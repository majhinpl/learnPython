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
