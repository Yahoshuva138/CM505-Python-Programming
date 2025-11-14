"""
Program 6: Arrays and Array Methods
Demonstrates accessing elements and using array methods
"""

# Note: Python doesn't have native arrays like other languages
# We'll use lists which are Python's version of arrays

print("=== LIST CREATION ===")
empty_list = []
number_list = [1, 2, 3, 4, 5]
mixed_list = [1, "Hello", 3.14, True, None]
nested_list = [[1, 2], [3, 4], [5, 6]]

print(f"Empty list: {empty_list}")
print(f"Number list: {number_list}")
print(f"Mixed list: {mixed_list}")
print(f"Nested list: {nested_list}")

print("\n=== ACCESSING ELEMENTS ===")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"List: {fruits}")
print(f"fruits[0]: {fruits[0]}")
print(f"fruits[2]: {fruits[2]}")
print(f"fruits[-1]: {fruits[-1]}")
print(f"fruits[-2]: {fruits[-2]}")

print("\n=== SLICING ===")
print(f"fruits[1:4]: {fruits[1:4]}")
print(f"fruits[:3]: {fruits[:3]}")
print(f"fruits[2:]: {fruits[2:]}")
print(f"fruits[::2]: {fruits[::2]}")
print(f"fruits[::-1]: {fruits[::-1]}")

print("\n=== LIST METHODS - MODIFICATION ===")
numbers = [1, 2, 3]
print(f"Original: {numbers}")
numbers.append(4)
print(f"After append(4): {numbers}")
numbers.extend([5, 6])
print(f"After extend([5, 6]): {numbers}")
numbers.insert(0, 0)
print(f"After insert(0, 0): {numbers}")

print("\n=== LIST METHODS - REMOVAL ===")
numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")
numbers.remove(3)
print(f"After remove(3): {numbers}")
popped = numbers.pop()
print(f"After pop(): {numbers}, popped value: {popped}")
popped_at_index = numbers.pop(0)
print(f"After pop(0): {numbers}, popped value: {popped_at_index}")

print("\n=== LIST METHODS - SEARCHING ===")
numbers = [1, 2, 3, 4, 5, 2]
print(f"List: {numbers}")
print(f"count(2): {numbers.count(2)}")
print(f"index(4): {numbers.index(4)}")
print(f"2 in numbers: {2 in numbers}")
print(f"10 in numbers: {10 in numbers}")

print("\n=== LIST METHODS - SORTING ===")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")
sorted_asc = sorted(numbers)
print(f"sorted(): {sorted_asc}")
sorted_desc = sorted(numbers, reverse=True)
print(f"sorted(reverse=True): {sorted_desc}")

numbers_copy = numbers.copy()
numbers_copy.sort()
print(f"After sort(): {numbers_copy}")

print("\n=== LIST METHODS - OTHER OPERATIONS ===")
numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")
numbers.reverse()
print(f"After reverse(): {numbers}")

print(f"len(numbers): {len(numbers)}")
print(f"min(numbers): {min(numbers)}")
print(f"max(numbers): {max(numbers)}")
print(f"sum(numbers): {sum(numbers)}")

print("\n=== LIST COPY (ALIASING vs CLONING) ===")
original = [1, 2, 3]
alias = original  # Aliasing - points to same list
clone = original.copy()  # Cloning - creates new list

print(f"Original: {original}, ID: {id(original)}")
print(f"Alias: {alias}, ID: {id(alias)}")
print(f"Clone: {clone}, ID: {id(clone)}")

original.append(4)
print(f"\nAfter original.append(4):")
print(f"Original: {original}")
print(f"Alias: {alias}")
print(f"Clone: {clone}")

print("\n=== USING ARRAY MODULE (Python's actual array) ===")
import array
arr = array.array('i', [1, 2, 3, 4, 5])
print(f"Array: {arr}")
print(f"Array[0]: {arr[0]}")
arr.append(6)
print(f"After append(6): {arr}")
arr.extend([7, 8])
print(f"After extend([7, 8]): {arr}")
