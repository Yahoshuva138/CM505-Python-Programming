# Program 6: Geometry - Square Area and Perimeter
# Demonstrating mathematical calculations

import math

print("=" * 50)
print("Program 6: Square - Area and Perimeter")
print("=" * 50)

# Method 1: Direct calculation
print("\nMethod 1: Direct Calculation")
side = 5
area = side ** 2
perimeter = 4 * side
print(f"Square with side = {side} cm")
print(f"Area = {side} × {side} = {area} cm²")
print(f"Perimeter = 4 × {side} = {perimeter} cm")

# Method 2: User input
print("\nMethod 2: User Input")
try:
    side_input = float(input("Enter side of square (in cm): "))
    if side_input <= 0:
        print("Side must be positive!")
    else:
        area_input = side_input ** 2
        perimeter_input = 4 * side_input
        print(f"\nSquare with side = {side_input} cm")
        print(f"Area = {area_input:.2f} cm²")
        print(f"Perimeter = {perimeter_input:.2f} cm")
except ValueError:
    print("Please enter a valid number!")

# Method 3: Multiple squares comparison
print("\nMethod 3: Multiple Squares Comparison")
sides = [2, 5, 10, 15]
print(f"\n{'Side (cm)':<12} {'Area (cm²)':<15} {'Perimeter (cm)':<15}")
print("-" * 42)
for s in sides:
    a = s ** 2
    p = 4 * s
    print(f"{s:<12} {a:<15} {p:<15}")
