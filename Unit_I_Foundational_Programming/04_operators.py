"""
Program 4: Operators
Demonstrates Arithmetic, Comparison, Assignment, Logical, Bitwise, 
Membership, and Identity operators
"""

print("=== ARITHMETIC OPERATORS ===")
a, b = 20, 10
print(f"a = {a}, b = {b}")
print(f"Addition: a + b = {a + b}")
print(f"Subtraction: a - b = {a - b}")
print(f"Multiplication: a * b = {a * b}")
print(f"Division: a / b = {a / b}")
print(f"Floor Division: a // b = {a // b}")
print(f"Modulo: a % b = {a % b}")
print(f"Exponentiation: a ** b = {a ** b}")

print("\n=== COMPARISON/RELATIONAL OPERATORS ===")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}")

print("\n=== ASSIGNMENT OPERATORS ===")
x = 5
print(f"x = {x}")
x += 3
print(f"x += 3: x = {x}")
x -= 2
print(f"x -= 2: x = {x}")
x *= 2
print(f"x *= 2: x = {x}")
x //= 3
print(f"x //= 3: x = {x}")

print("\n=== LOGICAL OPERATORS ===")
p, q = True, False
print(f"p = {p}, q = {q}")
print(f"p and q: {p and q}")
print(f"p or q: {p or q}")
print(f"not p: {not p}")

print("\n=== BITWISE OPERATORS ===")
m, n = 12, 10  # 12 = 1100, 10 = 1010
print(f"m = {m} (binary: {bin(m)}), n = {n} (binary: {bin(n)})")
print(f"m & n (AND): {m & n} (binary: {bin(m & n)})")
print(f"m | n (OR): {m | n} (binary: {bin(m | n)})")
print(f"m ^ n (XOR): {m ^ n} (binary: {bin(m ^ n)})")
print(f"~m (NOT): {~m}")
print(f"m << 2 (Left Shift): {m << 2}")
print(f"m >> 2 (Right Shift): {m >> 2}")

print("\n=== MEMBERSHIP OPERATORS ===")
fruits_list = ["apple", "banana", "cherry"]
print(f"List: {fruits_list}")
print(f"'apple' in fruits_list: {'apple' in fruits_list}")
print(f"'orange' in fruits_list: {'orange' in fruits_list}")
print(f"'banana' not in fruits_list: {'banana' not in fruits_list}")

print("\n=== IDENTITY OPERATORS ===")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"list1 = {list1}, list2 = {list2}, list3 = list1")
print(f"list1 is list2: {list1 is list2}")
print(f"list1 is list3: {list1 is list3}")
print(f"list1 == list2: {list1 == list2}")
print(f"list1 is not list2: {list1 is not list2}")
