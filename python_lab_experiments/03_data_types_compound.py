# Program 3: Working with Tuples, Lists, and Dictionaries
# Demonstrating compound data types

print("=" * 50)
print("Program 3: Working with Tuples, Lists, and Dictionaries")
print("=" * 50)

# Tuple operations
print("\nTuples (Immutable):")
tuple1 = (10, 20, 30, 40, 50)
tuple2 = ("Apple", "Banana", "Orange")
print(f"tuple1 = {tuple1}")
print(f"tuple2 = {tuple2}")
print(f"Length of tuple1: {len(tuple1)}")
print(f"First element: {tuple1[0]}")
print(f"Last element: {tuple1[-1]}")
print(f"Slice tuple1[1:4]: {tuple1[1:4]}")
print(f"Count of 30 in tuple1: {tuple1.count(30)}")
print(f"Index of 'Banana': {tuple2.index('Banana')}")

# List operations
print("\n" + "=" * 50)
print("Lists (Mutable):")
list1 = [10, 20, 30, 40, 50]
list2 = ["Python", "Java", "C++", "JavaScript"]
print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"Length of list1: {len(list1)}")
print(f"First element: {list1[0]}")
print(f"Last element: {list1[-1]}")
print(f"Sum: {sum(list1)}")
print(f"Maximum: {max(list1)}")
print(f"Minimum: {min(list1)}")

# Dictionary operations
print("\n" + "=" * 50)
print("Dictionaries (Key-Value Pairs):")
student = {
    "name": "Raj",
    "roll_no": 101,
    "class": "10th",
    "marks": 95.5
}
print(f"student = {student}")
print(f"Student name: {student['name']}")
print(f"Roll number: {student['roll_no']}")
print(f"Marks: {student['marks']}")
print(f"All keys: {student.keys()}")
print(f"All values: {student.values()}")
print(f"Number of items: {len(student)}")

# Data type checking
print("\n" + "=" * 50)
print("Data Type Information:")
print(f"Type of tuple1: {type(tuple1)}")
print(f"Type of list1: {type(list1)}")
print(f"Type of student: {type(student)}")
