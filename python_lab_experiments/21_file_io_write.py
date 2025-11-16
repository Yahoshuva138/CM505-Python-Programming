# Program 21: File I/O - Create File and Write Content
# Demonstrating file operations

print("=" * 50)
print("Program 21: File I/O - Create and Write")
print("=" * 50)

import os

# Method 1: Create and write file using write()
print("\nMethod 1: Create File with write()")

# Define file path
file_path = "hello.txt"

# Write to file
try:
    with open(file_path, 'w') as file:
        file.write("Hello World")
    print(f"File '{file_path}' created successfully!")
except Exception as e:
    print(f"Error: {e}")

# Method 2: Create file with multiple lines
print("\nMethod 2: Create File with Multiple Lines")

file_path2 = "python_info.txt"

try:
    with open(file_path2, 'w') as file:
        file.write("Python Programming\n")
        file.write("==================\n")
        file.write("Python is a high-level programming language.\n")
        file.write("It is easy to learn and powerful.\n")
        file.write("Python is used for web development, data science, AI, and more.\n")
    print(f"File '{file_path2}' created successfully!")
except Exception as e:
    print(f"Error: {e}")

# Method 3: Create file with writelines()
print("\nMethod 3: Create File with writelines()")

file_path3 = "programming_languages.txt"

languages = [
    "Python\n",
    "Java\n",
    "C++\n",
    "JavaScript\n",
    "C#\n"
]

try:
    with open(file_path3, 'w') as file:
        file.writelines(languages)
    print(f"File '{file_path3}' created successfully!")
except Exception as e:
    print(f"Error: {e}")

# Method 4: Append content to existing file
print("\nMethod 4: Append Content to File")

try:
    # First, create or open existing file
    with open(file_path, 'a') as file:  # 'a' for append
        file.write("\n\nThis is appended content!")
        file.write("\nAppended on a new line.")
    print(f"Content appended to '{file_path}'")
except Exception as e:
    print(f"Error: {e}")

# Method 5: Create file with formatted content
print("\nMethod 5: Create File with Formatted Content")

file_path4 = "student_record.txt"

try:
    with open(file_path4, 'w') as file:
        file.write("STUDENT RECORD\n")
        file.write("=" * 40 + "\n\n")
        
        students = [
            ("Raj", 101, 95),
            ("Priya", 102, 98),
            ("Arjun", 103, 92)
        ]
        
        for name, roll, marks in students:
            file.write(f"Name: {name}\n")
            file.write(f"Roll No: {roll}\n")
            file.write(f"Marks: {marks}\n")
            file.write("-" * 40 + "\n")
    
    print(f"File '{file_path4}' created successfully!")
except Exception as e:
    print(f"Error: {e}")

# Method 6: Create file using print() with file parameter
print("\nMethod 6: Create File Using print()")

file_path5 = "output.txt"

try:
    with open(file_path5, 'w') as file:
        print("This is line 1", file=file)
        print("This is line 2", file=file)
        print("This is line 3", file=file)
    print(f"File '{file_path5}' created successfully!")
except Exception as e:
    print(f"Error: {e}")

# Method 7: Verify file creation
print("\nMethod 7: Verify File Creation")

files_to_check = [file_path, file_path2, file_path3, file_path4, file_path5]
print("\nFiles created:")
print(f"{'Filename':<30} {'Exists':<10} {'Size (bytes)':<15}")
print("-" * 55)

for file in files_to_check:
    if os.path.exists(file):
        size = os.path.getsize(file)
        print(f"{file:<30} {'Yes':<10} {size:<15}")
    else:
        print(f"{file:<30} {'No':<10} {'-':<15}")

# Method 8: User input for file creation
print("\n" + "=" * 50)
print("Method 8: User Input for File Creation")

try:
    filename = input("Enter filename (with .txt): ")
    content = input("Enter content to write: ")
    
    with open(filename, 'w') as file:
        file.write(content)
    print(f"File '{filename}' created successfully!")
except Exception as e:
    print(f"Error: {e}")

# Method 9: File modes explanation
print("\n" + "=" * 50)
print("Method 9: File Modes Explanation")
print("""
File modes:
- 'r'  : Read (default)
- 'w'  : Write (creates new or overwrites existing)
- 'a'  : Append (adds to end of file)
- 'x'  : Create (fails if file exists)
- 'b'  : Binary mode
- 't'  : Text mode (default)
- '+'  : Read and Write
""")

print("\nProgram completed!")
