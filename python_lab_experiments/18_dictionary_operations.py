# Program 18: Dictionary Operations - Create, Add, Delete
# Demonstrating dictionary manipulation

print("=" * 50)
print("Program 18: Dictionary Operations")
print("=" * 50)

# Method 1: Create dictionaries
print("\nMethod 1: Creating Dictionaries")

# Empty dictionary
dict1 = {}
print(f"Empty dict: {dict1}")

# Dictionary with initial values
student = {
    "name": "Raj",
    "roll": 101,
    "class": "10th",
    "marks": 95
}
print(f"Student dict: {student}")

# Dictionary with different data types
mixed_dict = {
    1: "One",
    "two": 2,
    3.14: "Pi",
    True: "Boolean"
}
print(f"Mixed types dict: {mixed_dict}")

# Using dict() constructor
dict2 = dict(a=1, b=2, c=3)
print(f"Created with dict(): {dict2}")

# Method 2: Adding elements
print("\n" + "=" * 50)
print("Method 2: Adding Elements to Dictionary")

my_dict = {"color": "Red", "number": 5}
print(f"Original: {my_dict}")

# Add single key-value pair
my_dict["size"] = "Large"
print(f"After adding 'size': {my_dict}")

# Add multiple pairs using update()
my_dict.update({"shape": "Circle", "weight": 2.5})
print(f"After update(): {my_dict}")

# Add nested dictionary
my_dict["properties"] = {"transparent": True, "solid": False}
print(f"After adding nested dict: {my_dict}")

# Method 3: Accessing elements
print("\nMethod 3: Accessing Dictionary Elements")

person = {
    "name": "Alice",
    "age": 25,
    "city": "Delhi",
    "email": "alice@example.com"
}
print(f"Dictionary: {person}")
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"Using get(): {person.get('city')}")
print(f"Get with default: {person.get('country', 'India')}")

# Method 4: Deleting elements
print("\n" + "=" * 50)
print("Method 4: Deleting Elements from Dictionary")

book = {
    "title": "Python Basics",
    "author": "John",
    "pages": 300,
    "price": 500
}
print(f"Original: {book}")

# Delete using del
del book["price"]
print(f"After del book['price']: {book}")

# Delete using pop()
author = book.pop("author")
print(f"After pop('author'): {book}")
print(f"Popped value: {author}")

# Clear all elements
book_copy = book.copy()
book_copy.clear()
print(f"After clear(): {book_copy}")

# Method 5: Dictionary operations
print("\nMethod 5: Dictionary Operations and Methods")

inventory = {
    "apples": 10,
    "bananas": 5,
    "oranges": 8,
    "grapes": 12
}
print(f"Inventory: {inventory}")
print(f"Keys: {list(inventory.keys())}")
print(f"Values: {list(inventory.values())}")
print(f"Items: {list(inventory.items())}")
print(f"Number of items: {len(inventory)}")
print(f"'apples' in inventory: {'apples' in inventory}")

# Method 6: Complete example
print("\n" + "=" * 50)
print("Method 6: Complete Student Record Management")

student_record = {}

# Add initial data
student_record["name"] = "Priya"
student_record["roll"] = 105
student_record["marks"] = {"math": 95, "science": 88, "english": 92}
print(f"Student record: {student_record}")

# Update marks
student_record["marks"]["math"] = 97
print(f"After updating math marks: {student_record}")

# Add new subject
student_record["marks"]["hindi"] = 85
print(f"After adding hindi: {student_record}")

# Remove a subject
del student_record["marks"]["english"]
print(f"After removing english: {student_record}")

# Method 7: Iterating through dictionary
print("\nMethod 7: Iterating Through Dictionary")

product = {"name": "Laptop", "price": 50000, "brand": "Dell"}
print(f"Dictionary: {product}\n")

print("Iterating through keys:")
for key in product:
    print(f"  {key}: {product[key]}")

print("\nIterating through values:")
for value in product.values():
    print(f"  {value}")

print("\nIterating through items:")
for key, value in product.items():
    print(f"  {key} → {value}")

# Method 8: Interactive dictionary operations
print("\n" + "=" * 50)
print("Method 8: Interactive Dictionary Management")

contacts = {"Raj": 9876543210, "Priya": 9123456789}
print(f"Contacts: {contacts}")

while True:
    print("\n1. Add contact  2. Remove contact  3. Search  4. View all  5. Exit")
    choice = input("Choose (1-5): ")
    
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone
        print(f"Added {name}")
    elif choice == '2':
        name = input("Enter name to remove: ")
        if name in contacts:
            del contacts[name]
            print(f"Removed {name}")
        else:
            print(f"{name} not found")
    elif choice == '3':
        name = input("Enter name to search: ")
        print(f"{name}: {contacts.get(name, 'Not found')}")
    elif choice == '4':
        print("All contacts:")
        for name, phone in contacts.items():
            print(f"  {name}: {phone}")
    elif choice == '5':
        break
    else:
        print("Invalid choice!")
