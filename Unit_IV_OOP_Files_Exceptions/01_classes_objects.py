"""
Program 1: Classes and Objects
Demonstrates creating classes, attributes, methods, and objects
"""

print("=== BASIC CLASS DEFINITION ===")
class Person:
    """A class to represent a person"""
    
    # Class attribute
    species = "Homo sapiens"
    
    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    # Instance method
    def introduce(self):
        return f"Hello, I am {self.name} and I am {self.age} years old."
    
    def birthday(self):
        self.age += 1
        return f"{self.name} is now {self.age} years old."

# Create objects
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(f"Person 1: {person1.name}, Age: {person1.age}")
print(f"Person 2: {person2.name}, Age: {person2.age}")
print(f"Species: {person1.species}")

print(f"\n{person1.introduce()}")
print(f"{person2.introduce()}")

print(f"\n{person1.birthday()}")

print("\n=== CLASS AND INSTANCE ATTRIBUTES ===")
class Counter:
    count = 0  # Class attribute
    
    def __init__(self, initial=0):
        self.value = initial  # Instance attribute
        Counter.count += 1
    
    def increment(self):
        self.value += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

c1 = Counter(5)
c2 = Counter(10)
print(f"c1.value: {c1.value}, c2.value: {c2.value}")
print(f"Counter.count (class attribute): {Counter.get_count()}")

c1.increment()
print(f"After c1.increment(): c1.value = {c1.value}")

print("\n=== METHODS ===")
class Calculator:
    def __init__(self):
        self.result = 0
    
    # Instance method
    def add(self, x, y):
        self.result = x + y
        return self.result
    
    # Class method
    @classmethod
    def from_sum(cls, a, b):
        obj = cls()
        obj.result = a + b
        return obj
    
    # Static method
    @staticmethod
    def multiply(x, y):
        return x * y
    
    # Magic method
    def __str__(self):
        return f"Calculator with result: {self.result}"

calc = Calculator()
print(f"Result of add(10, 20): {calc.add(10, 20)}")
print(f"Static method multiply(5, 3): {Calculator.multiply(5, 3)}")

calc2 = Calculator.from_sum(100, 50)
print(f"Created from class method: {calc2}")
print(f"calc2.result: {calc2.result}")

print("\n=== PROPERTIES ===")
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below -273.15°C")
        self._celsius = value

temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")

temp.celsius = 30
print(f"After setting to 30°C: Fahrenheit = {temp.fahrenheit}°F")

print("\n=== SPECIAL METHODS (MAGIC METHODS) ===")
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)
    
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 2: {v1 * 2}")
print(f"v1 == Vector(3, 4): {v1 == Vector(3, 4)}")
print(f"v1 < v2: {v1 < v2}")
print(f"len(v1): {len(v1)}")

print("\n=== ENCAPSULATION - PRIVATE ATTRIBUTES ===")
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self._balance = balance  # Protected (single underscore)
        self.__pin = 1234  # Private (double underscore)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. New balance: ${self._balance}"
        return "Invalid amount"
    
    def withdraw(self, amount, pin):
        if pin != self.__pin:
            return "Invalid PIN"
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        return "Invalid amount or insufficient funds"
    
    def get_balance(self, pin):
        if pin != self.__pin:
            return "Invalid PIN"
        return self._balance

account = BankAccount("Alice", 1000)
print(f"Account holder: {account.account_holder}")
print(account.deposit(500))
print(account.withdraw(200, 1234))
print(f"Balance: ${account.get_balance(1234)}")
print(account.withdraw(100, 0000))  # Wrong PIN

print("\n=== OBJECT RELATIONSHIPS ===")
class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city
    
    def __str__(self):
        return f"{self.street}, {self.city}"

class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address  # Composition
    
    def __str__(self):
        return f"{self.name} lives at {self.address}"

addr = Address("123 Main St", "New York")
emp = Employee("John", addr)
print(f"Employee: {emp}")
