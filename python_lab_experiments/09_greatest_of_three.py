# Program 9: Conditional Logic - Find Greatest of Three Numbers
# Demonstrating nested if-else and conditional operators

print("=" * 50)
print("Program 9: Find Greatest of Three Numbers")
print("=" * 50)

# Method 1: Using nested if-else
print("\nMethod 1: Using Nested if-else")

def greatest_nested_if(a, b, c):
    """Find greatest using nested if-else"""
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b >= c:
            return b
        else:
            return c

# Test with examples
test_cases = [(10, 20, 15), (50, 30, 40), (100, 100, 50), (7, 8, 9)]
print("Test Cases:")
for a, b, c in test_cases:
    greatest = greatest_nested_if(a, b, c)
    print(f"Numbers: {a}, {b}, {c} → Greatest: {greatest}")

# Method 2: Using max() function
print("\nMethod 2: Using max() Function")
for a, b, c in test_cases:
    greatest = max(a, b, c)
    print(f"Numbers: {a}, {b}, {c} → Greatest: {greatest}")

# Method 3: Using conditional operators (ternary)
print("\nMethod 3: Using Ternary Operators")

def greatest_ternary(a, b, c):
    """Find greatest using ternary operators"""
    return a if (a >= b and a >= c) else (b if b >= c else c)

for a, b, c in test_cases:
    greatest = greatest_ternary(a, b, c)
    print(f"Numbers: {a}, {b}, {c} → Greatest: {greatest}")

# Method 4: User input
print("\nMethod 4: User Input")
try:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    z = float(input("Enter third number: "))
    
    greatest = max(x, y, z)
    print(f"\nNumbers: {x}, {y}, {z}")
    print(f"Greatest: {greatest}")
    
except ValueError:
    print("Please enter valid numbers!")

# Method 5: Display all comparisons
print("\n" + "=" * 50)
print("Method 5: Detailed Comparison")
a, b, c = 15, 25, 20
print(f"\nNumbers: {a}, {b}, {c}")
print(f"{a} > {b}: {a > b}")
print(f"{a} > {c}: {a > c}")
print(f"{b} > {a}: {b > a}")
print(f"{b} > {c}: {b > c}")
print(f"{c} > {a}: {c > a}")
print(f"{c} > {b}: {c > b}")
print(f"\nGreatest: {max(a, b, c)}")
