# Program 11: Loops - Multiplication Table
# Demonstrating for loops with nested loops

print("=" * 50)
print("Program 11: Multiplication Table (1-10)")
print("=" * 50)

# Method 1: Multiplication table for a single number
print("\nMethod 1: Single Number Multiplication Table")

def print_multiplication_table(num, limit=10):
    """Print multiplication table for a number"""
    print(f"\nMultiplication table of {num}:")
    print(f"{num} × 1 = {num * 1}")
    for i in range(2, limit + 1):
        print(f"{num} × {i} = {num * i}")

for number in [3, 7]:
    print_multiplication_table(number)

# Method 2: Multiplication tables for numbers 1-5
print("\n" + "=" * 50)
print("Method 2: Multiplication Tables for Numbers 1-5")

print("\nNested loops approach:")
for num in range(1, 6):
    print(f"\n--- Table of {num} ---")
    for i in range(1, 11):
        print(f"{num} × {i} = {num * i}", end="    ")
    print()  # New line

# Method 3: Formatted table display
print("\n" + "=" * 50)
print("Method 3: Formatted Table Display (Numbers 1-5)")

for num in range(1, 6):
    print(f"\nTable of {num}:")
    print(f"{'Multiplier':<12} {'Result':<12}")
    print("-" * 24)
    for i in range(1, 11):
        result = num * i
        print(f"{num} × {i:<8} {result:<12}")

# Method 4: User input for single table
print("\n" + "=" * 50)
print("Method 4: User Input")
try:
    user_num = int(input("Enter a number for multiplication table: "))
    limit = int(input("Enter the limit (default 10): ") or 10)
    
    print(f"\nMultiplication table of {user_num} up to {limit}:")
    for i in range(1, limit + 1):
        print(f"{user_num} × {i} = {user_num * i}")
except ValueError:
    print("Please enter valid integers!")

# Method 5: Formatted grid (all tables at once)
print("\n" + "=" * 50)
print("Method 5: All Tables in Grid Format (1-5)")
print(f"{'1':<5} {'2':<5} {'3':<5} {'4':<5} {'5':<5}")
print("-" * 25)
for i in range(1, 11):
    for num in range(1, 6):
        result = num * i
        print(f"{result:<5}", end="")
    print()
