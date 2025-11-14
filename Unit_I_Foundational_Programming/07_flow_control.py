"""
Program 7: Flow Control
Demonstrates break, continue, and pass statements
"""

print("=== BREAK STATEMENT ===")
print("Loop with break (exits at 3):")
for i in range(1, 10):
    if i == 3:
        print(f"Breaking at {i}")
        break
    print(i, end=" ")
print("\n")

print("=== BREAK STATEMENT - Finding number in list ===")
numbers = [2, 4, 6, 8, 10, 12]
search_num = 8
for num in numbers:
    if num == search_num:
        print(f"Found {search_num}!")
        break
    print(f"Checking {num}")

print("\n=== CONTINUE STATEMENT ===")
print("Loop with continue (skips odd numbers):")
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i, end=" ")
print("\n")

print("=== CONTINUE STATEMENT - Skip vowels ===")
text = "hello"
print(f"Characters (skipping vowels): ", end="")
for char in text:
    if char in "aeiouAEIOU":
        continue
    print(char, end=" ")
print("\n")

print("=== PASS STATEMENT ===")
print("Using pass as placeholder:")
for i in range(1, 4):
    if i == 2:
        pass  # Do nothing here
    else:
        print(f"Processing {i}")

print("\n=== PASS in empty function ===")
def dummy_function():
    """
    This is a function that does nothing yet.
    Pass is used as a placeholder.
    """
    pass

dummy_function()
print("Dummy function executed (does nothing)")

print("\n=== PASS in empty class ===")
class EmptyClass:
    pass

obj = EmptyClass()
print("Empty class instantiated successfully")

print("\n=== NESTED LOOPS WITH BREAK ===")
print("Breaking from nested loop:")
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(f"({i},{j})", end=" ")
    print()

print("\n=== WHILE-ELSE and FOR-ELSE ===")
print("For-else (else executes when loop completes):")
for i in range(1, 4):
    print(i, end=" ")
else:
    print("\nLoop completed successfully!")

print("\nFor-else with break (else is skipped):")
for i in range(1, 5):
    if i == 3:
        print(f"\nBreak at {i}")
        break
    print(i, end=" ")
else:
    print("This won't execute")
