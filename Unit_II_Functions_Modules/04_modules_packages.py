"""
Program 4: Modules and Packages
Demonstrates creation and importing of modules, and using Python packages
"""

# Importing standard library modules
import math
import random
import datetime

print("=== Using Math Module ===")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi value: {math.pi}")
print(f"Factorial of 5: {math.factorial(5)}")
print(f"ceil(4.3): {math.ceil(4.3)}")
print(f"floor(4.7): {math.floor(4.7)}")

print("\n=== Using Random Module ===")
print(f"Random float: {random.random()}")
print(f"Random integer (1-100): {random.randint(1, 100)}")
print(f"Random choice from list: {random.choice(['apple', 'banana', 'cherry'])}")

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")

print("\n=== Using Datetime Module ===")
now = datetime.datetime.now()
print(f"Current date and time: {now}")
print(f"Current year: {now.year}")
print(f"Current month: {now.month}")
print(f"Current day: {now.day}")

# Creating a date
d = datetime.date(2024, 12, 25)
print(f"Christmas 2024: {d}")

print("\n=== Importing Specific Items ===")
from math import pi, sqrt
print(f"Pi: {pi}")
print(f"Square root of 25: {sqrt(25)}")

print("\n=== Using Aliases ===")
import json as js
data = {"name": "Alice", "age": 30}
json_string = js.dumps(data)
print(f"JSON string: {json_string}")

print("\n=== Importing All from Module ===")
from statistics import mean, median, stdev
numbers = [10, 20, 30, 40, 50]
print(f"Numbers: {numbers}")
print(f"Mean: {mean(numbers)}")
print(f"Median: {median(numbers)}")
print(f"Std Dev: {stdev(numbers)}")

print("\n=== Module Information ===")
print(f"Math module file: {math.__file__}")
print(f"Math module attributes: {dir(math)[:5]}...")  # Show first 5

print("\n=== Collections Module ===")
from collections import Counter, defaultdict
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print(f"Word count: {word_count}")

print("\n=== Itertools Module ===")
from itertools import combinations, permutations
items = [1, 2, 3]
print(f"Combinations of {items}: {list(combinations(items, 2))}")
print(f"Permutations of [1,2]: {list(permutations([1, 2]))}")
