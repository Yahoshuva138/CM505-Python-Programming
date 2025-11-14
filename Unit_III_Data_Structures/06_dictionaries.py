"""
Program 6: Dictionaries
Demonstrates creation, operations, methods, and comprehension
"""

print("=== DICTIONARY CREATION ===")
empty_dict = {}
student = {"name": "Alice", "age": 25, "city": "New York"}
phone_book = {"Alice": "123-456", "Bob": "234-567", "Charlie": "345-678"}
mixed_dict = {1: "one", "two": 2, 3.0: "three"}

print(f"Empty: {empty_dict}")
print(f"Student: {student}")
print(f"Phone book: {phone_book}")
print(f"Mixed: {mixed_dict}")

# Using dict() constructor
dict_from_pairs = dict([("a", 1), ("b", 2), ("c", 3)])
print(f"From pairs: {dict_from_pairs}")

print("\n=== ACCESSING DICTIONARY VALUES ===")
student = {"name": "Alice", "age": 25, "city": "New York"}
print(f"Dictionary: {student}")
print(f"student['name']: {student['name']}")
print(f"student['age']: {student['age']}")
print(f"student.get('city'): {student.get('city')}")
print(f"student.get('email', 'Not found'): {student.get('email', 'Not found')}")

print("\n=== MODIFYING DICTIONARY ===")
student = {"name": "Alice", "age": 25}
print(f"Original: {student}")

# Add new key-value pair
student['city'] = "New York"
print(f"After adding city: {student}")

# Update existing value
student['age'] = 26
print(f"After updating age: {student}")

# Using update method
student.update({"email": "alice@example.com", "age": 27})
print(f"After update(): {student}")

print("\n=== REMOVING FROM DICTIONARY ===")
student = {"name": "Alice", "age": 25, "city": "New York", "email": "alice@example.com"}
print(f"Original: {student}")

# pop
removed = student.pop("email")
print(f"After pop('email'): {student}, removed: {removed}")

# popitem
key, value = student.popitem()
print(f"After popitem(): {student}, removed: ({key}, {value})")

# del
del student["city"]
print(f"After del student['city']: {student}")

print("\n=== DICTIONARY METHODS ===")
data = {"a": 1, "b": 2, "c": 3}
print(f"Dictionary: {data}")
print(f"keys(): {list(data.keys())}")
print(f"values(): {list(data.values())}")
print(f"items(): {list(data.items())}")
print(f"len(): {len(data)}")

print("\n=== DICTIONARY ITERATION ===")
student = {"name": "Alice", "age": 25, "city": "New York"}
print(f"Dictionary: {student}")

print("Iterating over keys:")
for key in student:
    print(f"  {key}: {student[key]}")

print("Iterating over items():")
for key, value in student.items():
    print(f"  {key}: {value}")

print("\n=== CHECKING MEMBERSHIP ===")
student = {"name": "Alice", "age": 25, "city": "New York"}
print(f"Dictionary: {student}")
print(f"'name' in student: {'name' in student}")
print(f"'email' in student: {'email' in student}")
print(f"'Alice' in student.values(): {'Alice' in student.values()}")

print("\n=== COPYING DICTIONARY ===")
original = {"a": 1, "b": [2, 3]}
shallow_copy = original.copy()
original["a"] = 99
original["b"].append(4)
print(f"Original: {original}")
print(f"Shallow copy: {shallow_copy}")
print("Note: nested objects are not deeply copied")

import copy
deep_copy = copy.deepcopy(original)
original["b"].append(5)
print(f"After adding to original['b']: {original}")
print(f"Deep copy unchanged: {deep_copy}")

print("\n=== DICTIONARY COMPREHENSION ===")
# Creating from range
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares dict: {squares}")

# Creating from list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_from_pairs = {key: value for key, value in pairs}
print(f"From pairs: {dict_from_pairs}")

# With condition
numbers = list(range(1, 11))
even_squares = {n: n**2 for n in numbers if n % 2 == 0}
print(f"Even squares 1-10: {even_squares}")

# Swapping keys and values
original_dict = {"a": 1, "b": 2, "c": 3}
swapped = {value: key for key, value in original_dict.items()}
print(f"Original: {original_dict}")
print(f"Swapped: {swapped}")

print("\n=== DEFAULT VALUES ===")
from collections import defaultdict

# Using get() with default
data = {"a": 1, "b": 2}
print(f"data.get('c', 0): {data.get('c', 0)}")

# Using defaultdict
counter = defaultdict(int)
counter["a"] += 1
counter["a"] += 1
counter["b"] += 1
print(f"Default dict (int): {dict(counter)}")

list_dict = defaultdict(list)
list_dict["a"].append(1)
list_dict["a"].append(2)
list_dict["b"].append(3)
print(f"Default dict (list): {dict(list_dict)}")

print("\n=== MERGING DICTIONARIES (Python 3.9+) ===")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2  # Requires Python 3.9+
print(f"dict1: {dict1}")
print(f"dict2: {dict2}")
print(f"Merged (|): {merged}")
