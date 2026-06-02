"""
PYTHON DATA TYPES
"""

print("=" * 50)
print("PYTHON DATA TYPES")
print("=" * 50)

# =====================================
# 1. INTEGER (int)
# =====================================

age = 25

print("\nINTEGER")
print(age)
print(type(age))

# Output:
# 25
# <class 'int'>


# =====================================
# 2. FLOAT (float)
# =====================================

price = 99.99

print("\nFLOAT")
print(price)
print(type(price))

# Output:
# 99.99
# <class 'float'>


# =====================================
# 3. COMPLEX (complex)
# =====================================

num = 3 + 4j

print("\nCOMPLEX")
print(num)
print(type(num))

# Output:
# (3+4j)
# <class 'complex'>


# =====================================
# 4. STRING (str)
# =====================================

name = "Python"

print("\nSTRING")
print(name)
print(type(name))

print("Length:", len(name))
print("Upper:", name.upper())
print("Lower:", name.lower())

# Output:
# Python
# <class 'str'>


# =====================================
# 5. BOOLEAN (bool)
# =====================================

is_valid = True

print("\nBOOLEAN")
print(is_valid)
print(type(is_valid))

# Output:
# True
# <class 'bool'>


# =====================================
# 6. LIST (list)
# =====================================

fruits = ["apple", "banana", "mango"]

print("\nLIST")
print(fruits)
print(type(fruits))

fruits.append("orange")

print("After Append:", fruits)

# Output:
# ['apple', 'banana', 'mango', 'orange']


# =====================================
# 7. TUPLE (tuple)
# =====================================

coordinates = (10, 20)

print("\nTUPLE")
print(coordinates)
print(type(coordinates))

# Output:
# (10, 20)
# <class 'tuple'>


# =====================================
# 8. SET (set)
# =====================================

numbers = {1, 2, 3, 3, 2, 1}

print("\nSET")
print(numbers)
print(type(numbers))

numbers.add(4)

print("After Add:", numbers)

# Output:
# {1, 2, 3, 4}
# <class 'set'>


# =====================================
# 9. DICTIONARY (dict)
# =====================================

student = {
    "name": "Yash",
    "age": 20,
    "course": "Python"
}

print("\nDICTIONARY")
print(student)
print(type(student))

print("Student Name:", student["name"])

# Output:
# {'name': 'Yash', 'age': 20, 'course': 'Python'}
# <class 'dict'>


# =====================================
# 10. NONE TYPE
# =====================================

value = None

print("\nNONE TYPE")
print(value)
print(type(value))

# Output:
# None
# <class 'NoneType'>


# =====================================
# TYPE CONVERSION
# =====================================

print("\nTYPE CONVERSION")

s = "100"

print(int(s))
print(float(s))
print(str(100))

# Output:
# 100
# 100.0
# 100


# =====================================
# isinstance()
# =====================================

print("\nISINSTANCE")

print(isinstance(age, int))
print(isinstance(name, str))
print(isinstance(fruits, list))

# Output:
# True
# True
# True


# =====================================
# MUTABLE VS IMMUTABLE
# =====================================

print("\nMUTABLE TYPES")
print("list")
print("dict")
print("set")

print("\nIMMUTABLE TYPES")
print("int")
print("float")
print("bool")
print("str")
print("tuple")
print("complex")


print("\nExamples")

print("type(10) =", type(10))
print("type(10.5) =", type(10.5))
print("type('Hello') =", type("Hello"))
print("type(True) =", type(True))
print("type([1,2,3]) =", type([1,2,3]))
print("type((1,2,3)) =", type((1,2,3)))
print("type({1,2,3}) =", type({1,2,3}))
print("type({'a':1}) =", type({'a':1}))
print("type(None) =", type(None))
print("type(2+5j) =", type(2+5j))
