# Program 5: Data Size Conversion - Bits to MB, GB, TB
# Demonstrating arithmetic operators and data type conversion

print("=" * 50)
print("Program 5: Data Size Conversion (Bits to MB/GB/TB)")
print("=" * 50)

# Conversion constants
bits_per_byte = 8
bytes_per_kb = 1024
bytes_per_mb = 1024 ** 2
bytes_per_gb = 1024 ** 3
bytes_per_tb = 1024 ** 4

# Function to convert bits to various units
def bits_to_units(bits):
    bytes_val = bits / bits_per_byte
    kb = bytes_val / bytes_per_kb
    mb = bytes_val / bytes_per_mb
    gb = bytes_val / bytes_per_gb
    tb = bytes_val / bytes_per_tb
    return bytes_val, kb, mb, gb, tb

# Example conversions
print("\nExample Conversions:")
test_bits = [
    8,                          # 1 byte
    8 * 1024,                   # 1 KB
    8 * 1024 ** 2,              # 1 MB
    8 * 1024 ** 3,              # 1 GB
    8 * 1024 ** 4               # 1 TB
]

for bits in test_bits:
    bytes_val, kb, mb, gb, tb = bits_to_units(bits)
    print(f"\n{bits:,} bits =")
    print(f"  {bytes_val:.2f} Bytes")
    print(f"  {kb:.2f} KB")
    print(f"  {mb:.2f} MB")
    print(f"  {gb:.2f} GB")
    print(f"  {tb:.2f} TB")

# User input conversion
print("\n" + "=" * 50)
print("Manual Conversion:")
try:
    bits_input = float(input("Enter size in bits: "))
    bytes_val, kb, mb, gb, tb = bits_to_units(bits_input)
    print(f"\n{bits_input:,.0f} bits =")
    print(f"  {bytes_val:.4f} Bytes")
    print(f"  {kb:.4f} KB")
    print(f"  {mb:.4f} MB")
    print(f"  {gb:.4f} GB")
    print(f"  {tb:.4f} TB")
except ValueError:
    print("Please enter a valid number!")

# Data type conversion demonstration
print("\n" + "=" * 50)
print("Data Type Conversion in Calculations:")
bits_str = "1048576"  # 1 Megabit in string
print(f"String input: '{bits_str}' (type: {type(bits_str).__name__})")
bits_int = int(bits_str)
print(f"Converted to int: {bits_int} (type: {type(bits_int).__name__})")
mb_float = bits_int / bits_per_byte / bytes_per_mb
print(f"Result in MB: {mb_float} (type: {type(mb_float).__name__})")
mb_rounded = round(mb_float, 2)
print(f"Rounded result: {mb_rounded} (type: {type(mb_rounded).__name__})")
