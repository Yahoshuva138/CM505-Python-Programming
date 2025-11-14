"""
Program 4: Tuples
Demonstrates tuple creation, assignment, operations, and use as return values
"""

print("=== TUPLE CREATION AND ACCESS ===")
empty_tuple = ()
single_item = (1,)  # Note: comma is required for single item
tuple1 = (1, 2, 3)
tuple2 = ("apple", "banana", "cherry")
tuple3 = (1, "hello", 3.14, True)

print(f"Empty: {empty_tuple}")
print(f"Single item: {single_item}")
print(f"Numbers: {tuple1}")
print(f"Strings: {tuple2}")
print(f"Mixed: {tuple3}")

print("\n=== TUPLE INDEXING AND SLICING ===")
tuple_data = ("a", "b", "c", "d", "e")
print(f"Tuple: {tuple_data}")
print(f"tuple_data[0]: {tuple_data[0]}")
print(f"tuple_data[2]: {tuple_data[2]}")
print(f"tuple_data[-1]: {tuple_data[-1]}")
print(f"tuple_data[1:4]: {tuple_data[1:4]}")
print(f"tuple_data[:3]: {tuple_data[:3]}")
print(f"tuple_data[::2]: {tuple_data[::2]}")

print("\n=== TUPLE IMMUTABILITY ===")
tuple_data = (1, 2, 3)
print(f"Original: {tuple_data}")
try:
    tuple_data[0] = 10  # This will raise an error
except TypeError as e:
    print(f"Error: {e}")
print("Tuples are immutable and cannot be modified")

print("\n=== TUPLE UNPACKING ===")
# Simple unpacking
coordinates = (10, 20)
x, y = coordinates
print(f"Coordinates: {coordinates}")
print(f"x: {x}, y: {y}")

# Unpacking with more values
data = (1, 2, 3, 4, 5)
a, b, *rest = data
print(f"\nData: {data}")
print(f"a: {a}, b: {b}, rest: {rest}")

# Swap variables
p, q = 5, 10
print(f"\nBefore swap: p={p}, q={q}")
p, q = q, p
print(f"After swap: p={p}, q={q}")

print("\n=== TUPLE AS RETURN VALUE ===")
def get_min_max(numbers):
    """Return minimum and maximum as tuple"""
    return (min(numbers), max(numbers))

numbers = [3, 7, 2, 9, 1, 5]
min_val, max_val = get_min_max(numbers)
print(f"Numbers: {numbers}")
print(f"Min: {min_val}, Max: {max_val}")

def divide_and_remainder(dividend, divisor):
    """Return quotient and remainder"""
    return (dividend // divisor, dividend % divisor)

quotient, remainder = divide_and_remainder(17, 5)
print(f"\n17 / 5 = quotient: {quotient}, remainder: {remainder}")

print("\n=== TUPLE METHODS ===")
tuple_data = (1, 2, 3, 2, 4, 2)
print(f"Tuple: {tuple_data}")
print(f"count(2): {tuple_data.count(2)}")
print(f"index(3): {tuple_data.index(3)}")

print("\n=== TUPLE OPERATIONS ===")
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
print(f"tuple1: {tuple1}")
print(f"tuple2: {tuple2}")
print(f"Concatenation: {tuple1 + tuple2}")
print(f"Repetition: {tuple1 * 3}")

print("\n=== CHECKING MEMBERSHIP ===")
tuple_data = (1, 2, 3, 4, 5)
print(f"Tuple: {tuple_data}")
print(f"3 in tuple_data: {3 in tuple_data}")
print(f"10 in tuple_data: {10 in tuple_data}")

print("\n=== CONVERTING BETWEEN TUPLE AND LIST ===")
tuple_data = (1, 2, 3)
list_data = [4, 5, 6]

print(f"Original tuple: {tuple_data}")
converted_to_list = list(tuple_data)
print(f"Converted to list: {converted_to_list}")

print(f"Original list: {list_data}")
converted_to_tuple = tuple(list_data)
print(f"Converted to tuple: {converted_to_tuple}")

print("\n=== TUPLE LENGTH, MIN, MAX ===")
numbers_tuple = (5, 2, 8, 1, 9)
print(f"Tuple: {numbers_tuple}")
print(f"Length: {len(numbers_tuple)}")
print(f"Min: {min(numbers_tuple)}")
print(f"Max: {max(numbers_tuple)}")
print(f"Sum: {sum(numbers_tuple)}")

print("\n=== NAMED TUPLES ===")
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(f"Point: {p}")
print(f"p.x: {p.x}, p.y: {p.y}")
print(f"Accessing by index: p[0]={p[0]}, p[1]={p[1]}")

Person = namedtuple('Person', ['name', 'age', 'city'])
person = Person('Alice', 30, 'New York')
print(f"\nPerson: {person}")
print(f"Name: {person.name}, Age: {person.age}, City: {person.city}")
