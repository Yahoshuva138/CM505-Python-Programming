# Program 15: Recursion - Fibonacci Sequence
# Demonstrating recursive generation of Fibonacci numbers

print("=" * 50)
print("Program 15: Fibonacci Sequence using Recursion")
print("=" * 50)

print("\nFibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...")
print("Each number is sum of the two preceding ones")
print("Formula: F(n) = F(n-1) + F(n-2)")
print("Base cases: F(0) = 0, F(1) = 1")

# Recursive fibonacci function
def fibonacci_recursive(n):
    """
    Generate nth Fibonacci number using recursion
    Base case: F(0) = 0, F(1) = 1
    Recursive case: F(n) = F(n-1) + F(n-2)
    """
    if n < 0:
        return "Error: n must be non-negative"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Method 1: Generate Fibonacci numbers up to a position
print("\n" + "=" * 50)
print("Method 1: Fibonacci Numbers at Specific Positions")
positions = [0, 1, 5, 10, 15]
print(f"\n{'Position':<12} {'Fibonacci Number':<20}")
print("-" * 32)
for pos in positions:
    fib = fibonacci_recursive(pos)
    print(f"F({pos})<{12-len(str(pos))} {fib:<20}")

# Method 2: Generate sequence up to a certain number
print("\nMethod 2: Fibonacci Sequence up to 100")
print("\nFibonacci numbers up to 100:")
sequence = []
i = 0
while True:
    fib = fibonacci_recursive(i)
    if fib <= 100:
        sequence.append(fib)
        i += 1
    else:
        break

print(sequence)

# Method 3: More efficient approach - using iteration
print("\n" + "=" * 50)
print("Method 3: Efficient Iterative Approach")

def fibonacci_iterative(limit):
    """Generate Fibonacci sequence up to limit using iteration"""
    sequence = []
    a, b = 0, 1
    while a <= limit:
        sequence.append(a)
        a, b = b, a + b
    return sequence

fib_up_to_100 = fibonacci_iterative(100)
print(f"\nFibonacci sequence up to 100:")
print(fib_up_to_100)

# Method 4: Show recursion steps
print("\nMethod 4: Show Recursion Steps for F(5)")

call_count = 0

def fibonacci_with_steps(n, level=0):
    """Show Fibonacci calculation with recursion steps"""
    global call_count
    call_count += 1
    indent = "  " * level
    print(f"{indent}F({n})", end="")
    
    if n <= 1:
        print(f" = {n}")
        return n
    else:
        print()
        left = fibonacci_with_steps(n - 1, level + 1)
        right = fibonacci_with_steps(n - 2, level + 1)
        result = left + right
        print(f"{indent}F({n}) = {left} + {right} = {result}")
        return result

print("\nRecursion steps for F(5):")
call_count = 0
result = fibonacci_with_steps(5)
print(f"\nTotal function calls: {call_count}")

# Method 5: User input
print("\n" + "=" * 50)
print("Method 5: User Input")

try:
    choice = int(input("\n1. Find Fibonacci at position\n2. Get all Fibonacci up to value\nChoose (1-2): "))
    
    if choice == 1:
        pos = int(input("Enter position (0-20): "))
        if 0 <= pos <= 20:
            fib = fibonacci_recursive(pos)
            print(f"F({pos}) = {fib}")
        else:
            print("Position should be between 0 and 20")
    elif choice == 2:
        limit = int(input("Enter limit: "))
        seq = fibonacci_iterative(limit)
        print(f"Fibonacci sequence up to {limit}: {seq}")
    else:
        print("Invalid choice!")
except ValueError:
    print("Please enter valid integers!")

# Method 6: Comparison
print("\n" + "=" * 50)
print("Method 6: First 15 Fibonacci Numbers")
print(f"\n{'Position':<12} {'Fibonacci':<15}")
print("-" * 27)
for i in range(15):
    fib = fibonacci_recursive(i)
    print(f"F({i})<{10-len(str(i))} {fib:<15}")
