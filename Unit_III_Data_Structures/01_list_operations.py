"""
Program 1: List Operations and Methods
Demonstrates basic list operations, slicing, and methods
"""

print("=== CREATING AND ACCESSING LISTS ===")
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")

print("\n=== LIST INDEXING ===")
print(f"fruits[0]: {fruits[0]}")
print(f"fruits[2]: {fruits[2]}")
print(f"fruits[-1]: {fruits[-1]}")
print(f"fruits[-2]: {fruits[-2]}")

print("\n=== LIST SLICING ===")
print(f"fruits[1:3]: {fruits[1:3]}")
print(f"fruits[:2]: {fruits[:2]}")
print(f"fruits[1:]: {fruits[1:]}")
print(f"fruits[::2]: {fruits[::2]}")
print(f"fruits[::-1]: {fruits[::-1]}")

print("\n=== LIST MODIFICATION ===")
numbers = [1, 2, 3]
print(f"Original: {numbers}")
numbers[0] = 10
print(f"After numbers[0] = 10: {numbers}")
numbers[1:3] = [20, 30]
print(f"After numbers[1:3] = [20, 30]: {numbers}")

print("\n=== LIST CONCATENATION AND REPETITION ===")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated = list1 + list2
print(f"list1 + list2: {concatenated}")
repeated = [1, 2] * 3
print(f"[1, 2] * 3: {repeated}")

print("\n=== LIST METHODS ===")
numbers = [3, 1, 4, 1, 5, 9]
print(f"Original: {numbers}")

# append
numbers_copy = numbers.copy()
numbers_copy.append(2)
print(f"After append(2): {numbers_copy}")

# extend
numbers_copy = numbers.copy()
numbers_copy.extend([6, 7])
print(f"After extend([6, 7]): {numbers_copy}")

# insert
numbers_copy = numbers.copy()
numbers_copy.insert(0, 0)
print(f"After insert(0, 0): {numbers_copy}")

# remove
numbers_copy = numbers.copy()
numbers_copy.remove(1)
print(f"After remove(1): {numbers_copy}")

# pop
numbers_copy = numbers.copy()
popped = numbers_copy.pop()
print(f"After pop(): {numbers_copy}, popped: {popped}")

# index and count
print(f"index(1): {numbers.index(1)}")
print(f"count(1): {numbers.count(1)}")

# sort and reverse
numbers_copy = numbers.copy()
numbers_copy.sort()
print(f"After sort(): {numbers_copy}")
numbers_copy.reverse()
print(f"After reverse(): {numbers_copy}")

# clear
numbers_copy = [1, 2, 3]
numbers_copy.clear()
print(f"After clear(): {numbers_copy}")

print("\n=== CHECKING MEMBERSHIP ===")
numbers = [1, 2, 3, 4, 5]
print(f"List: {numbers}")
print(f"3 in numbers: {3 in numbers}")
print(f"10 in numbers: {10 in numbers}")
print(f"2 not in numbers: {2 not in numbers}")

print("\n=== LIST LENGTH, MIN, MAX, SUM ===")
numbers = [5, 2, 8, 1, 9, 3]
print(f"List: {numbers}")
print(f"len(): {len(numbers)}")
print(f"min(): {min(numbers)}")
print(f"max(): {max(numbers)}")
print(f"sum(): {sum(numbers)}")

print("\n=== SORTING WITH CUSTOM ORDER ===")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")
print(f"sorted(): {sorted(numbers)}")
print(f"sorted(reverse=True): {sorted(numbers, reverse=True)}")

students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
print(f"Students: {students}")
print(f"Sorted by score: {sorted(students, key=lambda x: x[1])}")
