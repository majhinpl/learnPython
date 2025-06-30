"""
Dictionary in python

They are unordered, mutable(changeable) & don't allow duplicate keys

"""

info = {
    "name" : "nephx",
    "age" : 125,
    "learning" : "coading",
    "sub": ["js", "py", "c"],
    "topics": ("dict", "set")
}

"""print(type(info))
print(info["sub"])
info["name"] = "nephx"
info["lastname"] = "majhi"
print(info)"""

# Nested Dictionaries
student = {
    "name" : "nephx",
    "score": {
        "chem": 98,
        "phy": 97,
        "math" : 95
    }
}

"""print(student)
print(student["score"])
print(student["score"]["math"])"""

# Dictionary Methods
# Keys()
"""print(student.keys())
print(list(student.keys()))"""


# values()
"""print(student.values())
print(list(student.values()))"""

# items() # returns in tuples
"""print(student.items())"""

# get() # returns the key accourding to values.
"""print(student["name"])
print(student.get("name"))"""

# update() #insets the specified items to the dictionary.
"""student.update({"city": "jubail"})
print(student)"""


# Set in Python
# set is the collection of the unordered items.
# Each element in the set must be unique & immutable.

collection = {1,2,3,4, "hello", "hello"}

"""
print(collection)
print(type(collection))
print(len(collection))

"""
# empty sets // 

collection = set()

"""
print(collection)
print(type(collection))

"""

# Set Methods

"""
add(), remove(), clear(), pop()

"""
"""
collection.add(1)
collection.add(2)
collection.add(3)
collection.remove(3)
collection.add("nephx") 
collection.add((1,2,3,"tuple"))

print(collection)
collection.clear()
print(len(collection))
"""

# pop
"""
collection = {"hello", "nephx", "learn", "coading"}
print(collection.pop()) # output random values

"""

# union(set2) # combines both set values & returns new
set1 = {1,2,3}
set2 = {3,4,5}

# print(set1.union(set2))

# intersection(set2) #combines common values & returns new

# print(set1.intersection(set2))

# Practice

# Store following word meaninigs in a python in a python dictionary.

"""
word_meaning = {
    "table" : ["a pice of furniture", "list of facts & figures"],
    "cat": "a small animal"
}

print(word_meaning)

"""

# You are given a list of subjects for students. assume one classroom is required for 1 subject. how many classrooms are needed by all students.

"""
subjects = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}

print(len(subjects))

"""

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

"""
marks = {}

x = int(input("Enter your mark1: "))
marks.update({"marks1": x})

x = int(input("Enter your mark2: "))
marks.update({"marks2": x})

x = int(input("Enter your mark3: "))
marks.update({"marks3": x})

print(marks)

"""
# Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types)

values = {9, 9.0}
print(values)

values = {
    ("int", 9),
    ("float", 9.0)
}

print(values)
