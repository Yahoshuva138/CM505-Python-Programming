"""
Program 5: Exception Handling
Demonstrates try-except blocks, multiple exceptions, else, finally, and raising exceptions
"""

print("=== BASIC TRY-EXCEPT ===")
# Example 1: Division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# Example 2: Index error
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError:
    print("Error: Index out of range")

# Example 3: Type error
try:
    result = "hello" + 5
except TypeError:
    print("Error: Cannot concatenate string and integer")

print("\n=== CATCHING MULTIPLE EXCEPTIONS ===")
try:
    data = {"name": "Alice"}
    age = int(data["age"])
except KeyError:
    print("Error: Key not found in dictionary")
except ValueError:
    print("Error: Invalid value for conversion")
except Exception as e:
    print(f"Unexpected error: {e}")

print("\n=== SINGLE EXCEPT MULTIPLE EXCEPTIONS ===")
try:
    numbers = [1, 2, 3]
    index = int("hello")  # ValueError
    value = numbers[index]  # IndexError
except (ValueError, IndexError) as e:
    print(f"Error caught: {type(e).__name__}: {e}")

print("\n=== EXCEPTION WITH ERROR DETAILS ===")
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Exception type: {type(e).__name__}")
    print(f"Exception message: {e}")
    print(f"Exception args: {e.args}")

print("\n=== TRY-EXCEPT-ELSE ===")
try:
    numbers = [10, 20, 30]
    index = 1
    value = numbers[index]
except IndexError:
    print("Error: Index out of range")
else:
    print(f"Successfully accessed: numbers[{index}] = {value}")

print("\n=== TRY-EXCEPT-FINALLY ===")
def read_file_example():
    try:
        file = open("nonexistent.txt", "r")
        data = file.read()
    except FileNotFoundError:
        print("Error: File not found")
    finally:
        print("Finally block: This always executes")

read_file_example()

print("\n=== COMPLETE TRY-EXCEPT-ELSE-FINALLY ===")
def process_data(data):
    try:
        result = int(data)
    except ValueError:
        print(f"Error: '{data}' is not a valid integer")
        return None
    else:
        print(f"Successfully converted: {result}")
        return result
    finally:
        print("Processing complete")

print("Processing '42':")
process_data("42")

print("\nProcessing 'abc':")
process_data("abc")

print("\n=== RAISING EXCEPTIONS ===")
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age is unrealistic")
    return f"Valid age: {age}"

try:
    print(validate_age(25))
except ValueError as e:
    print(f"Validation error: {e}")

try:
    print(validate_age(-5))
except ValueError as e:
    print(f"Validation error: {e}")

print("\n=== CUSTOM EXCEPTIONS ===")
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: balance={balance}, requested={amount}")

class BankAccount_Exception:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

account = BankAccount_Exception("Alice", 100)
print(f"Current balance: ${account.balance}")

try:
    print(account.withdraw(50))
except InsufficientFundsError as e:
    print(f"Error: {e}")

try:
    print(account.withdraw(100))
except InsufficientFundsError as e:
    print(f"Error: {e}")

print("\n=== RE-RAISING EXCEPTIONS ===")
def process_payment(amount):
    try:
        if amount <= 0:
            raise ValueError("Amount must be positive")
    except ValueError as e:
        print(f"Processing error: {e}")
        raise  # Re-raise the exception

try:
    process_payment(-10)
except ValueError:
    print("Caught re-raised exception")

print("\n=== EXCEPTION CHAINING ===")
try:
    try:
        result = 1 / 0
    except ZeroDivisionError as e:
        raise ValueError("Invalid calculation") from e
except ValueError as e:
    print(f"Error: {e}")
    print(f"Caused by: {e.__cause__}")

print("\n=== CONTEXT MANAGER (WITH STATEMENT) ===")
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"Error occurred: {exc_type.__name__}: {exc_val}")
        return False

# Example with real file handling
try:
    with open("test.txt", "w") as f:
        f.write("Hello, World!")
    print("File created successfully")
except IOError as e:
    print(f"IO Error: {e}")

print("\n=== BUILT-IN EXCEPTIONS SUMMARY ===")
exceptions_info = [
    ("ValueError", "Invalid value for a function"),
    ("TypeError", "Invalid type for operation"),
    ("IndexError", "Index out of range"),
    ("KeyError", "Key not found in dictionary"),
    ("FileNotFoundError", "File not found"),
    ("ZeroDivisionError", "Division by zero"),
    ("AttributeError", "Attribute not found on object"),
    ("ImportError", "Import failed"),
]

print("Common Built-in Exceptions:")
for exc_name, description in exceptions_info:
    print(f"  {exc_name}: {description}")
