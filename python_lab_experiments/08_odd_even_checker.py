# Program 8: Conditional Logic - Odd or Even Checker
# Demonstrating if-else statements

print("=" * 50)
print("Program 8: Odd or Even Checker")
print("=" * 50)

# Method 1: Direct check
print("\nMethod 1: Direct Check")
numbers = [10, 23, 45, 78, 99, 102]
print(f"Numbers: {numbers}\n")
print(f"{'Number':<10} {'Result':<15}")
print("-" * 25)

for num in numbers:
    if num % 2 == 0:
        result = "Even"
    else:
        result = "Odd"
    print(f"{num:<10} {result:<15}")

# Method 2: Using ternary operator
print("\n" + "=" * 50)
print("Method 2: Using Ternary Operator")
test_num = 37
result = "Even" if test_num % 2 == 0 else "Odd"
print(f"{test_num} is {result}")

# Method 3: User input
print("\nMethod 3: User Input")
try:
    user_num = int(input("Enter a number: "))
    if user_num % 2 == 0:
        print(f"{user_num} is Even")
    else:
        print(f"{user_num} is Odd")
except ValueError:
    print("Please enter a valid integer!")

# Method 4: Function approach
print("\n" + "=" * 50)
print("Method 4: Using Functions")

def check_odd_even(n):
    return "Even" if n % 2 == 0 else "Odd"

test_numbers = [5, 20, 33, 88]
for num in test_numbers:
    print(f"{num} is {check_odd_even(num)}")
