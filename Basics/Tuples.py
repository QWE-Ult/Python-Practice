# ==========================================================
#                TUPLES IN PYTHON (COMPLETE GUIDE)
# ==========================================================
#
# A tuple is one of Python's built-in data types.
#
# Think of a tuple as:
#
#     A LOCKED LIST
#
# List  -> Can change (Mutable)
# Tuple -> Cannot change (Immutable)
#
# Example:
#
# List
# fruits = ["Apple", "Mango", "Banana"]
#
# Tuple
# fruits = ("Apple", "Mango", "Banana")
#
# Parentheses () are commonly used.
#
# ==========================================================


print("\n========== 1. Creating Tuples ==========\n")

t1 = (10, 20, 30)
print(t1)

t2 = ("Apple", "Banana", "Mango")
print(t2)

t3 = (1, "Hello", 5.6, True)
print(t3)


# Parentheses are optional

t4 = 10, 20, 30
print(t4)

print(type(t4))


# ==========================================================

print("\n========== 2. Why Use Tuples? ==========\n")

# Tuples are used when data should NOT change.

student = ("Rahul", 20, "Ahmedabad")

print(student)

# Name
# Age
# City

# We usually don't want these values changing accidentally.

# ==========================================================

print("\n========== 3. Empty Tuple ==========\n")

empty = ()

print(empty)
print(type(empty))

# ==========================================================

print("\n========== 4. Single Element Tuple ==========\n")

# Wrong

a = (5)

print(a)
print(type(a))

# It becomes an integer.


# Correct

b = (5,)

print(b)
print(type(b))

# Always remember:
# One element tuple MUST have a comma.

# ==========================================================

print("\n========== 5. Accessing Elements ==========\n")

fruits = ("Apple", "Banana", "Mango", "Orange")

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

# Negative Indexing

print(fruits[-1])
print(fruits[-2])

# ==========================================================

print("\n========== 6. Slicing ==========\n")

numbers = (10,20,30,40,50,60)

print(numbers[1:4])

print(numbers[:3])

print(numbers[3:])

print(numbers[:-1])

print(numbers[::-1])

# ==========================================================

print("\n========== 7. Tuple is Immutable ==========\n")

colors = ("Red","Green","Blue")

print(colors)

# This will give an error.

# colors[0] = "Black"

# TypeError:
# 'tuple' object does not support item assignment

# Tuples cannot be modified.

# ==========================================================

print("\n========== 8. Length ==========\n")

t = (1,2,3,4,5)

print(len(t))

# ==========================================================

print("\n========== 9. Looping ==========\n")

t = ("Python","Java","C++")

for item in t:
    print(item)

print()

for i in range(len(t)):
    print(i, t[i])

# ==========================================================

print("\n========== 10. Membership ==========\n")

fruits = ("Apple","Banana","Mango")

print("Apple" in fruits)

print("Orange" in fruits)

print("Orange" not in fruits)

# ==========================================================

print("\n========== 11. Concatenation ==========\n")

a = (1,2,3)

b = (4,5,6)

c = a + b

print(c)

# ==========================================================

print("\n========== 12. Repetition ==========\n")

a = ("Hi",)

print(a * 5)

# ==========================================================

print("\n========== 13. Tuple Packing ==========\n")

student = "Rahul",21,"Delhi"

print(student)

# Python automatically packs values into a tuple.

# ==========================================================

print("\n========== 14. Tuple Unpacking ==========\n")

student = ("Rahul",21,"Delhi")

name, age, city = student

print(name)
print(age)
print(city)

# ==========================================================

print("\n========== 15. Multiple Assignment ==========\n")

a,b,c = (10,20,30)

print(a)
print(b)
print(c)

# ==========================================================

print("\n========== 16. Swapping Variables ==========\n")

x = 10
y = 20

print(x,y)

x,y = y,x

print(x,y)

# Python internally uses tuple unpacking.

# ==========================================================

print("\n========== 17. Nested Tuple ==========\n")

data = (
    (1,"Rahul"),
    (2,"Amit"),
    (3,"Neha")
)

print(data)

print(data[0])

print(data[0][1])

print(data[2][1])

# ==========================================================

print("\n========== 18. Tuple Inside List ==========\n")

students = [
    ("Rahul",80),
    ("Amit",90),
    ("Neha",95)
]

print(students)

# ==========================================================

print("\n========== 19. List Inside Tuple ==========\n")

a = (
    [10,20],
    [30,40]
)

print(a)

# We cannot replace the list

# a[0] = [1,2]

# But...

a[0].append(100)

print(a)

# The tuple didn't change.
# The LIST inside it changed.

# ==========================================================

print("\n========== 20. Built-in Functions ==========\n")

t = (10,5,7,2,100)

print(len(t))

print(max(t))

print(min(t))

print(sum(t))

# ==========================================================

print("\n========== 21. count() ==========\n")

t = (1,2,2,2,3,4)

print(t.count(2))

print(t.count(5))

# ==========================================================

print("\n========== 22. index() ==========\n")

t = ("A","B","C","D")

print(t.index("C"))

# First occurrence

t = (10,20,30,20,40)

print(t.index(20))

# ==========================================================

print("\n========== 23. Sorting ==========\n")

t = (8,2,6,1,9)

print(sorted(t))

print(sorted(t, reverse=True))

# sorted() returns a LIST

print(type(sorted(t)))

# ==========================================================

print("\n========== 24. Convert List -> Tuple ==========\n")

l = [10,20,30]

t = tuple(l)

print(t)

# ==========================================================

print("\n========== 25. Convert Tuple -> List ==========\n")

t = (10,20,30)

l = list(t)

print(l)

# ==========================================================

print("\n========== 26. Deleting Tuple ==========\n")

t = (1,2,3)

print(t)

del t

# print(t)

# NameError

# ==========================================================

print("\n========== 27. Returning Multiple Values ==========\n")

def student():
    return "Rahul",20,85

result = student()

print(result)

print(type(result))

# Actually it returns a tuple.

# ==========================================================

print("\n========== 28. Unpacking Returned Values ==========\n")

def values():
    return 10,20,30

a,b,c = values()

print(a)
print(b)
print(c)

# ==========================================================

print("\n========== 29. Tuple Comprehension? ==========\n")

# There is NO tuple comprehension.

# Wrong:
#
# (x*x for x in range(5))
#
# This creates a Generator.

g = (x*x for x in range(5))

print(g)

print(type(g))

# To create a tuple:

t = tuple(x*x for x in range(5))

print(t)

# ==========================================================

print("\n========== 30. Packing vs Unpacking ==========\n")

# Packing

data = 1,2,3

print(data)

# Unpacking

a,b,c = data

print(a,b,c)

# ==========================================================

print("\n========== 31. Using * in Unpacking ==========\n")

numbers = (1,2,3,4,5,6)

a,*b,c = numbers

print(a)

print(b)

print(c)

# ==========================================================

print("\n========== 32. Comparing Tuples ==========\n")

print((1,2,3) == (1,2,3))

print((1,2) < (1,3))

print((5,8) > (5,4))

# Comparison happens element by element.

# ==========================================================

print("\n========== 33. Iterating with enumerate() ==========\n")

fruits = ("Apple","Banana","Mango")

for index,value in enumerate(fruits):
    print(index,value)

# ==========================================================

print("\n========== 34. zip() Creates Tuples ==========\n")

names = ["Rahul","Amit","Neha"]

marks = [80,90,95]

z = zip(names,marks)

print(list(z))

# Output:
# [('Rahul',80), ('Amit',90), ('Neha',95)]

# ==========================================================

print("\n========== 35. Dictionary Items are Tuples ==========\n")

student = {
    "Name":"Rahul",
    "Age":20
}

print(student.items())

for item in student.items():
    print(item)

# Each item is a tuple.

# ==========================================================

print("\n========== 36. Advantages ==========\n")

# Faster than lists
# Less memory
# Cannot change accidentally
# Hashable (if immutable elements)
# Can be dictionary keys

# ==========================================================

print("\n========== 37. Disadvantages ==========\n")

# Cannot add elements
# Cannot remove elements
# Cannot update elements
# Less flexible than lists

# ==========================================================

print("\n========== 38. List vs Tuple ==========\n")

"""
LIST

[]

Mutable

append()

remove()

pop()

sort()

more memory

slightly slower



TUPLE

()

Immutable

No append()

No remove()

No pop()

No sort()

less memory

slightly faster
"""

# ==========================================================
