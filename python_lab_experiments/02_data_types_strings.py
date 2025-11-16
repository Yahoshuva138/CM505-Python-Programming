# Program 2: Working with Strings
# Demonstrating string data type and operations

print("=" * 50)
print("Program 2: Working with Strings")
print("=" * 50)

# String creation and operations
str1 = "Hello"
str2 = "Python"
print(f"\nString Operations:")
print(f"str1 = '{str1}'")
print(f"str2 = '{str2}'")
print(f"Concatenation: '{str1}' + ' ' + '{str2}' = '{str1 + ' ' + str2}'")
print(f"Repetition: '{str1}' * 3 = '{str1 * 3}'")
print(f"Length: len('{str1}') = {len(str1)}")

# String methods
name = "Python Programming"
print(f"\nString Methods:")
print(f"Original string: '{name}'")
print(f"Uppercase: '{name.upper()}'")
print(f"Lowercase: '{name.lower()}'")
print(f"Capitalize: '{name.capitalize()}'")
print(f"Replace 'Python' with 'Java': '{name.replace('Python', 'Java')}'")
print(f"Split: {name.split()}")
print(f"Count 'o': {name.count('o')}")

# String indexing and slicing
text = "Programming"
print(f"\nString Indexing and Slicing:")
print(f"String: '{text}'")
print(f"First character: '{text[0]}'")
print(f"Last character: '{text[-1]}'")
print(f"Characters 0-4: '{text[0:5]}'")
print(f"Reverse: '{text[::-1]}'")

# Data type checking
print(f"\nData Type Information:")
print(f"Type of '{str1}': {type(str1)}")
