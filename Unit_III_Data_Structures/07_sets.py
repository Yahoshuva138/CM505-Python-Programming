"""
Program 7: Sets
Demonstrates creation, operations, and methods
"""

print("=== SET CREATION ===")
empty_set = set()  # Must use set() for empty set, {} is for dict
set1 = {1, 2, 3, 4, 5}
set2 = {"apple", "banana", "cherry"}
set_from_list = set([1, 2, 2, 3, 3, 3])  # Duplicates removed

print(f"Empty set: {empty_set}")
print(f"Numbers: {set1}")
print(f"Fruits: {set2}")
print(f"From list [1, 2, 2, 3, 3, 3]: {set_from_list}")

print("\n=== SET PROPERTIES ===")
print("Sets are unordered, unindexed, and contain unique elements")
numbers = {3, 1, 4, 1, 5, 9, 2, 6, 5}
print(f"From {list(range(1, 6))} + duplicates: {numbers}")

# Try to access by index (will fail)
try:
    print(numbers[0])
except TypeError as e:
    print(f"Error: {e} - Sets don't support indexing")

print("\n=== ADDING ELEMENTS ===")
fruits = {"apple", "banana"}
print(f"Original: {fruits}")
fruits.add("cherry")
print(f"After add('cherry'): {fruits}")
fruits.update(["date", "elderberry"])
print(f"After update(['date', 'elderberry']): {fruits}")

print("\n=== REMOVING ELEMENTS ===")
fruits = {"apple", "banana", "cherry"}
print(f"Original: {fruits}")

# remove
fruits_copy = fruits.copy()
fruits_copy.remove("banana")
print(f"After remove('banana'): {fruits_copy}")

# discard
fruits_copy = fruits.copy()
fruits_copy.discard("apple")
print(f"After discard('apple'): {fruits_copy}")

# pop (removes arbitrary element)
fruits_copy = fruits.copy()
removed = fruits_copy.pop()
print(f"After pop(): {fruits_copy}, removed: {removed}")

# clear
fruits_copy = fruits.copy()
fruits_copy.clear()
print(f"After clear(): {fruits_copy}")

print("\n=== SET OPERATIONS - UNION ===")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"set1 | set2 (union): {set1 | set2}")
print(f"set1.union(set2): {set1.union(set2)}")

print("\n=== SET OPERATIONS - INTERSECTION ===")
print(f"set1 & set2 (intersection): {set1 & set2}")
print(f"set1.intersection(set2): {set1.intersection(set2)}")

print("\n=== SET OPERATIONS - DIFFERENCE ===")
print(f"set1 - set2 (difference): {set1 - set2}")
print(f"set1.difference(set2): {set1.difference(set2)}")
print(f"set2 - set1 (difference): {set2 - set1}")

print("\n=== SET OPERATIONS - SYMMETRIC DIFFERENCE ===")
print(f"set1 ^ set2 (symmetric difference): {set1 ^ set2}")
print(f"set1.symmetric_difference(set2): {set1.symmetric_difference(set2)}")

print("\n=== SET COMPARISON ===")
set_a = {1, 2, 3}
set_b = {1, 2, 3}
set_c = {1, 2, 3, 4}
set_d = {4, 5, 6}

print(f"set_a: {set_a}")
print(f"set_b: {set_b}")
print(f"set_c: {set_c}")
print(f"set_d: {set_d}")
print(f"set_a == set_b: {set_a == set_b}")
print(f"set_a.issubset(set_c): {set_a.issubset(set_c)}")
print(f"set_c.issuperset(set_a): {set_c.issuperset(set_a)}")
print(f"set_a.isdisjoint(set_d): {set_a.isdisjoint(set_d)}")

print("\n=== CHECKING MEMBERSHIP ===")
numbers = {1, 2, 3, 4, 5}
print(f"Set: {numbers}")
print(f"3 in numbers: {3 in numbers}")
print(f"10 in numbers: {10 in numbers}")
print(f"2 not in numbers: {2 not in numbers}")

print("\n=== SET SIZE AND ITERATION ===")
colors = {"red", "green", "blue"}
print(f"Set: {colors}")
print(f"len(): {len(colors)}")
print("Iterating:")
for color in colors:
    print(f"  {color}")

print("\n=== REMOVING DUPLICATES FROM LIST ===")
numbers = [1, 2, 3, 2, 4, 3, 5, 1, 6]
unique = set(numbers)
print(f"Original list: {numbers}")
print(f"Unique (as set): {unique}")
print(f"Unique (as list): {list(unique)}")

print("\n=== SET COMPREHENSION ===")
numbers = range(1, 11)
# Even numbers
even_set = {n for n in numbers if n % 2 == 0}
print(f"Even numbers 1-10: {even_set}")

# Squares
squares_set = {n ** 2 for n in range(1, 6)}
print(f"Squares 1-5: {squares_set}")

# From list removing duplicates
words = ["apple", "banana", "apple", "cherry", "banana"]
unique_words = {word.upper() for word in words}
print(f"Words (lowercase): {words}")
print(f"Unique (uppercase): {unique_words}")

print("\n=== FROZENSET (IMMUTABLE SET) ===")
regular_set = {1, 2, 3}
frozen_set = frozenset({1, 2, 3})

print(f"Regular set: {regular_set}")
print(f"Frozen set: {frozen_set}")

try:
    frozen_set.add(4)
except AttributeError as e:
    print(f"Cannot modify frozenset: {e}")

# Frozenset can be used as dictionary key
dict_with_set_key = {frozen_set: "value"}
print(f"Using frozenset as dict key: {dict_with_set_key}")
