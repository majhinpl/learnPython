# List in Python
# A built-in data type that store a set of values
# It can store element of different types (integer, fload, string..)'

marks = [98.2, 85.4, 65.7, 75.2, 32.5, 65.4]
"""print(marks)
print(type(marks))
print(marks[2])"""

student = ["nephx", 87, 17, "arabia"]
# print(student)

student[0] = "hello"
# print(student)

# List Slicing
# similar to string slicing

# print(marks[1:5])


# List Methods
list = [2,1,3]

# append # adds one element at the end
list.append(4)
# print(list)

# sort #sorts in accending order
"""print(list.append(4))
print(list.sort())
print(list)"""

# decending sort
"""print(list.append(5))
print(list.sort(reverse=True))
print(list)

list = ["banana", "litchi", "apple"]
print(list.sort(reverse=True))
print(list)"""

# reverse
"""list = ["a", "b", "d", "h", "i"]
list.reverse()
print(list)
"""

# insert (idx, ele)

"""list.insert(2, 23)
print(list)"""

# remove
# pop

# Tuples in python
# A built-in data type that lets us create immutable sequesnce of value.

tup = (87, 64, 33, 95, 76)
"""print(tup[1])
print(tup[0])
# tup[0] = 43 # not allowed in python

singleTup = (1,) """

# Tuple Methods
# tup.index(el)
# tup.count(el) 


# Practice
# WAP to ask the user to enter names of their 3 favorite movie and store them in a ist.

"""movies = []
first_movie = input("enter your first movie :")
second_movie = input("enter your 2nd movie :")
third_movie = input("enter your 3rd movie :")

movies.append(first_movie)
movies.append(second_movie)
movies.append(third_movie)

print(movies)"""

#WAP to check if a list contains a palindrome of elements.

"""list1 = [1,2,3, 2]
copy_list1 = list1.copy()

if (copy_list1 == list1):
    print("palindrome")
else:
    print("NOT palindrome")"""

# WAP to count the number of students with the "A" grade in the following tuple

grades = ["C", "D", "A", "A", "B", "B", "A"]

# print(grades.count("A"))

# Store the above values in a list & sort them from A to D

grades.sort()
print(grades)

