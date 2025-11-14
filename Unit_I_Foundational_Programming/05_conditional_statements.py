"""
Program 5: Conditional Statements
Demonstrates if, if-else, and if-elif-else statements
"""

print("=== IF STATEMENT ===")
age = 18
if age >= 18:
    print(f"Age {age}: You are an adult")

print("\n=== IF-ELSE STATEMENT ===")
score = 45
if score >= 50:
    print(f"Score {score}: You passed the exam")
else:
    print(f"Score {score}: You failed the exam")

print("\n=== IF-ELIF-ELSE STATEMENT ===")
marks = 78
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Marks: {marks}, Grade: {grade}")

print("\n=== NESTED IF STATEMENTS ===")
number = 25
if number > 0:
    print(f"{number} is positive")
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
else:
    print(f"{number} is not positive")

print("\n=== CONDITIONAL WITH AND/OR ===")
age_val = 20
income = 50000
if age_val >= 18 and income >= 30000:
    print("You are eligible for a loan")
else:
    print("You are not eligible for a loan")

temperature = 35
if temperature > 30 or temperature < 5:
    print(f"Weather is extreme: {temperature}°C")
else:
    print(f"Weather is normal: {temperature}°C")

print("\n=== TERNARY OPERATOR (CONDITIONAL EXPRESSION) ===")
num = 15
result = "Even" if num % 2 == 0 else "Odd"
print(f"{num} is {result}")

status = "Pass" if marks >= 50 else "Fail"
print(f"Status: {status}")
