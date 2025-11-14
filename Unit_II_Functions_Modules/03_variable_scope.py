"""
Program 3: Variable Scope
Demonstrates Global and Local variable scope
"""

# Global variable
global_var = "I am global"

def function1():
    """Function accessing global variable"""
    print(f"Inside function1: {global_var}")

function1()
print(f"Outside function: {global_var}")

# Local variable
def function2():
    """Function with local variable"""
    local_var = "I am local"
    print(f"Inside function2: {local_var}")

function2()
# print(local_var)  # This would cause NameError

# Global keyword to modify global variable
counter = 0

def increment_counter():
    global counter
    counter += 1
    print(f"Counter inside function: {counter}")

print(f"Counter before: {counter}")
increment_counter()
increment_counter()
print(f"Counter after: {counter}")

# Local and global variables with same name
x = "I am global"

def function3():
    x = "I am local"
    print(f"Inside function3: {x}")

function3()
print(f"Outside function: {x}")

# Nested function scope (Enclosing scope)
def outer_function():
    outer_var = "I am in outer function"
    
    def inner_function():
        inner_var = "I am in inner function"
        print(f"Inner accessing outer: {outer_var}")
        print(f"Inner accessing inner: {inner_var}")
    
    inner_function()
    print(f"Outer accessing outer: {outer_var}")

outer_function()

# LEGB Rule demonstration
# Local -> Enclosing -> Global -> Built-in
global_var2 = "Global"

def outer():
    enclosing_var = "Enclosing"
    
    def inner():
        local_var = "Local"
        print(f"Local: {local_var}")
        print(f"Enclosing: {enclosing_var}")
        print(f"Global: {global_var2}")
        print(f"Built-in: {len([1, 2, 3])}")
    
    inner()

outer()

# Nonlocal keyword (for enclosing scope)
def outer_function2():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    print(f"First call: {increment()}")
    print(f"Second call: {increment()}")
    print(f"Third call: {increment()}")

outer_function2()

# Default argument mutable object issue (related to scope/binding)
def add_to_list(item, items=[]):
    items.append(item)
    return items

print(f"\nMutable default argument issue:")
print(add_to_list(1))  # [1]
print(add_to_list(2))  # [1, 2] - unexpected!
print(add_to_list(3))  # [1, 2, 3] - unexpected!

# Correct way to handle mutable default arguments
def add_to_list_correct(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(f"\nCorrect way:")
print(add_to_list_correct(1))  # [1]
print(add_to_list_correct(2))  # [2]
print(add_to_list_correct(3))  # [3]
