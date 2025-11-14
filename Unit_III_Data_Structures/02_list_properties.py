"""
Program 2: List Properties - Mutability, Aliasing, Cloning, and Parameters
Demonstrates list behavior and how they're handled
"""

print("=== MUTABILITY ===")
print("Lists are mutable - they can be modified after creation")
original_list = [1, 2, 3]
print(f"Original list: {original_list}, ID: {id(original_list)}")
original_list.append(4)
print(f"After append(4): {original_list}, ID: {id(original_list)}")
print("ID remains same because list was modified in-place")

print("\n=== ALIASING ===")
list_a = [1, 2, 3]
list_b = list_a  # Aliasing - both refer to same object

print(f"list_a: {list_a}, ID: {id(list_a)}")
print(f"list_b: {list_b}, ID: {id(list_b)}")
print(f"list_a is list_b: {list_a is list_b}")

# Modify through list_a
list_a.append(4)
print(f"\nAfter list_a.append(4):")
print(f"list_a: {list_a}")
print(f"list_b: {list_b}")
print("Both changed because they point to the same list")

print("\n=== CLONING (SHALLOW COPY) ===")
original = [1, 2, 3]
clone1 = original.copy()
clone2 = list(original)
clone3 = original[:]

print(f"original: {original}, ID: {id(original)}")
print(f"clone1: {clone1}, ID: {id(clone1)}")
print(f"original is clone1: {original is clone1}")

original.append(4)
print(f"\nAfter original.append(4):")
print(f"original: {original}")
print(f"clone1: {clone1}")
print("Clone unchanged because it's a separate object")

print("\n=== DEEP COPY vs SHALLOW COPY ===")
import copy

nested_original = [[1, 2], [3, 4], [5, 6]]
shallow_copy = nested_original.copy()
deep_copy = copy.deepcopy(nested_original)

print(f"original: {nested_original}")
print(f"shallow_copy: {shallow_copy}")
print(f"deep_copy: {deep_copy}")

nested_original[0].append(99)
print(f"\nAfter original[0].append(99):")
print(f"original: {nested_original}")
print(f"shallow_copy: {shallow_copy}")
print(f"deep_copy: {deep_copy}")
print("Shallow copy affected by modification, deep copy is not")

print("\n=== LIST PARAMETERS - FUNCTION MODIFICATION ===")
def append_to_list(lst):
    """Function that modifies the list passed to it"""
    lst.append(999)
    print(f"Inside function: {lst}")

original_list = [1, 2, 3]
print(f"Before function: {original_list}")
append_to_list(original_list)
print(f"After function: {original_list}")
print("Original list was modified because lists are passed by reference")

print("\n=== AVOIDING UNWANTED MODIFICATIONS ===")
def safe_append(lst):
    """Function that doesn't modify the original list"""
    lst_copy = lst.copy()
    lst_copy.append(999)
    return lst_copy

original_list = [1, 2, 3]
print(f"Before function: {original_list}")
result = safe_append(original_list)
print(f"After function: {original_list}")
print(f"Returned list: {result}")
print("Original list unchanged")

print("\n=== EQUALITY vs IDENTITY ===")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3 = list1")
print(f"list1 == list2: {list1 == list2} (same content)")
print(f"list1 is list2: {list1 is list2} (different objects)")
print(f"list1 == list3: {list1 == list3} (same content)")
print(f"list1 is list3: {list1 is list3} (same object)")

print("\n=== MODIFYING DEFAULT ARGUMENTS ISSUE ===")
def add_to_default(item, items=[]):
    """PROBLEMATIC: mutable default argument"""
    items.append(item)
    return items

print("First call:")
print(add_to_default(1))
print("Second call:")
print(add_to_default(2))
print("Third call:")
print(add_to_default(3))
print("Default argument persists across calls - this is usually a bug!")

print("\n=== CORRECT WAY WITH DEFAULT ARGUMENTS ===")
def add_to_default_correct(item, items=None):
    """CORRECT: create new list if None"""
    if items is None:
        items = []
    items.append(item)
    return items

print("First call:")
print(add_to_default_correct(1))
print("Second call:")
print(add_to_default_correct(2))
print("Third call:")
print(add_to_default_correct(3))
print("Each call gets a fresh list")
