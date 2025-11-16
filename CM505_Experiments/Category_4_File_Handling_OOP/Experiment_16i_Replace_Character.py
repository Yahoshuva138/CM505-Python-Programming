# Experiment 16(i): Replace Character in String

print("=" * 50)
print("EXPERIMENT 16(i): REPLACE CHARACTER")
print("=" * 50)

# Using replace() method
text = "Hello World"
print(f"\nOriginal text: {text}")

# Replace single character
new_text = text.replace("o", "0")
print(f"Replace 'o' with '0': {new_text}")

# Replace word
new_text = text.replace("World", "Python")
print(f"Replace 'World' with 'Python': {new_text}")

# Replace all occurrences
text = "aaa bbb aaa"
new_text = text.replace("a", "x")
print(f"\nOriginal: {text}")
print(f"Replace all 'a' with 'x': {new_text}")

print("=" * 50)
