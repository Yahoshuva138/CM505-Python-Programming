"""
Program 3: Input and Output statements with formatted I/O
Demonstrates various methods of input and formatted output
"""

# Basic output
print("=== Basic Output ===")
print("Welcome to Python Programming!")

# Multiple arguments to print
print("Name:", "Alice", "Age:", 30)

# Formatted output using f-strings
print("\n=== Formatted Output (f-strings) ===")
name = "Bob"
age = 25
salary = 50000.50
print(f"Name: {name}, Age: {age}, Salary: ${salary:.2f}")

# Formatted output using .format()
print("\n=== Using .format() ===")
print("Name: {}, Age: {}, Salary: ${:.2f}".format(name, age, salary))

# Formatted output using % operator
print("\n=== Using % operator ===")
print("Name: %s, Age: %d, Salary: $%.2f" % (name, age, salary))

# Taking input from user
print("\n=== User Input ===")
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_salary = float(input("Enter your salary: "))

print(f"\nYou entered:")
print(f"Name: {user_name}")
print(f"Age: {user_age}")
print(f"Salary: ${user_salary:.2f}")

# Formatted string with different alignment
print("\n=== String Alignment ===")
text = "Python"
print(f"Left aligned: |{text:<15}|")
print(f"Right aligned: |{text:>15}|")
print(f"Center aligned: |{text:^15}|")
