"""
Program 5: String Operations
Demonstrates string slices, immutability, string functions, and methods
"""

text = "Python Programming"

print("=== STRING SLICING ===")
print(f"Original string: {text}")
print(f"text[0]: {text[0]}")
print(f"text[-1]: {text[-1]}")
print(f"text[0:6]: {text[0:6]}")
print(f"text[7:]: {text[7:]}")
print(f"text[::2]: {text[::2]}")  # Every 2nd character
print(f"text[::-1]: {text[::-1]}")  # Reverse

print("\n=== STRING IMMUTABILITY ===")
original = "Hello"
print(f"Original: {original}, ID: {id(original)}")
# Strings are immutable, operations create new strings
modified = original.upper()
print(f"Modified: {modified}, ID: {id(modified)}")
print(f"Are they the same object? {original is modified}")

print("\n=== STRING METHODS - CASE ===")
text = "Hello World"
print(f"Original: {text}")
print(f"upper(): {text.upper()}")
print(f"lower(): {text.lower()}")
print(f"swapcase(): {text.swapcase()}")
print(f"capitalize(): {text.capitalize()}")
print(f"title(): {text.title()}")

print("\n=== STRING METHODS - SEARCH ===")
text = "Python is a powerful language"
print(f"Text: {text}")
print(f"find('powerful'): {text.find('powerful')}")
print(f"count('a'): {text.count('a')}")
print(f"startswith('Python'): {text.startswith('Python')}")
print(f"endswith('language'): {text.endswith('language')}")
print(f"index('is'): {text.index('is')}")

print("\n=== STRING METHODS - MODIFICATION ===")
text = "  Hello World  "
print(f"Original: '{text}'")
print(f"strip(): '{text.strip()}'")
print(f"lstrip(): '{text.lstrip()}'")
print(f"rstrip(): '{text.rstrip()}'")

text = "Python Programming"
print(f"replace('Python', 'Java'): {text.replace('Python', 'Java')}")
print(f"replace('o', '0'): {text.replace('o', '0')}")

print("\n=== STRING METHODS - SPLIT AND JOIN ===")
text = "apple, banana, cherry"
items = text.split(", ")
print(f"Original: {text}")
print(f"split(', '): {items}")

words = ["Hello", "World", "Python"]
joined = " ".join(words)
print(f"List: {words}")
print(f"' '.join(): {joined}")

print("\n=== STRING METHODS - CHECKING ===")
text = "Hello123"
print(f"Text: {text}")
print(f"isalpha(): {text.isalpha()}")
print(f"isdigit(): {text.isdigit()}")
print(f"isalnum(): {text.isalnum()}")

text = "12345"
print(f"Text: {text}")
print(f"isdigit(): {text.isdigit()}")

text = "HELLO"
print(f"Text: {text}")
print(f"isupper(): {text.isupper()}")

text = "hello"
print(f"Text: {text}")
print(f"islower(): {text.islower()}")

print("\n=== STRING FORMATTING ===")
name = "Alice"
age = 30
salary = 50000.50
print(f"f-string: My name is {name}, age {age}, salary ${salary:.2f}")
print("format(): My name is {}, age {}, salary ${:.2f}".format(name, age, salary))
print("%-operator: My name is %s, age %d, salary $%.2f" % (name, age, salary))

print("\n=== STRING METHODS - CENTER, LJUST, RJUST ===")
text = "Python"
print(f"Original: {text}")
print(f"center(15): '{text.center(15)}'")
print(f"ljust(15): '{text.ljust(15)}'")
print(f"rjust(15): '{text.rjust(15)}'")
