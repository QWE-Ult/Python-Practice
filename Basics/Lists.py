# ==========================================
# PYTHON LIST
# ==========================================

# What is a List?
# A list is an ordered, mutable (changeable)
# collection that can store multiple values.

# ------------------------------------------
# Creating Lists
# ------------------------------------------

nums = [1, 2, 3, 4, 5]

mixed = [1, "hello", 3.5, True]

empty = []

print(nums)
# Output:
# [1, 2, 3, 4, 5]

print(mixed)
# Output:
# [1, 'hello', 3.5, True]

# ------------------------------------------
# Accessing Elements
# ------------------------------------------

a = [10, 20, 30, 40, 50]

print(a[0])
# Output: 10

print(a[2])
# Output: 30

print(a[-1])
# Output: 50

print(a[-2])
# Output: 40

# ------------------------------------------
# Slicing
# ------------------------------------------

print(a[1:4])
# Output:
# [20, 30, 40]

print(a[:3])
# Output:
# [10, 20, 30]

print(a[2:])
# Output:
# [30, 40, 50]

print(a[::-1])
# Output:
# [50, 40, 30, 20, 10]

# ------------------------------------------
# Updating Elements
# ------------------------------------------

a[0] = 100

print(a)
# Output:
# [100, 20, 30, 40, 50]

# ------------------------------------------
# Adding Elements
# ------------------------------------------

l = [1, 2, 3]

l.append(4)

print(l)
# Output:
# [1, 2, 3, 4]

l.extend([5, 6, 7])

print(l)
# Output:
# [1, 2, 3, 4, 5, 6, 7]

l.insert(1, 99)

print(l)
# Output:
# [1, 99, 2, 3, 4, 5, 6, 7]

# ------------------------------------------
# Removing Elements
# ------------------------------------------

l = [10, 20, 30, 40, 50]

l.remove(30)

print(l)
# Output:
# [10, 20, 40, 50]

l.pop()

print(l)
# Output:
# [10, 20, 40]

l.pop(1)

print(l)
# Output:
# [10, 40]

del l[0]

print(l)
# Output:
# [40]

# ------------------------------------------
# Clearing List
# ------------------------------------------

l.clear()

print(l)
# Output:
# []

# ------------------------------------------
# List Length
# ------------------------------------------

nums = [1, 2, 3, 4, 5]

print(len(nums))
# Output:
# 5

# ------------------------------------------
# Membership Operators
# ------------------------------------------

nums = [10, 20, 30]

print(20 in nums)
# Output:
# True

print(50 in nums)
# Output:
# False

print(20 not in nums)
# Output:
# False

# ------------------------------------------
# Concatenation
# ------------------------------------------

a = [1, 2]
b = [3, 4]

c = a + b

print(c)
# Output:
# [1, 2, 3, 4]

# ------------------------------------------
# Repetition
# ------------------------------------------

print([1, 2] * 3)

# Output:
# [1, 2, 1, 2, 1, 2]

# ------------------------------------------
# List Traversal
# ------------------------------------------

nums = [10, 20, 30]

for num in nums:
    print(num)

# Output:
# 10
# 20
# 30

for i in range(len(nums)):
    print(i, nums[i])

# Output:
# 0 10
# 1 20
# 2 30

# ------------------------------------------
# Common List Methods
# ------------------------------------------

l = [3, 1, 5, 2, 4]

l.sort()

print(l)
# Output:
# [1, 2, 3, 4, 5]

l.sort(reverse=True)

print(l)
# Output:
# [5, 4, 3, 2, 1]

l.reverse()

print(l)
# Output:
# [1, 2, 3, 4, 5]

print(l.count(5))
# Output:
# 1

print(l.index(2))
# Output:
# 1

# ------------------------------------------
# Copying Lists
# ------------------------------------------

a = [1, 2, 3]

b = a.copy()

print(b)

# Output:
# [1, 2, 3]

# ------------------------------------------
# Shallow Copy Problem
# ------------------------------------------

a = [1, 2, 3]

b = a

b[0] = 100

print(a)
# Output:
# [100, 2, 3]

print(b)
# Output:
# [100, 2, 3]

# Both variables point to same list.

# ------------------------------------------
# List Comprehension
# ------------------------------------------

squares = [x * x for x in range(1, 6)]

print(squares)

# Output:
# [1, 4, 9, 16, 25]

evens = [x for x in range(10) if x % 2 == 0]

print(evens)

# Output:
# [0, 2, 4, 6, 8]

# ------------------------------------------
# Nested Lists
# ------------------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])

# Output:
# [1, 2, 3]

print(matrix[1][2])

# Output:
# 6

# ------------------------------------------
# Useful Functions
# ------------------------------------------

nums = [10, 20, 30, 40]

print(max(nums))
# Output:
# 40

print(min(nums))
# Output:
# 10

print(sum(nums))
# Output:
# 100

# ------------------------------------------
# Sorting Without Modifying Original List
# ------------------------------------------

nums = [5, 2, 8, 1]

new_list = sorted(nums)

print(nums)

# Output:
# [5, 2, 8, 1]

print(new_list)

# Output:
# [1, 2, 5, 8]

# ------------------------------------------
# Converting Other Types to List
# ------------------------------------------

s = "hello"

print(list(s))

# Output:
# ['h', 'e', 'l', 'l', 'o']

t = (1, 2, 3)

print(list(t))

# Output:
# [1, 2, 3]

# ------------------------------------------
# List Packing and Unpacking(doubt)
# ------------------------------------------

nums = [10, 20, 30]

a, b, c = nums

print(a)
# Output: 10

print(b)
# Output: 20

print(c)
# Output: 30

# ------------------------------------------
# append() vs extend()
# ------------------------------------------

l = [1, 2]

l.append([3, 4])

print(l)

# Output:
# [1, 2, [3, 4]]

# append() adds ONE object.

l = [1, 2]

l.extend([3, 4])

print(l)

# Output:
# [1, 2, 3, 4]

# extend() adds each element separately.

# ------------------------------------------
# insert() Example
# ------------------------------------------

l = [10, 20, 30]

l.insert(1, 99)

print(l)

# Output:
# [10, 99, 20, 30]

# ------------------------------------------
# reverse() vs reversed()
# ------------------------------------------

l = [1, 2, 3]

l.reverse()

print(l)

# Output:
# [3, 2, 1]

l = [1, 2, 3]

print(list(reversed(l)))

# Output:
# [3, 2, 1]

print(l)

# Output:
# [1, 2, 3]

# reversed() does not modify original list.
