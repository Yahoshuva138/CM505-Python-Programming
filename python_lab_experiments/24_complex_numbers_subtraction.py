# Program 24: Classes and Objects - Subtract Complex Numbers
# Demonstrating object-oriented programming with more operations

print("=" * 50)
print("Program 24: Complex Number Subtraction using Classes")
print("=" * 50)

# Define Enhanced Complex Number class
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
    
    def subtract(self, other):
        """Subtract two complex numbers (self - other)
        If z1 = a + bi and z2 = c + di
        Then z1 - z2 = (a-c) + (b-d)i
        """
        real_diff = self.real - other.real
        imag_diff = self.imaginary - other.imaginary
        return ComplexNumber(real_diff, imag_diff)
    
    def multiply(self, other):
        """Multiply two complex numbers
        (a+bi)(c+di) = (ac-bd) + (ad+bc)i
        """
        real_part = (self.real * other.real) - (self.imaginary * other.imaginary)
        imag_part = (self.real * other.imaginary) + (self.imaginary * other.real)
        return ComplexNumber(real_part, imag_part)
    
    def magnitude(self):
        """Calculate magnitude of complex number"""
        import math
        return math.sqrt(self.real**2 + self.imaginary**2)
    
    def conjugate(self):
        """Return conjugate of complex number"""
        return ComplexNumber(self.real, -self.imaginary)

# Method 1: Basic subtraction
print("\nMethod 1: Basic Complex Number Subtraction")

c1 = ComplexNumber(5, 3)
c2 = ComplexNumber(2, 1)

print(f"Complex number 1: {c1}")
print(f"Complex number 2: {c2}")

difference = c1.subtract(c2)
print(f"\n{c1} - {c2} = {difference}")

# Verify: (5+3i) - (2+1i) = 3+2i
print(f"Verification: (5-2) + (3-1)i = 3 + 2i ✓")

# Method 2: Multiple subtractions
print("\n" + "=" * 50)
print("Method 2: Multiple Subtractions")

num1 = ComplexNumber(10, 5)
num2 = ComplexNumber(3, 2)
num3 = ComplexNumber(1, 1)

print(f"Complex 1: {num1}")
print(f"Complex 2: {num2}")
print(f"Complex 3: {num3}")

result1 = num1.subtract(num2)
print(f"\n{num1} - {num2} = {result1}")

result2 = result1.subtract(num3)
print(f"{result1} - {num3} = {result2}")

# Method 3: Subtraction with negative results
print("\n" + "=" * 50)
print("Method 3: Subtraction with Negative Results")

a = ComplexNumber(1, 1)
b = ComplexNumber(5, 3)

print(f"Complex A: {a}")
print(f"Complex B: {b}")

result_ab = a.subtract(b)
print(f"\nA - B = {result_ab}")
print(f"({a}) - ({b})")
print(f"= (1-5) + (1-3)i")
print(f"= -4 - 2i ✓")

# Method 4: Comparison with addition
print("\nMethod 4: Addition vs Subtraction")

x = ComplexNumber(4, 3)
y = ComplexNumber(2, 1)

addition = x.add(y)
subtraction = x.subtract(y)

print(f"X = {x}")
print(f"Y = {y}")
print(f"\nX + Y = {addition}")
print(f"X - Y = {subtraction}")

# Method 5: All operations demonstration
print("\n" + "=" * 50)
print("Method 5: All Operations Demonstration")

z1 = ComplexNumber(6, 2)
z2 = ComplexNumber(3, 1)

print(f"Z1 = {z1}")
print(f"Z2 = {z2}")
print(f"\nZ1 + Z2 = {z1.add(z2)}")
print(f"Z1 - Z2 = {z1.subtract(z2)}")
print(f"Z1 × Z2 = {z1.multiply(z2)}")
print(f"Magnitude of Z1 = {z1.magnitude():.2f}")
print(f"Magnitude of Z2 = {z2.magnitude():.2f}")
print(f"Conjugate of Z1 = {z1.conjugate()}")

# Method 6: User input for subtraction
print("\n" + "=" * 50)
print("Method 6: User Input for Subtraction")

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
    
    sum_result = comp1.add(comp2)
    diff_result = comp1.subtract(comp2)
    
    print(f"\nAddition: {comp1} + {comp2} = {sum_result}")
    print(f"Subtraction: {comp1} - {comp2} = {diff_result}")
except ValueError:
    print("Please enter valid numbers!")

# Method 7: Properties of complex subtraction
print("\n" + "=" * 50)
print("Method 7: Properties of Complex Subtraction")

a = ComplexNumber(7, 2)
b = ComplexNumber(3, 1)

print(f"Property demonstrations with A = {a}, B = {b}")
print(f"\nA - B = {a.subtract(b)}")
print(f"B - A = {b.subtract(a)}")
print(f"(A - B) + B = {a.subtract(b).add(b)}")
print(f"Should equal A: {a}")

# Method 8: Table of subtractions
print("\nMethod 8: Subtraction Table")

nums = [
    ComplexNumber(5, 4),
    ComplexNumber(3, 2),
    ComplexNumber(1, 1)
]

print(f"\n{'Complex 1':<15} {'-':<3} {'Complex 2':<15} {'=':<3} {'Result':<15}")
print("-" * 60)

for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j:
            result = nums[i].subtract(nums[j])
            print(f"{str(nums[i]):<15} {'-':<3} {str(nums[j]):<15} {'=':<3} {str(result):<15}")
