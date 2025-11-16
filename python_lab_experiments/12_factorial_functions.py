# Program 12: Functions - Factorial Calculation
# Demonstrating function definition and calls

print("=" * 50)
print("Program 12: Factorial using Functions")
print("=" * 50)

# Function definition
def calculate_factorial(n):
    """
    Calculate factorial of a number
    Args:
        n: Integer number
    Returns:
        Factorial value if valid, -1 if invalid
    """
    if n < 0:
        print("Error: Factorial not defined for negative numbers")
        return -1
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result

# Function with detailed output
def factorial_with_display(n):
    """Display factorial calculation with steps"""
    if n < 0:
        print("Error: Factorial not defined for negative numbers")
        return
    
    result = calculate_factorial(n)
    if result == -1:
        return
    
    print(f"\n{n}! = {result}")

# Method 1: Direct function calls
print("\nMethod 1: Direct Function Calls")
numbers = [0, 1, 5, 6, 10]
for num in numbers:
    fact = calculate_factorial(num)
    print(f"{num}! = {fact}")

# Method 2: Using function with display
print("\nMethod 2: Function with Display")
for num in [3, 4, 7]:
    factorial_with_display(num)

# Method 3: Storing results in a list
print("\nMethod 3: Store Results in List")
results = []
for num in range(0, 6):
    fact = calculate_factorial(num)
    results.append(fact)

print("Factorials 0! to 5!:")
for i, fact in enumerate(results):
    print(f"{i}! = {fact}")

# Method 4: User input with error handling
print("\n" + "=" * 50)
print("Method 4: User Input with Error Handling")

def get_factorial_from_user():
    """Get factorial from user with validation"""
    try:
        num = int(input("Enter a number: "))
        result = calculate_factorial(num)
        if result != -1:
            print(f"Factorial of {num} is: {result}")
    except ValueError:
        print("Error: Please enter a valid integer!")

get_factorial_from_user()

# Method 5: Function statistics
print("\n" + "=" * 50)
print("Method 5: Function Statistics")

def factorial_stats():
    """Display factorial statistics"""
    print("Factorial values from 0 to 10:")
    print(f"{'Number':<10} {'Factorial':<15} {'Digits':<10}")
    print("-" * 35)
    
    for i in range(11):
        fact = calculate_factorial(i)
        digits = len(str(fact))
        print(f"{i:<10} {fact:<15} {digits:<10}")

factorial_stats()
