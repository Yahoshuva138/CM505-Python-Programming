"""
Program 3: List Comprehension
Demonstrates creating lists using comprehension syntax
"""

print("=== SIMPLE LIST COMPREHENSION ===")
# Traditional way
numbers1 = []
for i in range(1, 6):
    numbers1.append(i ** 2)

# Using list comprehension
numbers2 = [i ** 2 for i in range(1, 6)]

print(f"Traditional: {numbers1}")
print(f"Comprehension: {numbers2}")

print("\n=== LIST COMPREHENSION WITH CONDITION ===")
# Filter even numbers
numbers = list(range(1, 11))
even_traditional = []
for n in numbers:
    if n % 2 == 0:
        even_traditional.append(n)

even_comprehension = [n for n in numbers if n % 2 == 0]

print(f"Original: {numbers}")
print(f"Even (traditional): {even_traditional}")
print(f"Even (comprehension): {even_comprehension}")

print("\n=== LIST COMPREHENSION WITH STRING ===")
text = "Python"
chars = [char.upper() for char in text]
print(f"Text: {text}")
print(f"Uppercase chars: {chars}")

print("\n=== LIST COMPREHENSION WITH MULTIPLE CONDITIONS ===")
numbers = list(range(1, 21))
# Numbers divisible by 2 or 3
result = [n for n in numbers if n % 2 == 0 or n % 3 == 0]
print(f"Numbers from 1-20 divisible by 2 or 3: {result}")

print("\n=== NESTED LIST COMPREHENSION ===")
# Create multiplication table
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("Multiplication table 3x3:")
for row in table:
    print(row)

# Flatten nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested for item in sublist]
print(f"\nNested: {nested}")
print(f"Flattened: {flattened}")

print("\n=== LIST COMPREHENSION WITH TUPLE UNPACKING ===")
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers = [num for num, _ in pairs]
letters = [letter for _, letter in pairs]
print(f"Pairs: {pairs}")
print(f"Numbers: {numbers}")
print(f"Letters: {letters}")

print("\n=== LIST COMPREHENSION VS MAP/FILTER ===")
numbers = list(range(1, 11))

# Using map and filter
even_squared_mapfilter = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

# Using list comprehension
even_squared_comp = [x ** 2 for x in numbers if x % 2 == 0]

print(f"Using map/filter: {even_squared_mapfilter}")
print(f"Using comprehension: {even_squared_comp}")
print("List comprehension is usually more readable")

print("\n=== DICTIONARY COMPREHENSION (BONUS) ===")
words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}
print(f"Words: {words}")
print(f"Word lengths (dict comprehension): {word_lengths}")

# From list of pairs to dictionary
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_from_pairs = {key: value for key, value in pairs}
print(f"Pairs: {pairs}")
print(f"Dictionary: {dict_from_pairs}")

print("\n=== SET COMPREHENSION (BONUS) ===")
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_squared = {x ** 2 for x in numbers}
print(f"Numbers (with duplicates): {numbers}")
print(f"Unique squared (set comprehension): {unique_squared}")

print("\n=== COMPLEX LIST COMPREHENSION EXAMPLE ===")
# Generate list of complex numbers
complex_nums = [complex(real=x, imag=y) 
                for x in range(1, 3) 
                for y in range(1, 3)]
print(f"Complex numbers: {complex_nums}")

# List all combinations
from itertools import product
items = ["A", "B"]
numbers_range = [1, 2]
combinations = [(item, num) for item in items for num in numbers_range]
print(f"Combinations: {combinations}")
