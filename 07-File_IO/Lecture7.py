# File I/O in python
# Python can be used to perform operations on a file. (read & write data)

"""
# File type
Text files : .txt, .docx
Binary Files : .mp4, .mov
"""

# Open, read & close File
# We have to open a file before reading or writing.

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "practice.txt")

"""
with open(file_path, "r") as f:

    data = f.read()
    print(data) # Once files read there will be no data to read hence it will print blank.

    line1 = f.readline() 
    print(line1) # readline will read the first line of file.

    line2 = f.readline() 
    print(line2) # second readline will read the sec line of file. if there is no data it will print the blank

    line3 = f.readline() 
    print(line3) # rest readline will read the third.. line of file. if there is no data it will print the blank


    f.close()

"""

# Writing to a file.
# f = open("demo.txt", "w")
# f.write("this is a new line")

with open(file_path, "w") as f:

    f.write("\nA company called STOCKSLIFY.") 

    f.close()


with  open(file_path, "a+") as f:

    # f.write("Is this works!")
    print(f.read())

    # f.write("This is new data.")



# r+ : read + overwrite - (pointer place at starts) no truncate.
# w+ : read + overwrite - truncate.
# a+ : read and append - (pointer place at end) no truncate.
 
# With Syntax
"""
with open("demo.txt", "a") as f:
    data = f.read()

"""

# Deleting a file
# using the os module
"""
Module (like a code library) is a file written by another programmer that generally has a function we can use.

"""

# os.remove(file_path) #will delete the files

# Practice QS
# Create a new file "practice.txt" using python. Add the following data in it:

"""
Hi everyone
we are learning File I/O 
using Java.
i like programming in Java

"""
with open(file_path, "w") as f:

    f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")

# WAP that replace all occurences of "java" witht "python" in above file.

with open(file_path, "r") as f:
    data = f.read()
    

new_data = data.replace("Java", "Python")
print(new_data)


with open(file_path, "w") as f:
    f.write(new_data)

# Search in the word "learning" exists in file or not.

"""
with open(file_path, "r") as f:
    data = f.read()
    word = "learning"

    if data.find(word) != -1:
        print("Found")
    else:
        print("Not Found!")



def check_for_word():
    with open(file_path, "r") as f:
        data = f.read()
        word = "learning"

    if data.find(word) != -1:
        print("Found")
    else:
        print("Not Found!")

check_for_word()

"""

"""
# WAF to find in which line of the file does the word "learning" occur first.
# Print -1 if word not found.

"""

def check_wordline():
    word = "learning"
    line_no = 1
    data = True

    with open(file_path, "r") as f:
        data = f.read()
        while data:
            if (word in data):
                print(line_no)
                return
            line_no += 1
    return -1    
    

print(check_wordline())

# From a file containing numbers seperated by comma, print the count of even numbers.
with open(file_path, "w") as f:
    f.write("1, 2, 3, 78, 76, 100")


count = 0

with open(file_path, "r") as f:
    data = f.read()
    print("numbers :\n", data)
    nums = data.split(",")
    for val in nums:
        if (int(val) % 2 == 0):
            count += 1

print(count)