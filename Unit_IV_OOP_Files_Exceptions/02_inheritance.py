"""
Program 2: Inheritance
Demonstrates single inheritance, multiple inheritance, and method resolution order
"""

print("=== SINGLE INHERITANCE ===")
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"
    
    def move(self):
        return f"{self.name} is moving"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

dog = Dog("Rex")
cat = Cat("Whiskers")

print(f"{dog.name}: {dog.speak()}")
print(f"{dog.move()}")
print(f"\n{cat.name}: {cat.speak()}")
print(f"{cat.move()}")

print("\n=== CALLING PARENT CLASS METHODS ===")
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def describe(self):
        return f"{self.color} {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, color, num_doors):
        super().__init__(brand, color)
        self.num_doors = num_doors
    
    def describe(self):
        parent_desc = super().describe()
        return f"{parent_desc} with {self.num_doors} doors"

car = Car("Toyota", "Blue", 4)
print(f"Car: {car.describe()}")

print("\n=== MULTIPLE INHERITANCE ===")
class Flyer:
    def fly(self):
        return "Flying in the sky"

class Swimmer:
    def swim(self):
        return "Swimming in water"

class Duck(Flyer, Swimmer):
    def __init__(self, name):
        self.name = name
    
    def describe(self):
        return f"{self.name} is a duck"

duck = Duck("Donald")
print(f"{duck.describe()}")
print(duck.fly())
print(duck.swim())

print("\n=== METHOD RESOLUTION ORDER (MRO) ===")
class A:
    def method(self):
        return "Method from A"

class B(A):
    def method(self):
        return "Method from B"

class C(A):
    def method(self):
        return "Method from C"

class D(B, C):
    pass

d = D()
print(f"D().method(): {d.method()}")
print(f"\nMRO for D: {[cls.__name__ for cls in D.__mro__]}")

print("\n=== ISSUBCLASS AND ISINSTANCE ===")
class Shape:
    pass

class Circle(Shape):
    pass

class Rectangle(Shape):
    pass

circle = Circle()
rectangle = Rectangle()
shape = Shape()

print(f"Circle is subclass of Shape: {issubclass(Circle, Shape)}")
print(f"Rectangle is subclass of Shape: {issubclass(Rectangle, Shape)}")
print(f"circle is instance of Circle: {isinstance(circle, Circle)}")
print(f"circle is instance of Shape: {isinstance(circle, Shape)}")
print(f"rectangle is instance of Circle: {isinstance(rectangle, Circle)}")

print("\n=== ABSTRACT BASE CLASSES ===")
from abc import ABC, abstractmethod

class Animal_ABC(ABC):
    @abstractmethod
    def sound(self):
        pass
    
    def describe(self):
        return f"I am an animal"

class Dog_ABC(Animal_ABC):
    def sound(self):
        return "Woof!"

# Can't instantiate abstract class
# animal = Animal_ABC()  # TypeError

dog_abc = Dog_ABC()
print(f"Dog sound: {dog_abc.sound()}")
print(f"Dog describe: {dog_abc.describe()}")

print("\n=== COOPERATIVE MULTIPLE INHERITANCE ===")
class Mixin1:
    def method_a(self):
        return "Mixin1 method A"

class Mixin2:
    def method_b(self):
        return "Mixin2 method B"

class Base:
    def base_method(self):
        return "Base method"

class Combined(Mixin1, Mixin2, Base):
    def combined_method(self):
        return f"{self.method_a()}, {self.method_b()}, {self.base_method()}"

combined = Combined()
print(f"Combined: {combined.combined_method()}")

print("\n=== POLYMORPHISM ===")
class Shape_Poly:
    def area(self):
        pass

class Square(Shape_Poly):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class Circle_Poly(Shape_Poly):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Square(5), Circle_Poly(3)]
print("Areas of shapes:")
for shape in shapes:
    print(f"  {shape.area()}")

print("\n=== HIERARCHICAL INHERITANCE ===")
class Employee_Hierarchy:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

class Manager(Employee_Hierarchy):
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)
        self.team_size = team_size

class Developer(Employee_Hierarchy):
    def __init__(self, name, emp_id, language):
        super().__init__(name, emp_id)
        self.language = language

manager = Manager("Alice", 101, 5)
developer = Developer("Bob", 102, "Python")

print(f"Manager: {manager.name}, ID: {manager.emp_id}, Team: {manager.team_size}")
print(f"Developer: {developer.name}, ID: {developer.emp_id}, Language: {developer.language}")
