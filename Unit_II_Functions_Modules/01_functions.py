"""
Program 1: Functions - Definition and Calling
Demonstrates basic function definition and invocation
"""

# Function with no parameters and no return value
def greet():
    print("Hello, World!")

greet()

# Function with parameters
def add(a, b):
    return a + b

result = add(10, 20)
print(f"Addition of 10 and 20: {result}")

# Function with multiple parameters
def person_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

person_info("Alice", 30, "New York")

# Function with return statement
def multiply(x, y):
    return x * y

product = multiply(5, 6)
print(f"Product of 5 and 6: {product}")

# Function with default arguments
def greet_with_name(name="Guest"):
    print(f"Hello, {name}!")

greet_with_name()
greet_with_name("Bob")

# Function with keyword arguments
def describe_person(name, age=25, city="Unknown"):
    return f"{name} is {age} years old and lives in {city}"

print(describe_person("John"))
print(describe_person("Jane", 28))
print(describe_person("Mike", 35, "London"))

# Function with variable-length arguments (*args)
def sum_numbers(*args):
    """Sum any number of arguments"""
    total = 0
    for num in args:
        total += num
    return total

print(f"\nSum of 1, 2, 3: {sum_numbers(1, 2, 3)}")
print(f"Sum of 10, 20, 30, 40: {sum_numbers(10, 20, 30, 40)}")

# Function with keyword arguments (**kwargs)
def print_info(**kwargs):
    """Print key-value pairs"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\nPersonal Info:")
print_info(name="Alice", age=30, profession="Engineer")

# Function with *args and **kwargs
def mixed_function(a, b, *args, **kwargs):
    print(f"a = {a}, b = {b}")
    print(f"Additional positional args: {args}")
    print(f"Keyword arguments: {kwargs}")

mixed_function(1, 2, 3, 4, 5, name="John", age=25)
