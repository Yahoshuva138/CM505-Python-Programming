"""
Program 3: Method Overloading and Overriding
Demonstrates method overriding and simulating overloading
"""

print("=== METHOD OVERRIDING ===")
class Parent:
    def greet(self):
        return "Hello from Parent"
    
    def display(self):
        return "Parent display method"

class Child(Parent):
    # Override parent method
    def greet(self):
        return "Hello from Child"
    
    # This method only exists in Child
    def extra_method(self):
        return "Extra method in Child"

parent = Parent()
child = Child()

print(f"Parent greet(): {parent.greet()}")
print(f"Child greet(): {child.greet()}")
print(f"Child display() (inherited): {child.display()}")
print(f"Child extra_method(): {child.extra_method()}")

print("\n=== CALLING PARENT METHOD USING super() ===")
class Animal_Override:
    def __init__(self, name):
        self.name = name
    
    def describe(self):
        return f"Animal: {self.name}"

class Dog_Override(Animal_Override):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def describe(self):
        parent_desc = super().describe()
        return f"{parent_desc}, Breed: {self.breed}"

dog = Dog_Override("Rex", "Labrador")
print(f"Dog description: {dog.describe()}")

print("\n=== METHOD OVERLOADING SIMULATION ===")
# Python doesn't support true method overloading
# But we can simulate it using default arguments or *args, **kwargs

class Calculator:
    def add(self, a, b, c=0, d=0):
        """Add 2 to 4 numbers"""
        return a + b + c + d

calc = Calculator()
print(f"add(5, 10): {calc.add(5, 10)}")
print(f"add(5, 10, 15): {calc.add(5, 10, 15)}")
print(f"add(5, 10, 15, 20): {calc.add(5, 10, 15, 20)}")

print("\n=== METHOD OVERLOADING WITH *args ===")
class Printer:
    def print_data(self, *args):
        """Print any number of arguments"""
        for arg in args:
            print(f"  {arg}")

printer = Printer()
print("Printing single value:")
printer.print_data(10)
print("Printing multiple values:")
printer.print_data(10, 20, 30)
print("Printing strings:")
printer.print_data("Hello", "World", "Python")

print("\n=== OPERATOR OVERLOADING ===")
class Vector_Overload:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Overload + operator"""
        return Vector_Overload(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Overload - operator"""
        return Vector_Overload(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Overload * operator"""
        return Vector_Overload(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        """Right multiplication"""
        return self.__mul__(scalar)
    
    def __eq__(self, other):
        """Overload == operator"""
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector_Overload(1, 2)
v2 = Vector_Overload(3, 4)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 3: {v1 * 3}")
print(f"2 * v1: {2 * v1}")
print(f"v1 == Vector(1, 2): {v1 == Vector_Overload(1, 2)}")

print("\n=== COMPARISON OPERATOR OVERLOADING ===")
class Person_Compare:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __lt__(self, other):
        """Less than"""
        return self.age < other.age
    
    def __le__(self, other):
        """Less than or equal"""
        return self.age <= other.age
    
    def __gt__(self, other):
        """Greater than"""
        return self.age > other.age
    
    def __ge__(self, other):
        """Greater than or equal"""
        return self.age >= other.age
    
    def __eq__(self, other):
        """Equal"""
        return self.age == other.age
    
    def __str__(self):
        return f"{self.name} ({self.age})"

p1 = Person_Compare("Alice", 30)
p2 = Person_Compare("Bob", 25)

print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p1 > p2: {p1 > p2}")
print(f"p1 < p2: {p1 < p2}")
print(f"p1 == Person('Alice', 30): {p1 == Person_Compare('Alice', 30)}")

print("\n=== CONTAINER PROTOCOL OVERLOADING ===")
class CustomList:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
    
    def __contains__(self, item):
        return item in self.items
    
    def __str__(self):
        return str(self.items)

clist = CustomList([1, 2, 3, 4, 5])
print(f"clist: {clist}")
print(f"len(clist): {len(clist)}")
print(f"clist[2]: {clist[2]}")
print(f"3 in clist: {3 in clist}")
print(f"10 in clist: {10 in clist}")
clist[0] = 99
print(f"After clist[0] = 99: {clist}")

print("\n=== CALLABLE OBJECT (Functor) ===")
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        """Make instance callable like a function"""
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(f"double(5): {double(5)}")
print(f"triple(5): {triple(5)}")
