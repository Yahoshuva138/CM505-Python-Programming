# Program 16: List Operations - Create, Add, Delete
# Demonstrating list manipulation

print("=" * 50)
print("Program 16: List Operations")
print("=" * 50)

# Method 1: Create lists
print("\nMethod 1: Creating Lists")
list1 = []  # Empty list
list2 = [1, 2, 3, 4, 5]  # List with integers
list3 = ["Apple", "Banana", "Orange"]  # List with strings
list4 = [1, "Hello", 3.14, True]  # Mixed data types
list5 = [1, [2, 3], [4, 5, 6]]  # Nested lists

print(f"Empty list: {list1}")
print(f"Integer list: {list2}")
print(f"String list: {list3}")
print(f"Mixed types: {list4}")
print(f"Nested list: {list5}")

# Method 2: Adding elements
print("\n" + "=" * 50)
print("Method 2: Adding Elements to List")

my_list = [1, 2, 3]
print(f"Original list: {my_list}")

# Using append() - adds at end
my_list.append(4)
print(f"After append(4): {my_list}")

# Using insert() - adds at specific position
my_list.insert(1, 10)
print(f"After insert(1, 10): {my_list}")

# Using extend() - adds multiple elements
my_list.extend([5, 6, 7])
print(f"After extend([5, 6, 7]): {my_list}")

# Method 3: Deleting elements
print("\nMethod 3: Deleting Elements from List")

numbers = [10, 20, 30, 40, 50, 60]
print(f"Original list: {numbers}")

# Using remove() - removes by value
numbers.remove(30)
print(f"After remove(30): {numbers}")

# Using pop() - removes by index
popped = numbers.pop(2)
print(f"After pop(2) - removed {popped}: {numbers}")

# Using del - removes by index
del numbers[0]
print(f"After del numbers[0]: {numbers}")

# Method 4: Complete example
print("\n" + "=" * 50)
print("Method 4: Complete List Management Example")

tasks = []
print("Task Manager:")
print("1. Create initial list")
print("2. Add tasks")
print("3. Remove tasks")
print()

# Step 1: Create
tasks = ["Study", "Exercise"]
print(f"Initial tasks: {tasks}")

# Step 2: Add
tasks.append("Read book")
tasks.insert(1, "Breakfast")
print(f"After additions: {tasks}")

# Step 3: Remove
tasks.remove("Breakfast")
print(f"After removal: {tasks}")

# Method 5: List operations with user input
print("\nMethod 5: Interactive List Operations")

shopping_list = ["Milk", "Bread"]
print(f"Shopping list: {shopping_list}")

try:
    while True:
        print("\n1. Add item  2. Remove item  3. View list  4. Exit")
        choice = input("Choose (1-4): ")
        
        if choice == '1':
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"Added '{item}'. List: {shopping_list}")
        elif choice == '2':
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed '{item}'. List: {shopping_list}")
            else:
                print(f"'{item}' not found in list")
        elif choice == '3':
            print(f"Current list: {shopping_list}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
except Exception as e:
    print(f"Error: {e}")

# Method 6: List properties
print("\n" + "=" * 50)
print("Method 6: List Properties")
sample_list = [5, 2, 8, 1, 9, 3]
print(f"List: {sample_list}")
print(f"Length: {len(sample_list)}")
print(f"Maximum: {max(sample_list)}")
print(f"Minimum: {min(sample_list)}")
print(f"Sum: {sum(sample_list)}")
print(f"Is 5 in list? {5 in sample_list}")
print(f"Count of 5: {sample_list.count(5)}")
print(f"Index of 8: {sample_list.index(8)}")
