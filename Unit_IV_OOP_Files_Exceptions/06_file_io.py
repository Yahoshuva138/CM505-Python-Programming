"""
Program 6: File Input and Output
Demonstrates opening, reading, writing, and closing files in different modes
"""

import os

print("=== WRITING TO FILES ===")
# Write mode - creates file or overwrites existing
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")
    file.write("Python file I/O\n")

print("File created and written successfully")

print("\n=== READING ENTIRE FILE ===")
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

print("\n=== READING FILE LINE BY LINE ===")
with open("example.txt", "r") as file:
    print("Reading lines individually:")
    for line in file:
        print(f"  {line.rstrip()}")

print("\n=== READLINES METHOD ===")
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(f"Number of lines: {len(lines)}")
    for i, line in enumerate(lines, 1):
        print(f"  Line {i}: {line.rstrip()}")

print("\n=== APPEND MODE ===")
with open("example.txt", "a") as file:
    file.write("Appended line 1\n")
    file.write("Appended line 2\n")

print("Data appended to file")

with open("example.txt", "r") as file:
    print("Updated file content:")
    print(file.read())

print("\n=== WRITING MULTIPLE LINES AT ONCE ===")
with open("data.txt", "w") as file:
    lines = [
        "Name,Age,City\n",
        "Alice,30,New York\n",
        "Bob,25,Los Angeles\n",
        "Charlie,35,Chicago\n"
    ]
    file.writelines(lines)

print("Multi-line file created")

print("\n=== READING AND WRITING NUMBERS ===")
with open("numbers.txt", "w") as file:
    for i in range(1, 11):
        file.write(f"Number: {i}, Square: {i**2}\n")

print("Numbers file created")

with open("numbers.txt", "r") as file:
    print("Numbers file content:")
    print(file.read())

print("\n=== READING WITH ERROR HANDLING ===")
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found")

print("\n=== CHECKING FILE EXISTENCE ===")
if os.path.exists("example.txt"):
    print("example.txt exists")
    print(f"File size: {os.path.getsize('example.txt')} bytes")
else:
    print("File does not exist")

print("\n=== DIFFERENT FILE MODES ===")
modes_info = [
    ("r", "Read - default mode, file must exist"),
    ("w", "Write - creates or overwrites file"),
    ("a", "Append - adds to end of file"),
    ("x", "Exclusive creation - fails if file exists"),
    ("b", "Binary mode - append to other modes"),
    ("t", "Text mode - default, append to other modes"),
    ("+", "Read and write - append to other modes"),
]

print("File Modes:")
for mode, description in modes_info:
    print(f"  {mode:4} - {description}")

print("\n=== BINARY MODE ===")
# Write binary data
with open("binary.bin", "wb") as file:
    data = bytes([65, 66, 67, 68, 69])  # ASCII: ABCDE
    file.write(data)

# Read binary data
with open("binary.bin", "rb") as file:
    binary_content = file.read()
    print(f"Binary content: {binary_content}")
    print(f"As text: {binary_content.decode('ascii')}")

print("\n=== READING AND WRITING WITH CSV ===")
import csv

# Write CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Grade", "Score"])
    writer.writerow(["Alice", "A", 95])
    writer.writerow(["Bob", "B", 85])
    writer.writerow(["Charlie", "A", 92])

print("CSV file created")

# Read CSV
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    print("CSV content:")
    for row in reader:
        print(f"  {row}")

print("\n=== WRITING AND READING JSON ===")
import json

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "hiking", "programming"]
}

# Write JSON
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file created")

# Read JSON
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print("JSON content:")
    print(f"  Name: {loaded_data['name']}")
    print(f"  Age: {loaded_data['age']}")
    print(f"  Hobbies: {loaded_data['hobbies']}")

print("\n=== FILE POINTER POSITION ===")
with open("example.txt", "r") as file:
    print(f"Initial position: {file.tell()}")
    first_line = file.readline()
    print(f"After reading first line: {file.tell()}")
    print(f"First line: {first_line.rstrip()}")
    
    file.seek(0)  # Go back to beginning
    print(f"After seek(0): {file.tell()}")

print("\n=== FILE OPERATIONS WITH PATHLIB ===")
from pathlib import Path

p = Path("example.txt")
print(f"File name: {p.name}")
print(f"File stem: {p.stem}")
print(f"File suffix: {p.suffix}")
print(f"Absolute path: {p.absolute()}")
print(f"Is file: {p.is_file()}")

print("\n=== CLEANUP - REMOVE TEST FILES ===")
files_to_remove = ["example.txt", "data.txt", "numbers.txt", "binary.bin", "students.csv", "data.json"]
for filename in files_to_remove:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Removed {filename}")
