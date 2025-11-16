# Program 13: Functions - Multiplication Table
# Demonstrating functions with parameters

print("=" * 50)
print("Program 13: Multiplication Table using Functions")
print("=" * 50)

# Function 1: Print multiplication table for a single number
def print_table(num, limit=10):
    """
    Print multiplication table for a number
    Args:
        num: Number for which to print table
        limit: Up to which number (default 10)
    """
    print(f"\nMultiplication table of {num} (up to {limit}):")
    for i in range(1, limit + 1):
        print(f"{num} × {i} = {num * i}")

# Function 2: Print formatted table
def print_formatted_table(num, limit=10):
    """Print formatted multiplication table"""
    print(f"\nTable of {num}:")
    print(f"{'Multiplier':<12} {'Result':<12}")
    print("-" * 24)
    for i in range(1, limit + 1):
        print(f"{num} × {i:<8} {num * i:<12}")

# Function 3: Generate table as list
def generate_table(num, limit=10):
    """
    Generate multiplication table as a list
    Args:
        num: Number for which to generate table
        limit: Up to which number
    Returns:
        List of multiplication results
    """
    return [num * i for i in range(1, limit + 1)]

# Function 4: Print multiple tables
def print_multiple_tables(start, end, limit=10):
    """Print multiplication tables for range of numbers"""
    for num in range(start, end + 1):
        print_table(num, limit)

# Method 1: Direct function calls
print("\nMethod 1: Single Table")
print_table(5)
print_table(7, 8)

# Method 2: Formatted output
print("\nMethod 2: Formatted Tables")
print_formatted_table(4)
print_formatted_table(6)

# Method 3: Generate and display
print("\nMethod 3: Generate as List")
for num in [3, 5]:
    table = generate_table(num)
    print(f"\nTable of {num}: {table}")

# Method 4: Multiple tables
print("\n" + "=" * 50)
print("Method 4: Multiple Tables (1-5)")
print_multiple_tables(1, 5)

# Method 5: User input with function
print("\n" + "=" * 50)
print("Method 5: User Input")

def get_table_from_user():
    """Get multiplication table from user"""
    try:
        num = int(input("Enter a number: "))
        limit = int(input("Enter limit (default 10): ") or 10)
        
        if num <= 0 or limit <= 0:
            print("Number and limit must be positive!")
            return
        
        print_formatted_table(num, limit)
    except ValueError:
        print("Please enter valid integers!")

get_table_from_user()

# Method 6: Table comparison
print("\n" + "=" * 50)
print("Method 6: Compare Tables")

def compare_tables(num1, num2, limit=5):
    """Compare multiplication tables"""
    print(f"\nComparison of Tables {num1} and {num2}:")
    print(f"{'i':<5} {num1}×i":<12} {num2}×i":<12}")
    print("-" * 29)
    for i in range(1, limit + 1):
        print(f"{i:<5} {num1*i:<12} {num2*i:<12}")

compare_tables(3, 5, 8)
