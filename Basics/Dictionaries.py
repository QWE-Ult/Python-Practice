# ==========================================================
#            DICTIONARIES IN PYTHON (COMPLETE GUIDE)
# ==========================================================
#
# A Dictionary is a built-in data type used to store
# data in the form of KEY : VALUE pairs.
#
# Think of a dictionary like a real dictionary.
#
# Word        Meaning
# Apple   ->  A Fruit
# Car     ->  A Vehicle
# Python  ->  A Programming Language
#
# Here,
# Word = Key
# Meaning = Value
#
# ==========================================================

print("\n========== 1. Creating Dictionaries ==========\n")

student = {
    "name": "Rahul",
    "age": 21,
    "city": "Ahmedabad"
}

print(student)

# ==========================================================

print("\n========== 2. Different Ways to Create Dictionaries ==========\n")

# Method 1

d1 = {
    "A": 10,
    "B": 20
}

print(d1)

# Method 2

d2 = dict(name="Amit", age=22)

print(d2)

# Method 3

d3 = dict([
    ("x",10),
    ("y",20),
    ("z",30)
])

print(d3)

# Method 4

d4 = {}

print(d4)

# ==========================================================

print("\n========== 3. Dictionary Characteristics ==========\n")

"""
Dictionary

Ordered (Python 3.7+)

Mutable

Keys are unique

Values may repeat

Stores Key : Value pairs
"""

# ==========================================================

print("\n========== 4. Keys and Values ==========\n")

student = {
    "name":"Rahul",
    "age":21,
    "city":"Ahmedabad"
}

print(student)

print(student.keys())

print(student.values())

print(student.items())

# ==========================================================

print("\n========== 5. Valid Keys ==========\n")

data = {
    1:"Integer",
    5.5:"Float",
    True:"Boolean",
    "Python":"String",
    (1,2):"Tuple"
}

print(data)

# ==========================================================

print("\n========== 6. Invalid Keys ==========\n")

# Lists cannot be keys

# {
#     [1,2]:"Hello"
# }

# Sets cannot be keys

# {
#     {1,2}:"Hello"
# }

# Dictionaries cannot be keys

# {
#     {"A":1}:"Hello"
# }

print("List, Set and Dictionary cannot be dictionary keys.")

# ==========================================================

print("\n========== 7. Duplicate Keys ==========\n")

data = {
    "A":10,
    "A":50,
    "B":20
}

print(data)

# The last value replaces the previous value.

# ==========================================================

print("\n========== 8. Duplicate Values ==========\n")

data = {
    "A":10,
    "B":10,
    "C":10
}

print(data)

# Duplicate values are allowed.

# ==========================================================

print("\n========== 9. Accessing Values ==========\n")

student = {
    "name":"Rahul",
    "age":21,
    "city":"Ahmedabad"
}

print(student["name"])

print(student["age"])

print(student["city"])

# ==========================================================

print("\n========== 10. Accessing Missing Key ==========\n")

# print(student["salary"])

# KeyError

# ==========================================================

print("\n========== 11. get() ==========\n")

print(student.get("name"))

print(student.get("city"))

print(student.get("salary"))

print(student.get("salary",0))

# ==========================================================

print("\n========== 12. Adding New Items ==========\n")

student["gender"] = "Male"

print(student)

student["country"] = "India"

print(student)

# ==========================================================

print("\n========== 13. Updating Existing Items ==========\n")

student["age"] = 22

print(student)

student["city"] = "Surat"

print(student)

# ==========================================================

print("\n========== 14. update() ==========\n")

student.update({
    "country":"India",
    "state":"Gujarat"
})

print(student)

student.update({
    "age":25
})

print(student)

# ==========================================================

print("\n========== 15. setdefault() ==========\n")

student.setdefault("college","GTU")

print(student)

student.setdefault("name","Someone")

print(student)

# setdefault()

# Adds the key only if it does not exist.

# ==========================================================

print("\n========== 16. Removing Items using pop() ==========\n")

marks = {
    "Math":90,
    "Science":80,
    "English":85
}

print(marks)

removed = marks.pop("Science")

print(removed)

print(marks)

# ==========================================================

print("\n========== 17. pop() with Default Value ==========\n")

print(marks.pop("Hindi","Not Found"))

# ==========================================================

print("\n========== 18. popitem() ==========\n")

data = {
    "A":10,
    "B":20,
    "C":30
}

print(data)

item = data.popitem()

print(item)

print(data)

# popitem() removes the last inserted item.

# ==========================================================

print("\n========== 19. del ==========\n")

student = {
    "name":"Rahul",
    "age":21,
    "city":"Ahmedabad"
}

print(student)

del student["age"]

print(student)

# ==========================================================

print("\n========== 20. clear() ==========\n")

student.clear()

print(student)

# ==========================================================

print("\n========== 21. copy() ==========\n")

a = {
    "A":10,
    "B":20
}

b = a.copy()

print(a)

print(b)

# copy() creates a new dictionary.

# ==========================================================

print("\n========== 22. keys() ==========\n")

student = {
    "name": "Rahul",
    "age": 21,
    "city": "Ahmedabad"
}

print(student.keys())

for key in student.keys():
    print(key)

# keys() returns all the keys.

# ==========================================================

print("\n========== 23. values() ==========\n")

print(student.values())

for value in student.values():
    print(value)

# values() returns all the values.

# ==========================================================

print("\n========== 24. items() ==========\n")

print(student.items())

for item in student.items():
    print(item)

# Each item is a tuple.

# Example:
# ("name", "Rahul")

# ==========================================================

print("\n========== 25. Looping Through Dictionary ==========\n")

student = {
    "name":"Rahul",
    "age":21,
    "city":"Ahmedabad"
}

for key in student:
    print(key)

# Default loop gives keys.

# ==========================================================

print("\n========== 26. Looping Using keys() ==========\n")

for key in student.keys():
    print(key)

# ==========================================================

print("\n========== 27. Looping Using values() ==========\n")

for value in student.values():
    print(value)

# ==========================================================

print("\n========== 28. Looping Using items() ==========\n")

for key, value in student.items():
    print(key, ":", value)

# ==========================================================

print("\n========== 29. Access Values Inside Loop ==========\n")

for key in student:
    print(key, student[key])

# ==========================================================

print("\n========== 30. Membership Operators ==========\n")

print("name" in student)

print("salary" in student)

print("city" not in student)

print("salary" not in student)

# Membership checks only KEYS.

# ==========================================================

print("\n========== 31. len() ==========\n")

print(len(student))

# Number of key-value pairs.

# ==========================================================

print("\n========== 32. Nested Dictionary ==========\n")

students = {
    101: {
        "name":"Rahul",
        "marks":90
    },
    102: {
        "name":"Neha",
        "marks":95
    },
    103: {
        "name":"Amit",
        "marks":88
    }
}

print(students)

# ==========================================================

print("\n========== 33. Access Nested Dictionary ==========\n")

print(students[101])

print(students[101]["name"])

print(students[102]["marks"])

# ==========================================================

print("\n========== 34. Update Nested Dictionary ==========\n")

students[101]["marks"] = 99

print(students)

students[103]["name"] = "Rohan"

print(students)

# ==========================================================

print("\n========== 35. Dictionary Inside List ==========\n")

employees = [
    {
        "id":1,
        "name":"Rahul"
    },
    {
        "id":2,
        "name":"Neha"
    },
    {
        "id":3,
        "name":"Amit"
    }
]

print(employees)

# ==========================================================

print("\n========== 36. Access Dictionary Inside List ==========\n")

print(employees[0])

print(employees[1]["name"])

print(employees[2]["id"])

# ==========================================================

print("\n========== 37. Loop Dictionary Inside List ==========\n")

for employee in employees:
    print(employee)

print()

for employee in employees:
    print(employee["name"])

# ==========================================================

print("\n========== 38. List Inside Dictionary ==========\n")

student = {
    "name":"Rahul",
    "subjects":[
        "Python",
        "Java",
        "SQL"
    ]
}

print(student)

# ==========================================================

print("\n========== 39. Access List Inside Dictionary ==========\n")

print(student["subjects"])

print(student["subjects"][0])

print(student["subjects"][2])

# ==========================================================

print("\n========== 40. Modify List Inside Dictionary ==========\n")

student["subjects"].append("C++")

print(student)

student["subjects"].remove("Java")

print(student)

# ==========================================================

print("\n========== 41. Dictionary Comprehension ==========\n")

square = {
    x : x*x
    for x in range(1,6)
}

print(square)

# ==========================================================

print("\n========== 42. Dictionary Comprehension with Condition ==========\n")

even_square = {
    x : x*x
    for x in range(1,11)
    if x % 2 == 0
}

print(even_square)

# ==========================================================

print("\n========== 43. Dictionary Comprehension Using String ==========\n")

word = "python"

letters = {
    ch : ord(ch)
    for ch in word
}

print(letters)

# ==========================================================

print("\n========== 44. fromkeys() ==========\n")

keys = [
    "name",
    "age",
    "city"
]

data = dict.fromkeys(keys)

print(data)

# Default value is None.

# ==========================================================

print("\n========== 45. fromkeys() with Value ==========\n")

data = dict.fromkeys(keys, "Unknown")

print(data)

# ==========================================================

print("\n========== 46. Dictionary Unpacking (**) ==========\n")

student = {
    "name": "Rahul",
    "age": 21
}

details = {
    **student,
    "city": "Ahmedabad",
    "country": "India"
}

print(details)

# ** copies all key-value pairs into another dictionary.

# ==========================================================

print("\n========== 47. Dictionary Unpacking (Overwrite) ==========\n")

a = {
    "x": 10,
    "y": 20
}

b = {
    "y": 50,
    "z": 100
}

result = {
    **a,
    **b
}

print(result)

# If the same key exists,
# the last value is kept.

# ==========================================================

print("\n========== 48. Merging Dictionaries Using update() ==========\n")

d1 = {
    "A": 10,
    "B": 20
}

d2 = {
    "C": 30,
    "D": 40
}

print(d1)

d1.update(d2)

print(d1)

# update() modifies the original dictionary.

# ==========================================================

print("\n========== 49. Merging Using | Operator ==========\n")

a = {
    "x": 1,
    "y": 2
}

b = {
    "z": 3
}

c = a | b

print(c)

# Original dictionaries remain unchanged.

print(a)

print(b)

# ==========================================================

print("\n========== 50. Sorting Dictionary Keys ==========\n")

marks = {
    "Rahul": 80,
    "Neha": 95,
    "Amit": 90,
    "Karan": 75
}

print(sorted(marks))

# sorted(dictionary)
# returns sorted KEYS.

# ==========================================================

print("\n========== 51. Sorting Dictionary Values ==========\n")

print(sorted(marks.values()))

# ==========================================================

print("\n========== 52. Sorting Dictionary Items ==========\n")

print(sorted(marks.items()))

# Items are sorted by keys.

# ==========================================================

print("\n========== 53. Sorting Items by Values ==========\n")

sorted_marks = sorted(
    marks.items(),
    key=lambda item: item[1]
)

print(sorted_marks)

# item[0] = Key
# item[1] = Value

# ==========================================================

print("\n========== 54. Sorting in Descending Order ==========\n")

descending = sorted(
    marks.items(),
    key=lambda item: item[1],
    reverse=True
)

print(descending)

# ==========================================================

print("\n========== 55. max() ==========\n")

numbers = {
    "a": 20,
    "b": 80,
    "c": 40
}

print(max(numbers))

# max() checks KEYS.

print(max(numbers.values()))

# ==========================================================

print("\n========== 56. min() ==========\n")

print(min(numbers))

print(min(numbers.values()))

# ==========================================================

print("\n========== 57. sum() ==========\n")

print(sum(numbers.values()))

# sum() works on values.

# ==========================================================

print("\n========== 58. sorted() ==========\n")

print(sorted(numbers))

print(sorted(numbers.values()))

print(sorted(numbers.items()))

# ==========================================================

print("\n========== 59. Combining Built-in Functions ==========\n")

salary = {
    "Rahul": 50000,
    "Neha": 75000,
    "Amit": 62000,
    "Rohan": 58000
}

print("Maximum Salary")

print(max(salary.values()))

print()

print("Minimum Salary")

print(min(salary.values()))

print()

print("Total Salary")

print(sum(salary.values()))

print()

print("Sorted Employee Names")

print(sorted(salary))

# ==========================================================

print("\n========== 60. Complete Example ==========\n")

students = {
    "Rahul": 88,
    "Amit": 95,
    "Neha": 91
}

print(students)

students["Karan"] = 76

students["Rahul"] = 90

print(students)

print(students.get("Neha"))

print(students.keys())

print(students.values())

print(students.items())

print(len(students))

print(sum(students.values()))

print(max(students.values()))

print(min(students.values()))

print(sorted(students))

print(sorted(students.values()))

for name, marks in students.items():
    print(name, marks)

# ==========================================================
