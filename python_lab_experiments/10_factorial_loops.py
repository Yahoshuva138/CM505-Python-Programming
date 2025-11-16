# Program 10: Loops - Factorial Calculation
# Demonstrating for and while loops

print("=" * 50)
print("Program 10: Factorial Calculation using Loops")
print("=" * 50)

# Method 1: Using for loop
print("\nMethod 1: Using For Loop")

def factorial_for(n):
    """Calculate factorial using for loop"""
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test cases
numbers = [0, 1, 5, 10, 7]
print("Factorial using for loop:")
for num in numbers:
    fact = factorial_for(num)
    print(f"{num}! = {fact}")

# Method 2: Using while loop
print("\nMethod 2: Using While Loop")

def factorial_while(n):
    """Calculate factorial using while loop"""
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

print("Factorial using while loop:")
for num in numbers:
    fact = factorial_while(num)
    print(f"{num}! = {fact}")

# Method 3: Show calculation steps
print("\nMethod 3: Show Calculation Steps")

def factorial_steps(n):
    """Calculate factorial and show steps"""
    if n < 0:
        print("Factorial not defined for negative numbers")
        return
    
    result = 1
    print(f"Calculating {n}!")
    print("Steps:", end=" ")
    for i in range(1, n + 1):
        result *= i
        if i == 1:
            print(f"{i}", end="")
        else:
            print(f" × {i}", end="")
    print(f" = {result}")
    return result

for num in [5, 6]:
    factorial_steps(num)
    print()

# Method 4: User input
print("=" * 50)
print("Method 4: User Input")
try:
    user_num = int(input("Enter a number to find factorial: "))
    if user_num < 0:
        print("Factorial is not defined for negative numbers!")
    else:
        result = factorial_for(user_num)
        print(f"{user_num}! = {result}")
except ValueError:
    print("Please enter a valid integer!")
