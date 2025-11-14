"""
Program 7: OS Module and pathlib Module
Demonstrates directory management, file operations, and path handling
"""

import os
from pathlib import Path

print("=== CURRENT WORKING DIRECTORY ===")
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

print("\n=== CREATING DIRECTORIES ===")
# Create a single directory
if not os.path.exists("test_directory"):
    os.mkdir("test_directory")
    print("Created test_directory")
else:
    print("test_directory already exists")

# Create nested directories
if not os.path.exists("test_directory/sub1/sub2"):
    os.makedirs("test_directory/sub1/sub2")
    print("Created nested directories: test_directory/sub1/sub2")

print("\n=== LISTING DIRECTORY CONTENTS ===")
contents = os.listdir(".")
print(f"Contents of current directory (first 10):")
for item in contents[:10]:
    print(f"  {item}")

print("\n=== CHECKING IF FILE OR DIRECTORY EXISTS ===")
print(f"'test_directory' exists: {os.path.exists('test_directory')}")
print(f"'test_directory' is directory: {os.path.isdir('test_directory')}")
print(f"Current file 'nonexistent.txt' exists: {os.path.exists('nonexistent.txt')}")

print("\n=== WALKING THROUGH DIRECTORY TREE ===")
for root, dirs, files in os.walk("test_directory"):
    level = root.replace("test_directory", "").count(os.sep)
    indent = " " * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = " " * 2 * (level + 1)
    for file in files:
        print(f"{subindent}{file}")

print("\n=== FILE AND DIRECTORY OPERATIONS ===")
# Create a test file
test_file = "test_directory/test_file.txt"
with open(test_file, "w") as f:
    f.write("Test content")
print(f"Created file: {test_file}")

# Get file size
file_size = os.path.getsize(test_file)
print(f"File size: {file_size} bytes")

# Get file modification time
import time
mod_time = os.path.getmtime(test_file)
print(f"Last modified: {time.ctime(mod_time)}")

# Rename file
renamed_file = "test_directory/renamed_file.txt"
os.rename(test_file, renamed_file)
print(f"Renamed to: {renamed_file}")

# Copy file
import shutil
shutil.copy(renamed_file, "test_directory/sub1/copy_file.txt")
print(f"Copied file to: test_directory/sub1/copy_file.txt")

print("\n=== PATHLIB - MODERN PATH HANDLING ===")
# Creating Path objects
p = Path("test_directory")
print(f"Path object: {p}")
print(f"Path exists: {p.exists()}")
print(f"Is directory: {p.is_dir()}")
print(f"Absolute path: {p.absolute()}")

print("\n=== PATHLIB - PATH OPERATIONS ===")
p1 = Path("test_directory")
p2 = p1 / "sub1" / "file.txt"  # Using / operator for path joining
print(f"Joined path: {p2}")

# Get path components
print(f"Path parts: {p2.parts}")
print(f"Parent directory: {p2.parent}")
print(f"File name: {p2.name}")
print(f"File stem: {p2.stem}")
print(f"File suffix: {p2.suffix}")

print("\n=== PATHLIB - FILE OPERATIONS ===")
p = Path("test_directory/sub1")
if not p.exists():
    p.mkdir(parents=True)

# Create and write to file using pathlib
file_path = p / "pathlib_file.txt"
file_path.write_text("Content using pathlib")
print(f"Created file: {file_path}")

# Read file content
content = file_path.read_text()
print(f"File content: {content}")

print("\n=== PATHLIB - GLOB PATTERNS ===")
# Create some test files
for i in range(3):
    (Path("test_directory") / f"file{i}.txt").write_text(f"Content {i}")

# Find all .txt files
txt_files = list(Path("test_directory").glob("*.txt"))
print(f"Text files in test_directory: {[f.name for f in txt_files]}")

# Find files recursively
all_txt_files = list(Path("test_directory").rglob("*.txt"))
print(f"All text files recursively: {[f.name for f in all_txt_files]}")

print("\n=== ENVIRONMENT VARIABLES ===")
# Get environment variable
path_env = os.environ.get("PATH")
print(f"PATH variable exists: {bool(path_env)}")

# Set environment variable
os.environ["MY_VAR"] = "My Value"
print(f"Set MY_VAR: {os.environ.get('MY_VAR')}")

# Get all environment variables (first 5)
print("Environment variables (first 5):")
for i, (key, value) in enumerate(os.environ.items()):
    if i >= 5:
        break
    print(f"  {key}: {value[:50]}...")

print("\n=== SYSTEM INFORMATION ===")
print(f"Operating system: {os.name}")
print(f"Platform: {os.uname()}")
print(f"Process ID: {os.getpid()}")

print("\n=== JOINING PATHS ===")
# Using os.path.join
path1 = os.path.join("directory", "subdirectory", "file.txt")
print(f"os.path.join result: {path1}")

# Using pathlib (recommended)
path2 = Path("directory") / "subdirectory" / "file.txt"
print(f"pathlib result: {path2}")

print("\n=== ABSOLUTE AND RELATIVE PATHS ===")
rel_path = Path("test_directory/sub1")
abs_path = rel_path.absolute()
print(f"Relative path: {rel_path}")
print(f"Absolute path: {abs_path}")

print("\n=== CHECKING PATH COMPONENTS ===")
p = Path("/home/user/documents/file.txt")
print(f"Path: {p}")
print(f"Drive: {p.drive}")
print(f"Root: {p.root}")
print(f"Parts: {p.parts}")
print(f"Parents: {list(p.parents)}")

print("\n=== CLEANUP ===")
# Remove test files and directories
import shutil
if os.path.exists("test_directory"):
    shutil.rmtree("test_directory")
    print("Removed test_directory and its contents")

print("\nDirectory management operations completed!")
