"""
Program 8: Collections - Counter, Heapq, Deque, OrderedDict, DefaultDict
Demonstrates specialized collection data structures
"""

from collections import Counter, deque, OrderedDict, defaultdict
import heapq

print("=== COUNTER ===")
# Count occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print(f"Words: {words}")
print(f"Counter: {word_count}")
print(f"Type: {type(word_count)}")

# Most common
print(f"Most common 2: {word_count.most_common(2)}")
print(f"Least common: {word_count.most_common()[::-1][:2]}")

# Count characters
text = "mississippi"
char_count = Counter(text)
print(f"\nText: {text}")
print(f"Character count: {char_count}")
print(f"Most common: {char_count.most_common(3)}")

# Counter arithmetic
c1 = Counter({"a": 3, "b": 1})
c2 = Counter({"a": 1, "b": 2})
print(f"\nc1: {c1}")
print(f"c2: {c2}")
print(f"c1 + c2: {c1 + c2}")
print(f"c1 - c2: {c1 - c2}")
print(f"c1 & c2 (intersection): {c1 & c2}")
print(f"c1 | c2 (union): {c1 | c2}")

print("\n=== DEQUE (Double Ended Queue) ===")
dq = deque([1, 2, 3])
print(f"Initial: {dq}")

# Append to both ends
dq.append(4)
print(f"After append(4): {dq}")
dq.appendleft(0)
print(f"After appendleft(0): {dq}")

# Pop from both ends
right = dq.pop()
print(f"After pop(): {dq}, popped: {right}")
left = dq.popleft()
print(f"After popleft(): {dq}, popped: {left}")

# Rotation
dq = deque([1, 2, 3, 4, 5])
print(f"Original: {dq}")
dq.rotate(2)
print(f"After rotate(2): {dq}")
dq.rotate(-2)
print(f"After rotate(-2): {dq}")

# Maximum length
dq = deque([1, 2, 3], maxlen=3)
print(f"Deque with maxlen=3: {dq}")
dq.append(4)
print(f"After append(4): {dq} (leftmost element dropped)")

print("\n=== HEAPQ (Min-Heap) ===")
numbers = [5, 2, 8, 1, 9, 3]
heap = numbers.copy()
heapq.heapify(heap)
print(f"Original: {numbers}")
print(f"As heap: {heap}")

# Find min
print(f"Min (heap[0]): {heap[0]}")

# Pop minimum
min_val = heapq.heappop(heap)
print(f"After heappop(): {heap}, popped: {min_val}")

# Push element
heapq.heappush(heap, 0)
print(f"After heappush(0): {heap}")

# N largest and smallest
numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]
print(f"\nNumbers: {numbers}")
print(f"3 largest: {heapq.nlargest(3, numbers)}")
print(f"3 smallest: {heapq.nsmallest(3, numbers)}")

# Using heap for sorting
data = [(2, 'b'), (1, 'a'), (3, 'c')]
heapq.heapify(data)
print(f"\nTuples sorted: {[heapq.heappop(data) for _ in range(len(data))]}")

print("\n=== ORDEREDDICT ===")
# In Python 3.7+, regular dict maintains insertion order
# But OrderedDict explicitly guarantees it

regular_dict = {"b": 2, "a": 1, "c": 3}
ordered_dict = OrderedDict([("b", 2), ("a", 1), ("c", 3)])

print(f"Regular dict: {regular_dict}")
print(f"OrderedDict: {ordered_dict}")

# Move to end
ordered_dict.move_to_end("a")
print(f"After move_to_end('a'): {ordered_dict}")
ordered_dict.move_to_end("a", last=False)
print(f"After move_to_end('a', False): {ordered_dict}")

# Reverse iteration
print(f"Reverse items: {list(reversed(ordered_dict.items()))}")

print("\n=== DEFAULTDICT ===")
# With int default
int_dict = defaultdict(int)
int_dict["a"] += 1
int_dict["a"] += 1
int_dict["b"] += 1
print(f"DefaultDict(int): {dict(int_dict)}")

# With list default
list_dict = defaultdict(list)
list_dict["a"].append(1)
list_dict["a"].append(2)
list_dict["b"].append(3)
print(f"DefaultDict(list): {dict(list_dict)}")

# With set default
set_dict = defaultdict(set)
set_dict["a"].add(1)
set_dict["a"].add(2)
set_dict["b"].add(1)
print(f"DefaultDict(set): {dict(set_dict)}")

# With custom default function
def default_value():
    return "No value set"

custom_dict = defaultdict(default_value)
print(f"DefaultDict(custom): {custom_dict['unknown']}")

print("\n=== PRACTICAL EXAMPLES ===")
# Count word frequency
text = "the quick brown fox jumps over the lazy dog"
words = text.split()
freq = Counter(words)
print(f"Text: {text}")
print(f"Word frequency: {freq}")

# Priority queue using heapq
tasks = [(3, "Task C"), (1, "Task A"), (2, "Task B")]
heapq.heapify(tasks)
print(f"Tasks in priority order:")
while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"  Priority {priority}: {task}")

# Using defaultdict for grouping
students = [("Math", "Alice"), ("Math", "Bob"), ("English", "Alice"), ("English", "Charlie")]
subjects = defaultdict(list)
for subject, student in students:
    subjects[subject].append(student)
print(f"\nStudents grouped by subject: {dict(subjects)}")
