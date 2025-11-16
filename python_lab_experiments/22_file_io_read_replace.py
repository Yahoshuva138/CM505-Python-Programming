# Program 22: File I/O - Read and Replace Content
# Demonstrating file reading and string replacement

print("=" * 50)
print("Program 22: File I/O - Read and Replace")
print("=" * 50)

import os

# Step 1: Create a sample file to work with
print("\nStep 1: Creating sample file...")
sample_file = "sample.txt"

try:
    with open(sample_file, 'w') as f:
        f.write("Hello World\n")
        f.write("Python is helpful\n")
        f.write("Hello Python\n")
        f.write("Help is important\n")
    print(f"Sample file '{sample_file}' created.")
except Exception as e:
    print(f"Error: {e}")

# Method 1: Read and replace 'h' character
print("\n" + "=" * 50)
print("Method 1: Read and Replace 'h' with '-'")

try:
    # Read from original file
    with open(sample_file, 'r') as f:
        content = f.read()
    
    print(f"Original content:\n{content}")
    
    # Replace 'h' with '-'
    modified_content = content.replace('h', '-')
    
    print(f"\nAfter replacing 'h' with '-':\n{modified_content}")
    
    # Write to new file
    output_file1 = "sample_modified.txt"
    with open(output_file1, 'w') as f:
        f.write(modified_content)
    print(f"\nModified content saved to '{output_file1}'")
except Exception as e:
    print(f"Error: {e}")

# Method 2: Read and count character occurrences
print("\nMethod 2: Count Character Occurrences")

def count_character(filename, char):
    """Count occurrences of a character in file"""
    try:
        with open(filename, 'r') as f:
            content = f.read()
        
        count = content.count(char)
        print(f"File: {filename}")
        print(f"Content:\n{content}")
        print(f"Character '{char}' appears: {count} times")
        return count
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
        return -1

print("\nCounting 'a' in sample file:")
count_character(sample_file, 'a')

print("\nCounting 'e' in sample file:")
count_character(sample_file, 'e')

# Method 3: Case-insensitive replacement
print("\n" + "=" * 50)
print("Method 3: Case-Insensitive Operations")

try:
    with open(sample_file, 'r') as f:
        content = f.read()
    
    # Count 'h' (any case)
    h_lower = content.lower().count('h')
    print(f"Letter 'h' (lowercase) appears: {h_lower} times")
    
    # Replace 'H' and 'h'
    modified = content.replace('H', 'X').replace('h', 'x')
    print(f"\nAfter replacing both 'H' and 'h' with 'X' and 'x':\n{modified}")
except Exception as e:
    print(f"Error: {e}")

# Method 4: Line-by-line replacement
print("\nMethod 4: Line-by-Line Processing")

def process_lines(input_file, output_file, replace_char, replacement):
    """Process file line by line"""
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
        
        print(f"Processing '{input_file}' line by line:")
        print(f"Replacing '{replace_char}' with '{replacement}'")
        print()
        
        modified_lines = []
        for i, line in enumerate(lines):
            modified_line = line.replace(replace_char, replacement)
            modified_lines.append(modified_line)
            print(f"Line {i+1} original:  {line.rstrip()}")
            print(f"Line {i+1} modified: {modified_line.rstrip()}\n")
        
        # Write to output file
        with open(output_file, 'w') as f:
            f.writelines(modified_lines)
        
        print(f"Modified content saved to '{output_file}'")
    except Exception as e:
        print(f"Error: {e}")

output_file2 = "sample_line_modified.txt"
process_lines(sample_file, output_file2, 'p', '*')

# Method 5: Multiple replacements
print("\n" + "=" * 50)
print("Method 5: Multiple Replacements")

def multiple_replace(filename, replacements):
    """Apply multiple replacements"""
    try:
        with open(filename, 'r') as f:
            content = f.read()
        
        print(f"Original content:\n{content}\n")
        
        modified = content
        for old, new in replacements.items():
            modified = modified.replace(old, new)
        
        print(f"After multiple replacements:\n{modified}")
        return modified
    except Exception as e:
        print(f"Error: {e}")
        return None

replacements = {
    'o': '0',
    'e': '3',
    'l': '1'
}
multiple_replace(sample_file, replacements)

# Method 6: Count all characters
print("\nMethod 6: Count All Character Occurrences")

def count_all_chars(filename):
    """Count all unique characters"""
    try:
        with open(filename, 'r') as f:
            content = f.read()
        
        char_count = {}
        for char in content:
            if char not in '\n':  # Exclude newline
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
        
        print(f"File: {filename}")
        print(f"Content:\n{content}")
        print(f"\nCharacter count:")
        print(f"{'Character':<15} {'Count':<15}")
        print("-" * 30)
        
        for char, count in sorted(char_count.items()):
            if char == ' ':
                print(f"{'(space)':<15} {count:<15}")
            else:
                print(f"{char:<15} {count:<15}")
    except Exception as e:
        print(f"Error: {e}")

count_all_chars(sample_file)

# Method 7: User input for file operations
print("\n" + "=" * 50)
print("Method 7: User Input")

try:
    file_to_process = input("Enter filename to process: ")
    search_char = input("Enter character to search: ")
    
    if os.path.exists(file_to_process):
        count = count_character(file_to_process, search_char)
    else:
        print(f"File '{file_to_process}' not found!")
except Exception as e:
    print(f"Error: {e}")

print("\nProgram completed!")
