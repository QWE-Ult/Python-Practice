# ===============
# INTEGERS
# ===============

# Creating Integers

a = 10
b = -20
c = 0

print(a)  # 10
print(b)  # -20
print(c)  # 0


# Checking Type

print(type(a))  # <class 'int'>
print(type(b))  # <class 'int'>


# Addition

x = 20
y = 5

print(x + y)  # 25


# Subtraction

print(x - y)  # 15


# Multiplication

print(x * y)  # 100


# Division

print(x / y)  # 4.0


# Floor Division

print(x // y)  # 4


# Modulus

print(x % y)  # 0


# Power

print(x ** y)  # 3200000


# Absolute Value

n = -25

print(abs(n))  # 25


# Type Conversion String to Integer

s = "100"

num = int(s)

print(num)         # 100
print(type(num))   # <class 'int'>


# Float to Integer

f = 12.8

print(int(f))  # 12


# Comparison Operators

a = 10
b = 20

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True



# Increment

count = 10

count = count + 1

print(count)  # 11


# Decrement

count = count - 1

print(count)  # 10


# Augmented Assignment

x = 10

x += 5
print(x)  # 15

x -= 3
print(x)  # 12

x *= 2
print(x)  # 24

x //= 4
print(x)  # 6


# Integer Division

print(17 // 5)  # 3


# Remainder

print(17 % 5)  # 2


# Power

print(2 ** 5)  # 32



# Prime Number Check

num = 13
prime = True

if num < 2:
    prime = False

for i in range(2, num):
    if num % i == 0:
        prime = False
        break

print(prime)  # True




# Bitwise AND

print(5 & 3)  # 1


# Bitwise OR

print(5 | 3)  # 7


# Bitwise XOR

print(5 ^ 3)  # 6


# Bitwise NOT

print(~5)  # -6


# Left Shift

print(5 << 1)  # 10


# Right Shift

print(5 >> 1)  # 2


# Large Integer

big_num = 999999999999999999999999999999999999

print(big_num)

# 999999999999999999999999999999999999


# Boolean as Integer

print(True + True)    # 2
print(True + False)   # 1

print(isinstance(True, int))  # True


# ASCII Value

print(ord("A"))  # 65


# Character from ASCII

print(chr(65))  # A




nums = [10, 5, 20, 50, 3]

# Minimum Value
print(min(nums))  # 3


# Maximum Value
print(max(nums))  # 50


# Integer Membership

nums = [1, 2, 3, 4, 5]

print(3 in nums)   # True
print(10 in nums)  # False


# Integer Functions Summary

# int()       -> Convert to integer
# abs()       -> Absolute value
# min()       -> Smallest value
# max()       -> Largest value
# type()      -> Check datatype
# id()        -> Memory address
# ord()       -> Character to ASCII
# chr()       -> ASCII to Character
# isinstance() -> Check object type