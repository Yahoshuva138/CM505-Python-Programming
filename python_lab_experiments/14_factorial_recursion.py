# Program 14: Recursion - Factorial
# Demonstrating recursive functions

print("=" * 50)
print("Program 14: Factorial using Recursion")
print("=" * 50)

# Recursive factorial function
def factorial_recursive(n):
    """
    Calculate factorial using recursion
    Base case: n = 0 or n = 1 returns 1
    Recursive case: n! = n × (n-1)!
    """
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial_recursive(n - 1)

# Function to show recursion steps
def factorial_recursive_steps(n, indent=0):
    """Show recursion steps"""
    prefix = "  " * indent
    print(f"{prefix}factorial({n})", end="")
    
    if n <= 1:
        print(f" = 1")
        return 1
    else:
        print()
        result = n * factorial_recursive_steps(n - 1, indent + 1)
        print(f"{prefix}factorial({n}) = {n} × {result // n} = {result}")
        return result

# Method 1: Simple recursive calls
print("\nMethod 1: Simple Recursive Calls")
numbers = [0, 1, 5, 7, 10]
for num in numbers:
    result = factorial_recursive(num)
    print(f"{num}! = {result}")

# Method 2: Show recursion steps
print("\n" + "=" * 50)
print("Method 2: Show Recursion Steps")

for num in [4, 5]:
    print(f"\nCalculating {num}!:")
    result = factorial_recursive_steps(num)
    print(f"Result: {num}! = {result}\n")

# Method 3: Compare with iterative
print("=" * 50)
print("Method 3: Compare Recursive vs Iterative")

def factorial_iterative(n):
    """Calculate factorial iteratively"""
    if n < 0:
        return "Error"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("\n{'Number':<10} {'Recursive':<15} {'Iterative':<15}")
print("-" * 40)
for num in range(0, 11):
    rec = factorial_recursive(num)
    itr = factorial_iterative(num)
    print(f"{num:<10} {rec:<15} {itr:<15}")

# Method 4: User input
print("\n" + "=" * 50)
print("Method 4: User Input")

try:
    user_num = int(input("Enter a number (0-12) for factorial: "))
    if user_num < 0:
        print("Factorial not defined for negative numbers!")
    elif user_num > 12:
        print("Number too large (for demonstration, keep it ≤ 12)")
    else:
        result = factorial_recursive(user_num)
        print(f"{user_num}! = {result}")
        
        # Show steps for small numbers
        if user_num <= 6:
            print("\nRecursion steps:")
            factorial_recursive_steps(user_num)
except ValueError:
    print("Please enter a valid integer!")

# Method 5: Recursion depth explanation
print("\n" + "=" * 50)
print("Method 5: Understanding Recursion")
print("\nFor factorial(5):")
print("factorial(5) = 5 × factorial(4)")
print("            = 5 × 4 × factorial(3)")
print("            = 5 × 4 × 3 × factorial(2)")
print("            = 5 × 4 × 3 × 2 × factorial(1)")
print("            = 5 × 4 × 3 × 2 × 1")
print("            = 120")
