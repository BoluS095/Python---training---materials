# Variables and Types in Python

## Theory

Python is dynamically typed — you don't need to declare variable types explicitly.

### Basic Types

```python
# Numbers
age = 25              # int
price = 19.99         # float
complex_num = 3 + 4j  # complex

# Text
name = "Rafał"        # str
multiline = """This is
a multiline string"""

# Boolean
is_active = True      # bool
is_empty = False

# None
result = None         # NoneType
```

### Type Checking and Conversion

```python
# Check type
type(42)          # <class 'int'>
isinstance(42, int)  # True

# Convert between types
int("42")         # 42
float("3.14")     # 3.14
str(42)           # "42"
bool(0)           # False
bool(1)           # True
bool("")          # False
bool("hello")     # True
```

### Variable Naming

```python
# Good names
user_name = "Jan"
total_price = 99.99
is_valid = True
MAX_RETRIES = 3  # constants by convention

# Bad names (but technically valid)
x = "Jan"
a1 = 99.99
```

## Key Concepts

1. **Everything is an object** — even integers and strings
2. **Variables are references** — they point to objects in memory
3. **Python uses duck typing** — "If it walks like a duck..."
4. **Convention: UPPER_CASE for constants** — Python doesn't enforce immutability

## Common Pitfalls

```python
# Mutable default arguments
def add_item(item, items=[]):  # DON'T do this
    items.append(item)
    return items

# Integer caching (-5 to 256)
a = 256
b = 256
a is b  # True (cached)

a = 257
b = 257
a is b  # May be False (not cached)
```
