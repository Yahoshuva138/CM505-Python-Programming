"""
Program 7: Map, Reduce, and Filter
Demonstrates functional programming concepts
"""

from functools import reduce

print("=== MAP FUNCTION ===")
numbers = [1, 2, 3, 4, 5]

# Using map with lambda
squared = list(map(lambda x: x ** 2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared}")

# Using map with regular function
def double(x):
    return x * 2

doubled = list(map(double, numbers))
print(f"Doubled: {doubled}")

# Map with multiple iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sums = list(map(lambda x, y: x + y, list1, list2))
print(f"List1: {list1}, List2: {list2}")
print(f"Sums: {sums}")

# Map with strings
strings = ["hello", "world", "python"]
uppercase = list(map(str.upper, strings))
print(f"Original: {strings}")
print(f"Uppercase: {uppercase}")

print("\n=== FILTER FUNCTION ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter with lambda
even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Original: {numbers}")
print(f"Even numbers: {even}")

# Using filter with regular function
def is_positive(x):
    return x > 0

positive = list(filter(is_positive, numbers))
print(f"Positive numbers: {positive}")

# Filter with strings
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = list(filter(lambda x: len(x) > 5, words))
print(f"Words: {words}")
print(f"Words with length > 5: {long_words}")

print("\n=== REDUCE FUNCTION ===")
numbers = [1, 2, 3, 4, 5]

# Sum using reduce
total = reduce(lambda x, y: x + y, numbers)
print(f"Numbers: {numbers}")
print(f"Sum using reduce: {total}")

# Product using reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"Product using reduce: {product}")

# Finding maximum using reduce
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum using reduce: {maximum}")

# String concatenation using reduce
strings = ["Hello", "World", "Python", "Programming"]
concatenated = reduce(lambda x, y: x + " " + y, strings)
print(f"Strings: {strings}")
print(f"Concatenated: {concatenated}")

print("\n=== COMBINING MAP, FILTER, REDUCE ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original: {numbers}")

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Map to square
squared_evens = list(map(lambda x: x ** 2, evens))
print(f"Squared evens: {squared_evens}")

# Reduce to sum
result = reduce(lambda x, y: x + y, squared_evens)
print(f"Sum of squared evens: {result}")

# All in one line using composition
final_result = reduce(lambda x, y: x + y, 
                      map(lambda x: x ** 2, 
                          filter(lambda x: x % 2 == 0, numbers)))
print(f"Final result (all in one): {final_result}")

print("\n=== USING LIST COMPREHENSION (Alternative to map/filter) ===")
# List comprehension is often more Pythonic than map/filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Instead of map
squared_comp = [x ** 2 for x in numbers]
print(f"Squared (comprehension): {squared_comp}")

# Instead of filter
evens_comp = [x for x in numbers if x % 2 == 0]
print(f"Even (comprehension): {evens_comp}")

# Combining filter and map
squared_evens_comp = [x ** 2 for x in numbers if x % 2 == 0]
print(f"Squared evens (comprehension): {squared_evens_comp}")
