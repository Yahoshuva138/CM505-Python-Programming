# Program 17: List Operations - Sort, Reverse, Count
# Demonstrating list sorting and manipulation

print("=" * 50)
print("Program 17: List Sort, Reverse, and Count")
print("=" * 50)

# Method 1: Sorting lists
print("\nMethod 1: Sorting Lists")

# Numeric list
numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"Original numbers: {numbers}")

sorted_asc = sorted(numbers)  # Returns new sorted list
print(f"Sorted ascending: {sorted_asc}")

sorted_desc = sorted(numbers, reverse=True)  # Sort descending
print(f"Sorted descending: {sorted_desc}")

# In-place sorting
numbers_copy = numbers.copy()
numbers_copy.sort()
print(f"After sort() (in-place): {numbers_copy}")

# Sorting strings
words = ["zebra", "apple", "mango", "banana"]
print(f"\nOriginal words: {words}")
print(f"Sorted words: {sorted(words)}")

# Method 2: Reversing lists
print("\nMethod 2: Reversing Lists")

list_to_reverse = [1, 2, 3, 4, 5]
print(f"Original: {list_to_reverse}")

# Using slicing
reversed_slice = list_to_reverse[::-1]
print(f"Using slicing [::-1]: {reversed_slice}")

# Using reversed()
reversed_list = list(reversed(list_to_reverse))
print(f"Using reversed(): {reversed_list}")

# In-place reversal
list_copy = list_to_reverse.copy()
list_copy.reverse()
print(f"Using reverse() method: {list_copy}")

# Method 3: Counting elements
print("\nMethod 3: Counting Elements")

items = ["apple", "banana", "apple", "orange", "apple", "banana"]
print(f"List: {items}")
print(f"Count of 'apple': {items.count('apple')}")
print(f"Count of 'banana': {items.count('banana')}")
print(f"Count of 'orange': {items.count('orange')}")
print(f"Count of 'grape': {items.count('grape')}")

# Method 4: Combined operations
print("\n" + "=" * 50)
print("Method 4: Combined Operations")

data = [45, 23, 56, 12, 78, 23, 45, 90, 23]
print(f"Original list: {data}")
print(f"Sorted: {sorted(data)}")
print(f"Sorted reversed: {sorted(data, reverse=True)}")
print(f"Reversed (not sorted): {data[::-1]}")
print(f"Unique elements: {list(set(data))}")
print(f"Count of 23: {data.count(23)}")

# Method 5: Sorting with specific criteria
print("\nMethod 5: Advanced Sorting")

students = [
    ("Alice", 85),
    ("Bob", 75),
    ("Charlie", 90),
    ("David", 80)
]
print("Students (name, marks):")
for name, marks in students:
    print(f"  {name}: {marks}")

# Sort by marks
sorted_by_marks = sorted(students, key=lambda x: x[1])
print("\nSorted by marks (ascending):")
for name, marks in sorted_by_marks:
    print(f"  {name}: {marks}")

# Sort by marks descending
sorted_by_marks_desc = sorted(students, key=lambda x: x[1], reverse=True)
print("\nSorted by marks (descending):")
for name, marks in sorted_by_marks_desc:
    print(f"  {name}: {marks}")

# Method 6: Demonstration with all operations
print("\nMethod 6: Complete Example")

scores = [85, 90, 78, 92, 88, 85, 95]
print(f"Original scores: {scores}")
print(f"Sorted scores: {sorted(scores)}")
print(f"Highest to lowest: {sorted(scores, reverse=True)}")
print(f"Length: {len(scores)}")
print(f"Average: {sum(scores) / len(scores):.2f}")
print(f"Highest: {max(scores)}")
print(f"Lowest: {min(scores)}")
print(f"Count of 85: {scores.count(85)}")

# Method 7: User interactive
print("\n" + "=" * 50)
print("Method 7: Interactive List Operations")

user_list = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Initial list: {user_list}")

while True:
    print("\n1. Sort  2. Reverse  3. Count element  4. Show stats  5. Exit")
    choice = input("Choose (1-5): ")
    
    if choice == '1':
        print(f"Sorted ascending: {sorted(user_list)}")
        print(f"Sorted descending: {sorted(user_list, reverse=True)}")
    elif choice == '2':
        print(f"Reversed: {user_list[::-1]}")
    elif choice == '3':
        try:
            elem = int(input("Enter element to count: "))
            print(f"Count of {elem}: {user_list.count(elem)}")
        except ValueError:
            print("Invalid input!")
    elif choice == '4':
        print(f"Length: {len(user_list)}")
        print(f"Sum: {sum(user_list)}")
        print(f"Max: {max(user_list)}")
        print(f"Min: {min(user_list)}")
    elif choice == '5':
        break
    else:
        print("Invalid choice!")
