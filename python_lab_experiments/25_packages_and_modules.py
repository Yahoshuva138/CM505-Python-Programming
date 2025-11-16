# Program 25: Create a Package and Access It
# Demonstrating Python packages and modules

print("=" * 50)
print("Program 25: Python Packages and Modules")
print("=" * 50)

print("\nUnderstanding Packages and Modules:")
print("- Module: A Python file (.py)")
print("- Package: A directory containing modules and __init__.py")
print("- Package is a way of organizing related modules into a directory hierarchy")

# Method 1: Import built-in modules
print("\n" + "=" * 50)
print("Method 1: Import Built-in Modules")

import math
import statistics
import datetime

print(f"\nUsing 'math' module:")
print(f"  π (pi) = {math.pi}")
print(f"  sqrt(16) = {math.sqrt(16)}")
print(f"  sin(π/2) = {math.sin(math.pi/2)}")

print(f"\nUsing 'statistics' module:")
data = [10, 20, 30, 40, 50]
print(f"  Data: {data}")
print(f"  Mean: {statistics.mean(data)}")
print(f"  Median: {statistics.median(data)}")

print(f"\nUsing 'datetime' module:")
now = datetime.datetime.now()
print(f"  Current date and time: {now}")

# Method 2: Import specific items from module
print("\nMethod 2: Import Specific Items")

from math import pi, sqrt, sin
from statistics import mean, median

print(f"Using 'from math import':")
print(f"  pi = {pi}")
print(f"  sqrt(25) = {sqrt(25)}")

# Method 3: List module contents
print("\n" + "=" * 50)
print("Method 3: List Module Contents")

import sys
print(f"Items in 'sys' module (sample):")
sys_items = dir(sys)
for i, item in enumerate(sys_items[:10]):
    print(f"  {i+1}. {item}")
print(f"  ... and {len(sys_items)-10} more items")

# Method 4: Create custom modules demonstration
print("\nMethod 4: Creating Custom Module Concept")
print("""
To create a custom module:
1. Create a Python file (e.g., mymodule.py)
2. Define functions/classes in it
3. Import using: import mymodule or from mymodule import function

To create a package:
1. Create a directory (e.g., mypackage)
2. Create __init__.py inside it (can be empty)
3. Create module files inside the directory
4. Import using: from mypackage import module or from mypackage.module import function
""")

# Method 5: Demonstrate package structure
print("\n" + "=" * 50)
print("Method 5: Package Structure Example")
print("""
mypackage/
    __init__.py
    math_operations.py
    string_operations.py
    file_operations.py
    utils.py

File: mypackage/__init__.py
(Can contain package initialization code)

File: mypackage/math_operations.py
def add(a, b):
    return a + b
def multiply(a, b):
    return a * b

Usage:
from mypackage.math_operations import add, multiply
result = add(5, 3)
""")

# Method 6: Create simple module simulation
print("\nMethod 6: Simple Module Simulation")

class MathOperations:
    """A class simulating a module for math operations"""
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

class StringOperations:
    """A class simulating a module for string operations"""
    
    @staticmethod
    def reverse(s):
        return s[::-1]
    
    @staticmethod
    def uppercase(s):
        return s.upper()
    
    @staticmethod
    def count_vowels(s):
        vowels = 'aeiouAEIOU'
        return sum(1 for char in s if char in vowels)

# Using the "modules"
print("Using MathOperations 'module':")
print(f"  add(10, 20) = {MathOperations.add(10, 20)}")
print(f"  multiply(5, 4) = {MathOperations.multiply(5, 4)}")
print(f"  divide(20, 4) = {MathOperations.divide(20, 4)}")

print("\nUsing StringOperations 'module':")
text = "Hello World"
print(f"  reverse('{text}') = {StringOperations.reverse(text)}")
print(f"  uppercase('{text}') = {StringOperations.uppercase(text)}")
print(f"  count_vowels('{text}') = {StringOperations.count_vowels(text)}")

# Method 7: List installed packages
print("\n" + "=" * 50)
print("Method 7: Show Python Path and Modules")

import sys
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"\nPython path (first 3 entries):")
for i, path in enumerate(sys.path[:3]):
    print(f"  {i+1}. {path}")

# Method 8: Check module information
print("\nMethod 8: Module Information")

import os
print(f"\n'os' module:")
print(f"  Location: {os.__file__}")
print(f"  Docstring (first 200 chars): {os.__doc__[:200]}...")

# Method 9: Demonstrate __name__ variable
print("\n" + "=" * 50)
print("Method 9: __name__ Variable")

print(f"Current script __name__: {__name__}")
print(f"Value is '__main__' when run directly")
print(f"Value is 'module_name' when imported")

# Method 10: Package and module best practices
print("\nMethod 10: Best Practices")
print("""
Package Organization Best Practices:
1. Use meaningful names (lowercase, underscore for multi-word)
2. Always include __init__.py in packages
3. Use logical grouping of modules
4. Document modules and packages
5. Use relative imports within packages
6. Keep modules focused on single responsibility

Example structure:
dataprocessing/
    __init__.py
    core/
        __init__.py
        parser.py
        validator.py
    utils/
        __init__.py
        helpers.py
        formatters.py
    tests/
        __init__.py
        test_parser.py
""")

print("\n" + "=" * 50)
print("Program completed!")
