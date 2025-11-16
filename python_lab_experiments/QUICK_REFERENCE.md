# Quick Reference Guide - Python Lab Experiments

## Program Execution Quick Start

Run any program using:
```bash
python program_name.py
```

## Programs by Category

### Data Types & Variables (01-03)
| Program | Topic | Key Concepts |
|---------|-------|--------------|
| 01 | Numbers | int, float, arithmetic operations |
| 02 | Strings | string methods, concatenation, indexing |
| 03 | Collections | tuple, list, dictionary operations |

### Arithmetic & Data Conversion (04-05)
| Program | Topic | Key Concepts |
|---------|-------|--------------|
| 04 | Currency Conversion | float conversion, mathematical operations |
| 05 | Data Size Conversion | unit conversion, bit/byte relationships |

### Geometry (06-07)
| Program | Topic | Formula |
|---------|-------|---------|
| 06 | Square | Area = side², Perimeter = 4×side |
| 07 | Cone | Volume = ⅓πr²h, Lateral Area = πrl |

### Conditionals (08-09)
| Program | Topic | Operators |
|---------|-------|-----------|
| 08 | Odd/Even | Modulus (%), if-else |
| 09 | Greatest of Three | Comparison (>, >=), nested if |

### Loops (10-11)
| Program | Topic | Pattern |
|---------|-------|---------|
| 10 | Factorial | Loop from 1 to n, multiply all |
| 11 | Multiplication | Nested loops for table generation |

### Functions (12-13)
| Program | Topic | Concepts |
|---------|-------|----------|
| 12 | Factorial Function | def, return, parameters |
| 13 | Table Function | Functions with loop logic |

### Recursion (14-15)
| Program | Topic | Pattern |
|---------|-------|---------|
| 14 | Factorial Recursion | Base case: n≤1; Recursive: n×fac(n-1) |
| 15 | Fibonacci | Base: F(0)=0, F(1)=1; Recursive: F(n-1)+F(n-2) |

### List Operations (16-17)
| Program | Operations | Methods |
|---------|------------|---------|
| 16 | Create, Add, Delete | append(), insert(), remove(), pop() |
| 17 | Sort, Reverse, Count | sorted(), reverse(), count(), len() |

### Dictionary (18)
| Operation | Syntax |
|-----------|--------|
| Create | `{key: value, ...}` |
| Add | `dict[key] = value` |
| Access | `dict[key]` or `dict.get(key)` |
| Delete | `del dict[key]` or `dict.pop(key)` |
| Iterate | `for key in dict:` or `for k,v in dict.items():` |

### Statistics (19)
| Metric | Method |
|--------|--------|
| Mean | `sum(data) / len(data)` |
| Median | Middle value when sorted |
| Std Dev | `√(Σ(x-mean)² / n)` |
| Using Module | `import statistics` |

### Factors (20)
| Concept | Method |
|---------|--------|
| All Factors | Loop from 1 to n, check divisibility |
| Prime Factors | Filter factors that are prime |
| Factor Pairs | Find (a,b) where a×b = n |

### File I/O (21-22)
| Mode | Operation |
|------|-----------|
| 'r' | Read file |
| 'w' | Write (overwrites) |
| 'a' | Append to file |
| Methods | open(), read(), write(), close() |

### Classes & Objects (23-25)
| Program | Concept |
|---------|---------|
| 23 | Class definition, object creation, methods |
| 24 | Multiple operations in classes |
| 25 | Modules, packages, imports |

## Common Python Patterns

### Loop Pattern
```python
for i in range(1, n+1):
    # do something with i
```

### Function Pattern
```python
def function_name(parameters):
    """Docstring"""
    # function body
    return result
```

### Class Pattern
```python
class ClassName:
    def __init__(self, parameter):
        self.attribute = parameter
    
    def method(self):
        return something
```

### File Pattern
```python
with open('filename', 'mode') as file:
    # work with file
    # automatically closes
```

### Exception Handling
```python
try:
    # risky code
except ValueError:
    # handle error
```

## Important Operators

### Arithmetic
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `//` Floor Division
- `%` Modulus
- `**` Power

### Comparison
- `==` Equal to
- `!=` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater or equal
- `<=` Less or equal

### Logical
- `and` Both conditions true
- `or` Either condition true
- `not` Negation

### Membership
- `in` Check if element in collection
- `not in` Check if element not in collection

## String Methods
- `.upper()` → Uppercase
- `.lower()` → Lowercase
- `.capitalize()` → First letter capital
- `.replace(old, new)` → Replace text
- `.split()` → Split into list
- `.join()` → Join list into string
- `.count(char)` → Count occurrences
- `.index(char)` → Find position

## List Methods
- `.append(item)` → Add at end
- `.insert(index, item)` → Add at position
- `.remove(item)` → Remove by value
- `.pop(index)` → Remove by index
- `.sort()` → Sort in place
- `.reverse()` → Reverse in place
- `.count(item)` → Count occurrences
- `.index(item)` → Find position

## Dictionary Methods
- `.keys()` → Get all keys
- `.values()` → Get all values
- `.items()` → Get key-value pairs
- `.get(key, default)` → Get with default
- `.pop(key)` → Remove and return
- `.update(dict)` → Merge dictionaries
- `.clear()` → Remove all items

## Useful Built-in Functions
- `len(obj)` → Length
- `sum(iterable)` → Sum of elements
- `max(iterable)` → Maximum value
- `min(iterable)` → Minimum value
- `sorted(iterable)` → Sorted list
- `reversed(iterable)` → Reversed iterator
- `type(obj)` → Data type
- `range(start, end, step)` → Number sequence
- `enumerate(iterable)` → Index and value
- `zip(list1, list2)` → Pair elements

## Quick Tips

1. **Use meaningful variable names** - `student_name` instead of `sn`
2. **Add comments** - Explain complex logic
3. **Test incrementally** - Run code as you write it
4. **Handle errors** - Use try-except blocks
5. **Keep functions simple** - Do one thing well
6. **Use list comprehensions** - `[x*2 for x in range(5)]`
7. **Document functions** - Use docstrings
8. **DRY principle** - Don't Repeat Yourself

## Debugging Tips

- Use `print()` to check variable values
- Use `type()` to check data types
- Use `len()` to check collection sizes
- Check indentation for syntax errors
- Read error messages carefully
- Break large problems into smaller ones

---

**Created for 10th Class Python Programming Laboratory**
