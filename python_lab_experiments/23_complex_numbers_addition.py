# Program 23: Classes and Objects - Add Complex Numbers
# Demonstrating object-oriented programming

print("=" * 50)
print("Program 23: Complex Number Addition using Classes")
print("=" * 50)

# Define Complex Number class
class ComplexNumber:
    """Class to represent and operate on complex numbers"""
    
    def __init__(self, real, imaginary):
        """Constructor to initialize complex number
        Args:
            real: Real part of complex number
            imaginary: Imaginary part of complex number
        """
        self.real = real
        self.imaginary = imaginary
    
    def display(self):
        """Display complex number"""
        if self.imaginary >= 0:
            print(f"{self.real} + {self.imaginary}i")
        else:
            print(f"{self.real} - {abs(self.imaginary)}i")
    
    def __str__(self):
        """String representation"""
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"
    
    def add(self, other):
        """Add two complex numbers"""
        real_sum = self.real + other.real
        imag_sum = self.imaginary + other.imaginary
        return ComplexNumber(real_sum, imag_sum)
    
    def magnitude(self):
        """Calculate magnitude of complex number"""
        import math
        return math.sqrt(self.real**2 + self.imaginary**2)
    
    def conjugate(self):
        """Return conjugate of complex number"""
        return ComplexNumber(self.real, -self.imaginary)

# Method 1: Direct object creation and addition
print("\nMethod 1: Direct Object Creation and Addition")

# Create complex numbers
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)

print(f"Complex number 1: {c1}")
print(f"Complex number 2: {c2}")

# Add complex numbers
c3 = c1.add(c2)
print(f"Sum: {c3}")

# Method 2: Multiple additions
print("\n" + "=" * 50)
print("Method 2: Multiple Complex Number Additions")

numbers = [
    ComplexNumber(2, 3),
    ComplexNumber(4, 5),
    ComplexNumber(1, 2),
    ComplexNumber(3, 1)
]

print("Complex numbers:")
for i, num in enumerate(numbers):
    print(f"  C{i+1} = {num}")

# Add first two
result1 = numbers[0].add(numbers[1])
print(f"\nC1 + C2 = {result1}")

# Add result with third
result2 = result1.add(numbers[2])
print(f"(C1 + C2) + C3 = {result2}")

# Add result with fourth
result3 = result2.add(numbers[3])
print(f"((C1 + C2) + C3) + C4 = {result3}")

# Method 3: Display object properties
print("\nMethod 3: Complex Number Properties")

c = ComplexNumber(3, 4)
print(f"\nComplex number: {c}")
print(f"Real part: {c.real}")
print(f"Imaginary part: {c.imaginary}")
print(f"Magnitude: {c.magnitude()}")
print(f"Conjugate: {c.conjugate()}")

# Method 4: Using Python's built-in complex type
print("\n" + "=" * 50)
print("Method 4: Using Python's Built-in Complex Type")

# Python has built-in complex support
py_c1 = 3 + 4j
py_c2 = 1 + 2j

print(f"Python complex 1: {py_c1}")
print(f"Python complex 2: {py_c2}")
print(f"Sum: {py_c1 + py_c2}")
print(f"Difference: {py_c1 - py_c2}")
print(f"Product: {py_c1 * py_c2}")
print(f"Division: {py_c1 / py_c2}")
print(f"Conjugate: {py_c1.conjugate()}")
print(f"Real part: {py_c1.real}")
print(f"Imaginary part: {py_c1.imag}")

# Method 5: User input
print("\n" + "=" * 50)
print("Method 5: User Input for Complex Numbers")

try:
    print("Enter first complex number:")
    r1 = float(input("  Real part: "))
    i1 = float(input("  Imaginary part: "))
    
    print("Enter second complex number:")
    r2 = float(input("  Real part: "))
    i2 = float(input("  Imaginary part: "))
    
    comp1 = ComplexNumber(r1, i1)
    comp2 = ComplexNumber(r2, i2)
    
    print(f"\nComplex 1: {comp1}")
    print(f"Complex 2: {comp2}")
    
    result = comp1.add(comp2)
    print(f"Sum: {result}")
    print(f"Magnitude of sum: {result.magnitude():.2f}")
except ValueError:
    print("Please enter valid numbers!")

# Method 6: Demonstration
print("\n" + "=" * 50)
print("Method 6: Complete Example")

print("Adding multiple complex numbers:")
c1 = ComplexNumber(1, 1)
c2 = ComplexNumber(2, 2)
c3 = ComplexNumber(3, 3)

print(f"C1 = {c1}")
print(f"C2 = {c2}")
print(f"C3 = {c3}")

sum_all = c1.add(c2).add(c3)
print(f"\nC1 + C2 + C3 = {sum_all}")
