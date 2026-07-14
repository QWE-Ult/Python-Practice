# ==========================================================
#                 SETS IN PYTHON (COMPLETE GUIDE)
# ==========================================================
#
# A Set is a built-in Python data type used to store
# multiple UNIQUE values.
#
# Think of a set as:
#
#        A BAG OF UNIQUE ITEMS
#
# Example:
#
# Basket:
# Apple
# Banana
# Mango
# Apple
# Mango
#
# Set automatically removes duplicates.
#
# Result:
# {"Apple", "Banana", "Mango"}
#
# ==========================================================

print("\n========== 1. Creating Sets ==========\n")

s1 = {10, 20, 30}
print(s1)

s2 = {"Apple", "Banana", "Mango"}
print(s2)

s3 = {1, "Hello", 5.5, True}
print(s3)

# ==========================================================

print("\n========== 2. Empty Set ==========\n")

a = {}
print(type(a))

# {} creates an EMPTY DICTIONARY.

b = set()
print(type(b))

# set() creates an EMPTY SET.

# ==========================================================

print("\n========== 3. Duplicate Values ==========\n")

numbers = {10,20,30,20,30,40,50,40}

print(numbers)

# Duplicate values are automatically removed.

# ==========================================================

print("\n========== 4. Unordered ==========\n")

fruits = {"Apple","Banana","Mango","Orange"}

print(fruits)

# Order may change every time you run the program.

# ==========================================================

print("\n========== 5. Length ==========\n")

print(len(fruits))

# ==========================================================

print("\n========== 6. Membership ==========\n")

print("Apple" in fruits)

print("Kiwi" in fruits)

print("Kiwi" not in fruits)

# ==========================================================

print("\n========== 7. Looping ==========\n")

for item in fruits:
    print(item)

# ==========================================================

print("\n========== 8. add() ==========\n")

fruits.add("Kiwi")

print(fruits)

# ==========================================================

print("\n========== 9. update() ==========\n")

fruits.update(["Pineapple","Grapes"])

print(fruits)

# Can also update with tuple or another set.

# ==========================================================

print("\n========== 10. remove() ==========\n")

fruits.remove("Kiwi")

print(fruits)

# remove() raises KeyError if item not found.

# ==========================================================

print("\n========== 11. discard() ==========\n")

fruits.discard("Watermelon")

print(fruits)

# discard() never gives an error.

# ==========================================================

print("\n========== 12. pop() ==========\n")

value = fruits.pop()

print(value)

print(fruits)

# Removes a random item.

# ==========================================================

print("\n========== 13. clear() ==========\n")

a = {1,2,3}

a.clear()

print(a)

# ==========================================================

print("\n========== 14. del ==========\n")

a = {1,2,3}

del a

# print(a)

# NameError

# ==========================================================

print("\n========== 15. Copy ==========\n")

a = {1,2,3}

b = a.copy()

print(a)

print(b)

# ==========================================================

print("\n========== 16. Union ==========\n")

A = {1,2,3}

B = {3,4,5}

print(A | B)

print(A.union(B))

# ==========================================================

print("\n========== 17. Intersection ==========\n")

A = {1,2,3}

B = {2,3,4}

print(A & B)

print(A.intersection(B))

# ==========================================================

print("\n========== 18. Difference ==========\n")

A = {1,2,3}

B = {2,3,4}

print(A - B)

print(A.difference(B))

# ==========================================================

print("\n========== 19. Symmetric Difference ==========\n")

A = {1,2,3}

B = {2,3,4}

print(A ^ B)

print(A.symmetric_difference(B))

# ==========================================================

print("\n========== 20. update() Operations ==========\n")

A = {1,2,3}
B = {3,4,5}

A.update(B)

print(A)

# ==========================================================

print("\n========== 21. intersection_update() ==========\n")

A = {1,2,3}

B = {2,3,4}

A.intersection_update(B)

print(A)

# ==========================================================

print("\n========== 22. difference_update() ==========\n")

A = {1,2,3}

B = {2,3}

A.difference_update(B)

print(A)

# ==========================================================

print("\n========== 23. symmetric_difference_update() ==========\n")

A = {1,2,3}

B = {2,3,4}

A.symmetric_difference_update(B)

print(A)

# ==========================================================

print("\n========== 24. issubset() ==========\n")

A = {1,2}

B = {1,2,3,4}

print(A.issubset(B))

# ==========================================================

print("\n========== 25. issuperset() ==========\n")

print(B.issuperset(A))

# ==========================================================

print("\n========== 26. isdisjoint() ==========\n")

A = {1,2}

B = {3,4}

print(A.isdisjoint(B))

# ==========================================================

print("\n========== 27. Frozen Set ==========\n")

fs = frozenset([1,2,3])

print(fs)

print(type(fs))

# Frozen set cannot be modified.

# fs.add(5)

# Error

# ==========================================================

print("\n========== 28. Set from List ==========\n")

nums = [1,2,2,3,4,4,5]

unique = set(nums)

print(unique)

# ==========================================================

print("\n========== 29. Set from String ==========\n")

word = "mississippi"

letters = set(word)

print(letters)

# ==========================================================

print("\n========== 30. Remove Duplicates ==========\n")

nums = [4,2,7,4,2,8,7,10]

unique = list(set(nums))

print(unique)

# ==========================================================

print("\n========== 31. Set Comprehension ==========\n")

square = {x*x for x in range(1,6)}

print(square)

# ==========================================================

print("\n========== 32. Conditional Set Comprehension ==========\n")

even = {x for x in range(20) if x%2==0}

print(even)

# ==========================================================

print("\n========== 33. Nested Loop Comprehension ==========\n")

pairs = {(x,y) for x in range(3) for y in range(3)}

print(pairs)

# ==========================================================

print("\n========== 34. max min sum ==========\n")

nums = {10,20,30,40}

print(max(nums))

print(min(nums))

print(sum(nums))

# ==========================================================

print("\n========== 35. sorted() ==========\n")

nums = {7,2,9,1}

print(sorted(nums))

# Returns a LIST

# ==========================================================

print("\n========== 36. Convert Set ==========\n")

nums = {1,2,3}

print(list(nums))

print(tuple(nums))

# ==========================================================

print("\n========== 37. Mutable vs Immutable ==========\n")

"""
Set

Mutable

Can add
Can remove


Frozen Set

Immutable

Cannot change
"""

# ==========================================================

print("\n========== 38. Hashable Objects ==========\n")

# Allowed

a = {1,2,3}

print(a)

# Not Allowed

# b = {[1,2],[3,4]}

# Lists are mutable.

# Tuples are allowed if immutable.

a = {(1,2),(3,4)}

print(a)

# ==========================================================

print("\n========== 40. List vs Set ==========\n")

"""
LIST

Ordered

Duplicates allowed

Indexed

Mutable

Slower searching



SET

Unordered

Unique values

No indexing

Mutable

Faster searching
"""

# ==========================================================

print("\n========== 41. Tuple vs Set ==========\n")

"""
Tuple

Ordered

Immutable

Duplicates allowed

Indexed



Set

Unordered

Mutable

Unique values

No indexing
"""

# ==========================================================