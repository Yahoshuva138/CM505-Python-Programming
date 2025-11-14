"""
Program 2: Anonymous Functions (Lambda)
Demonstrates lambda functions and their usage
"""

# Simple lambda function
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple arguments
add = lambda x, y: x + y
print(f"Sum of 3 and 7: {add(3, 7)}")

# Lambda with conditional logic
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(f"5 is: {check_even(5)}")
print(f"10 is: {check_even(10)}")

# Lambda used with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"\nOriginal list: {numbers}")
print(f"Squared list: {squared}")

# Lambda used with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"\nOriginal list: {numbers}")
print(f"Even numbers: {even_numbers}")

# Lambda used with sorted()
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
sorted_by_score = sorted(students, key=lambda x: x[1])
print(f"\nStudents sorted by score: {sorted_by_score}")

# Lambda used with sorted() - reverse
sorted_by_score_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Students sorted by score (descending): {sorted_by_score_desc}")

# Nested lambda
multiply_and_add = lambda x, y: (lambda z: x * y + z)(10)
print(f"\nMultiply 3*4 and add 10: {multiply_and_add(3, 4)}")

# Lambda in a function
def apply_operation(x, y, operation):
    return operation(x, y)

result = apply_operation(10, 5, lambda x, y: x + y)
print(f"Apply add operation on 10, 5: {result}")

result = apply_operation(10, 5, lambda x, y: x * y)
print(f"Apply multiply operation on 10, 5: {result}")

# Lambda with reduce()
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"\nProduct of {numbers}: {product}")

# Lambda to sort complex data
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
sorted_data = sorted(data, key=lambda x: x["age"])
print(f"\nSorted by age: {sorted_data}")
