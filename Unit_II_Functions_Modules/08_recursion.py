"""
Program 8: Recursion
Demonstrates recursive functions with base cases and examples
"""

print("=== FACTORIAL USING RECURSION ===")
def factorial(n):
    """Calculate factorial using recursion"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

for i in range(6):
    print(f"factorial({i}) = {factorial(i)}")

print("\n=== FIBONACCI USING RECURSION ===")
def fibonacci(n):
    """Calculate nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci sequence (first 10):")
for i in range(10):
    print(fibonacci(i), end=" ")
print()

print("\n=== SUM OF DIGITS USING RECURSION ===")
def sum_of_digits(n):
    """Calculate sum of digits"""
    if n < 10:
        return n
    return (n % 10) + sum_of_digits(n // 10)

number = 12345
print(f"Sum of digits in {number}: {sum_of_digits(number)}")

print("\n=== POWER FUNCTION USING RECURSION ===")
def power(base, exp):
    """Calculate base^exp using recursion"""
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power(base, exp - 1)

print(f"power(2, 5) = {power(2, 5)}")
print(f"power(3, 4) = {power(3, 4)}")

print("\n=== REVERSE STRING USING RECURSION ===")
def reverse_string(s):
    """Reverse a string using recursion"""
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])

text = "Python"
print(f"Original: {text}")
print(f"Reversed: {reverse_string(text)}")

print("\n=== PALINDROME CHECK USING RECURSION ===")
def is_palindrome(s):
    """Check if string is palindrome using recursion"""
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

test_strings = ["racecar", "hello", "madam", "noon", "python"]
for s in test_strings:
    print(f"'{s}' is palindrome: {is_palindrome(s)}")

print("\n=== BINARY SEARCH USING RECURSION ===")
def binary_search(arr, target, low, high):
    """Binary search using recursion"""
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7
result = binary_search(sorted_array, target, 0, len(sorted_array) - 1)
print(f"Array: {sorted_array}")
print(f"Target: {target}")
print(f"Index: {result}")

print("\n=== GCD USING RECURSION (EUCLIDEAN ALGORITHM) ===")
def gcd(a, b):
    """Calculate GCD using Euclidean algorithm"""
    if b == 0:
        return a
    return gcd(b, a % b)

print(f"GCD(48, 18) = {gcd(48, 18)}")
print(f"GCD(100, 50) = {gcd(100, 50)}")

print("\n=== TOWERS OF HANOI ===")
def hanoi(n, source, destination, auxiliary):
    """Solve Tower of Hanoi problem"""
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n - 1, auxiliary, destination, source)

print("Tower of Hanoi (3 disks):")
hanoi(3, 'A', 'C', 'B')

print("\n=== TREE TRAVERSAL USING RECURSION ===")
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):
    """In-order traversal of binary tree"""
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.value, end=" ")
    inorder_traversal(node.right)

# Create a simple binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("In-order traversal: ", end="")
inorder_traversal(root)
print()
