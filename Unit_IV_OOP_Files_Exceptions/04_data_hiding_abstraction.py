"""
Program 4: Data Hiding and Data Abstraction
Demonstrates OOP concepts of encapsulation and abstraction
"""

print("=== ENCAPSULATION - DATA HIDING ===")
class BankAccount_Encapsulation:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute
        self.__transaction_history = []  # Private attribute
    
    def deposit(self, amount):
        """Public method to deposit money"""
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"Deposit: +${amount}")
            return f"Successfully deposited ${amount}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        """Public method to withdraw money"""
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdraw: -${amount}")
            return f"Successfully withdrew ${amount}"
        return "Invalid amount or insufficient funds"
    
    def get_balance(self):
        """Public method to get balance"""
        return self.__balance
    
    def __process_transaction(self, amount):
        """Private method"""
        pass

account = BankAccount_Encapsulation("Alice", 1000)
print(f"Account holder: {account.account_holder}")
print(account.deposit(500))
print(account.withdraw(200))
print(f"Balance: ${account.get_balance()}")

# Cannot access private attributes directly (though Python allows it with name mangling)
try:
    print(account.__balance)
except AttributeError as e:
    print(f"Cannot access __balance directly: {e}")

print("\n=== NAME MANGLING (Private Attribute Access) ===")
# Python uses name mangling for private attributes (__attribute)
print(f"Can access with name mangling: {account._BankAccount_Encapsulation__balance}")
# But this is not recommended practice

print("\n=== PROPERTY DECORATORS FOR CONTROLLED ACCESS ===")
class Temperature_Property:
    def __init__(self, celsius=0):
        self._celsius = celsius  # Protected attribute
    
    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Getter for fahrenheit (read-only)"""
        return (self._celsius * 9/5) + 32
    
    @property
    def kelvin(self):
        """Getter for kelvin"""
        return self._celsius + 273.15

temp = Temperature_Property(25)
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")
print(f"Kelvin: {temp.kelvin}K")

temp.celsius = 30
print(f"After setting to 30°C: Fahrenheit = {temp.fahrenheit}°F")

try:
    temp.celsius = -300  # Invalid
except ValueError as e:
    print(f"Error: {e}")

print("\n=== ABSTRACTION ===")
from abc import ABC, abstractmethod

class Shape_Abstract(ABC):
    """Abstract base class for shapes"""
    
    @abstractmethod
    def area(self):
        """Calculate area - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented by subclasses"""
        pass
    
    def describe(self):
        """Concrete method available to all subclasses"""
        return f"I am a shape with area {self.area()}"

class Circle_Abstract(Shape_Abstract):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle_Abstract(Shape_Abstract):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Cannot instantiate abstract class
# shape = Shape_Abstract()  # TypeError

circle = Circle_Abstract(5)
rectangle = Rectangle_Abstract(4, 6)

print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")
print(f"Circle: {circle.describe()}")

print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")
print(f"Rectangle: {rectangle.describe()}")

print("\n=== INTERFACE-LIKE BEHAVIOR ===")
class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def query(self, sql):
        pass
    
    @abstractmethod
    def close(self):
        pass

class MySQLDatabase(DatabaseInterface):
    def connect(self):
        return "Connected to MySQL"
    
    def query(self, sql):
        return f"Executing MySQL query: {sql}"
    
    def close(self):
        return "MySQL connection closed"

class PostgresDatabase(DatabaseInterface):
    def connect(self):
        return "Connected to PostgreSQL"
    
    def query(self, sql):
        return f"Executing PostgreSQL query: {sql}"
    
    def close(self):
        return "PostgreSQL connection closed"

databases = [MySQLDatabase(), PostgresDatabase()]

for db in databases:
    print(f"{db.connect()}")
    print(f"{db.query('SELECT * FROM users')}")
    print(f"{db.close()}")
    print()

print("\n=== GETTER AND SETTER METHODS ===")
class Student:
    def __init__(self, name, roll_number):
        self._name = name
        self._roll_number = roll_number
        self._gpa = 0.0
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self._name = name
    
    def get_gpa(self):
        return self._gpa
    
    def set_gpa(self, gpa):
        if not (0 <= gpa <= 4.0):
            raise ValueError("GPA must be between 0 and 4.0")
        self._gpa = gpa
    
    def get_roll_number(self):
        return self._roll_number

student = Student("Alice", "2024001")
print(f"Name: {student.get_name()}")
print(f"Roll Number: {student.get_roll_number()}")

student.set_gpa(3.8)
print(f"GPA: {student.get_gpa()}")

student.set_name("Bob")
print(f"Updated name: {student.get_name()}")

try:
    student.set_gpa(5.0)  # Invalid
except ValueError as e:
    print(f"Error: {e}")
