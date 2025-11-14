"""
Program 6: Loop Statements
Demonstrates for loops and while loops
"""

print("=== FOR LOOP - Simple Iteration ===")
for i in range(1, 6):
    print(f"Iteration {i}")

print("\n=== FOR LOOP - Iterating Over a List ===")
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

print("\n=== FOR LOOP - With index using enumerate() ===")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

print("\n=== FOR LOOP - Range with step ===")
print("Even numbers from 0 to 10:")
for i in range(0, 11, 2):
    print(i, end=" ")
print()

print("\n=== FOR LOOP - Nested Loops ===")
print("Multiplication Table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}*{j}={i*j}", end="  ")
    print()

print("\n=== WHILE LOOP - Basic ===")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

print("\n=== WHILE LOOP - With user input ===")
print("Enter numbers (type 'stop' to exit):")
# Uncomment below for interactive use
# while True:
#     user_input = input("Enter a number: ")
#     if user_input.lower() == 'stop':
#         break
#     print(f"You entered: {user_input}")

print("\n=== WHILE LOOP - Countdown ===")
countdown = 5
while countdown > 0:
    print(countdown, end=" ")
    countdown -= 1
print("\nBlast off!")

print("\n=== WHILE LOOP - Finding sum of digits ===")
num = 12345
temp = num
digit_sum = 0
while temp > 0:
    digit_sum += temp % 10
    temp //= 10
print(f"Sum of digits in {num}: {digit_sum}")
