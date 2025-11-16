# Program 4: Currency Conversion - US Dollars to Indian Rupees
# Demonstrating arithmetic operators and data type conversion

print("=" * 50)
print("Program 4: Currency Conversion (USD to INR)")
print("=" * 50)

# Conversion rate (1 USD = 83.5 INR approximately)
conversion_rate = 83.5

# Method 1: Simple conversion
print("\nMethod 1: Simple Conversion")
dollars = 100
rupees = dollars * conversion_rate
print(f"${dollars} USD = ₹{rupees} INR")

# Method 2: Taking input from user
print("\nMethod 2: User Input Conversion")
try:
    amount_usd = float(input("Enter amount in USD: "))
    amount_inr = amount_usd * conversion_rate
    print(f"${amount_usd} USD = ₹{amount_inr:.2f} INR")
except ValueError:
    print("Please enter a valid number!")

# Method 3: Multiple conversions with different amounts
print("\nMethod 3: Multiple Conversions")
amounts = [50, 100, 250, 500, 1000]
print(f"\n{'USD':<15} {'INR':<15}")
print("-" * 30)
for usd in amounts:
    inr = usd * conversion_rate
    print(f"${usd:<14} ₹{inr:<14.2f}")

# Data type conversion demonstration
print("\n" + "=" * 50)
print("Data Type Conversion:")
num_string = "1000"
print(f"String: '{num_string}' (type: {type(num_string).__name__})")
num_int = int(num_string)
print(f"Converted to int: {num_int} (type: {type(num_int).__name__})")
num_float = float(num_string)
print(f"Converted to float: {num_float} (type: {type(num_float).__name__})")
result = num_int * conversion_rate
print(f"Calculation result: {result} (type: {type(result).__name__})")
