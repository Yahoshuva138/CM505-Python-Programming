# Program 7: Geometry - Cone Volume and Surface Area
# Demonstrating mathematical calculations with pi

import math

print("=" * 50)
print("Program 7: Cone - Volume and Surface Area")
print("=" * 50)

# Formulas:
# Volume = (1/3) * π * r² * h
# Lateral Surface Area = π * r * l (where l = slant height)
# Total Surface Area = π * r * l + π * r²
# Slant height (l) = sqrt(r² + h²)

print("\nFormulas:")
print("Volume = (1/3) × π × r² × h")
print("Slant Height (l) = √(r² + h²)")
print("Lateral Surface Area = π × r × l")
print("Total Surface Area = π × r × l + π × r²")

# Method 1: Direct calculation
print("\n" + "=" * 50)
print("Method 1: Direct Calculation")
radius = 5
height = 12
slant_height = math.sqrt(radius**2 + height**2)
volume = (1/3) * math.pi * radius**2 * height
lateral_area = math.pi * radius * slant_height
total_area = lateral_area + math.pi * radius**2

print(f"\nCone with radius = {radius} cm, height = {height} cm")
print(f"Slant Height = √({radius}² + {height}²) = {slant_height:.2f} cm")
print(f"Volume = (1/3) × π × {radius}² × {height} = {volume:.2f} cm³")
print(f"Lateral Surface Area = π × {radius} × {slant_height:.2f} = {lateral_area:.2f} cm²")
print(f"Total Surface Area = {lateral_area:.2f} + π × {radius}² = {total_area:.2f} cm²")

# Method 2: User input
print("\nMethod 2: User Input")
try:
    r_input = float(input("Enter radius (in cm): "))
    h_input = float(input("Enter height (in cm): "))
    
    if r_input <= 0 or h_input <= 0:
        print("Radius and height must be positive!")
    else:
        l_input = math.sqrt(r_input**2 + h_input**2)
        v_input = (1/3) * math.pi * r_input**2 * h_input
        la_input = math.pi * r_input * l_input
        ta_input = la_input + math.pi * r_input**2
        
        print(f"\nCone with radius = {r_input} cm, height = {h_input} cm")
        print(f"Slant Height = {l_input:.2f} cm")
        print(f"Volume = {v_input:.2f} cm³")
        print(f"Lateral Surface Area = {la_input:.2f} cm²")
        print(f"Total Surface Area = {ta_input:.2f} cm²")
except ValueError:
    print("Please enter valid numbers!")

# Method 3: Multiple cones comparison
print("\nMethod 3: Multiple Cones Comparison")
cones = [(3, 4), (5, 12), (6, 8), (8, 15)]
print(f"\n{'Radius':<10} {'Height':<10} {'Slant H':<10} {'Volume':<15} {'Lateral Area':<15}")
print("-" * 60)
for r, h in cones:
    l = math.sqrt(r**2 + h**2)
    v = (1/3) * math.pi * r**2 * h
    la = math.pi * r * l
    print(f"{r:<10} {h:<10} {l:<10.2f} {v:<15.2f} {la:<15.2f}")
