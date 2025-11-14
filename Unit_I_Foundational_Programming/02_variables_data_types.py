"""
Program 2: Declaration, initialization, and usage of variables and data types
Demonstrates Int, Float, Boolean, String, and List data types
"""

# Integer
age = 25
print(f"Age (Integer): {age}, Type: {type(age)}")

# Float
height = 5.9
print(f"Height (Float): {height}, Type: {type(height)}")

# Boolean
is_student = True
print(f"Is Student (Boolean): {is_student}, Type: {type(is_student)}")

# String
name = "John Doe"
print(f"Name (String): {name}, Type: {type(name)}")

# List
fruits = ["apple", "banana", "cherry"]
print(f"Fruits (List): {fruits}, Type: {type(fruits)}")

# Multiple variable assignment
x, y, z = 10, 20, 30
print(f"\nMultiple Assignment - x: {x}, y: {y}, z: {z}")

# Dynamic typing - changing variable type
value = 100
print(f"\nValue: {value}, Type: {type(value)}")
value = "Now a string"
print(f"Value: {value}, Type: {type(value)}")
