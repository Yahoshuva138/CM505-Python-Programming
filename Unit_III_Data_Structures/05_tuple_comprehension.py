"""
Program 5: Tuple Comprehension
Demonstrates creating tuples using comprehension syntax
"""

print("=== TUPLE COMPREHENSION ===")
# Create tuple using generator expression
numbers1 = tuple(i ** 2 for i in range(1, 6))
print(f"Squares (1-5): {numbers1}")

# Traditional way with list then conversion
numbers2_list = [i ** 2 for i in range(1, 6)]
numbers2 = tuple(numbers2_list)
print(f"Using list then convert: {numbers2}")

print("\n=== TUPLE COMPREHENSION WITH CONDITIONS ===")
numbers = list(range(1, 11))
even_tuple = tuple(n for n in numbers if n % 2 == 0)
print(f"Numbers: {numbers}")
print(f"Even numbers: {even_tuple}")

print("\n=== NESTED TUPLE COMPREHENSION ===")
# Create nested tuples
matrix = tuple(tuple(i * j for j in range(1, 4)) for i in range(1, 4))
print("Multiplication table as nested tuples:")
for row in matrix:
    print(row)

print("\n=== TUPLE COMPREHENSION WITH STRING ===")
text = "Python"
char_tuples = tuple((char, ord(char)) for char in text)
print(f"Text: {text}")
print(f"Char with ASCII: {char_tuples}")

print("\n=== FILTERING IN TUPLE COMPREHENSION ===")
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = tuple(word for word in words if len(word) > 5)
print(f"Words: {words}")
print(f"Long words (>5 chars): {long_words}")

print("\n=== MULTIPLE GENERATORS IN TUPLE COMPREHENSION ===")
# Cartesian product
colors = ["red", "blue"]
sizes = ["S", "M", "L"]
combinations = tuple((color, size) for color in colors for size in sizes)
print(f"Colors: {colors}")
print(f"Sizes: {sizes}")
print(f"Combinations: {combinations}")

print("\n=== TRANSFORMING AND FILTERING ===")
numbers = range(1, 21)
# Even numbers squared
result = tuple(x ** 2 for x in numbers if x % 2 == 0)
print(f"Even numbers from 1-20 squared: {result}")

# Numbers divisible by 3 or 5
result2 = tuple(x for x in numbers if x % 3 == 0 or x % 5 == 0)
print(f"Numbers divisible by 3 or 5: {result2}")

print("\n=== UNPACKING FROM TUPLE COMPREHENSION ===")
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers_tuple = tuple(num for num, _ in pairs)
letters_tuple = tuple(letter for _, letter in pairs)
print(f"Pairs: {pairs}")
print(f"Numbers: {numbers_tuple}")
print(f"Letters: {letters_tuple}")

print("\n=== PERFORMANCE: TUPLE VS LIST COMPREHENSION ===")
import timeit

# Time list comprehension
list_time = timeit.timeit(lambda: [i ** 2 for i in range(1000)], number=10000)
print(f"List comprehension (10k times): {list_time:.4f}s")

# Time tuple comprehension
tuple_time = timeit.timeit(lambda: tuple(i ** 2 for i in range(1000)), number=10000)
print(f"Tuple comprehension (10k times): {tuple_time:.4f}s")

print("\n=== COMPLEX TUPLE COMPREHENSION ===")
# Create tuples of (number, square, cube)
result = tuple((n, n**2, n**3) for n in range(1, 6))
print("(n, n², n³):")
for item in result:
    print(item)

# Create tuple of coordinates
points = tuple((x, y) for x in range(1, 4) for y in range(1, 3))
print(f"\nCoordinates: {points}")

print("\n=== TUPLE COMPREHENSION WITH FUNCTION ===")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = tuple(n for n in range(2, 20) if is_prime(n))
print(f"Prime numbers 2-19: {primes}")
