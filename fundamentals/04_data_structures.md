# Data Structures

## Lists

```python
# Creation
fruits = ["apple", "banana", "cherry"]
numbers = list(range(1, 11))

# Access
first = fruits[0]       # "apple"
last = fruits[-1]       # "cherry"
slice_ = fruits[1:3]    # ["banana", "cherry"]

# Modification
fruits.append("date")
fruits.insert(1, "avocado")
fruits.remove("banana")
popped = fruits.pop()

# Useful methods
fruits.sort()
fruits.reverse()
count = fruits.count("apple")
index = fruits.index("cherry")
```

## Dictionaries

```python
# Creation
user = {"name": "Jan", "age": 25, "city": "Warsaw"}
user = dict(name="Jan", age=25, city="Warsaw")

# Access
name = user["name"]
age = user.get("age", 0)  # with default

# Modification
user["email"] = "jan@example.com"
user.update({"age": 26, "phone": "123456"})
del user["phone"]

# Iteration
for key in user:
    print(key)

for key, value in user.items():
    print(f"{key}: {value}")

# Useful methods
keys = user.keys()
values = user.values()
items = user.items()
user.setdefault("country", "Poland")
```

## Sets

```python
# Creation
colors = {"red", "green", "blue"}
numbers = set([1, 2, 3, 2, 1])  # {1, 2, 3}

# Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b    # union: {1, 2, 3, 4, 5, 6}
a & b    # intersection: {3, 4}
a - b    # difference: {1, 2}
a ^ b    # symmetric difference: {1, 2, 5, 6}

# Membership test (O(1) average)
"red" in colors  # True
```

## Tuples

```python
# Immutable sequences
point = (3, 4)
x, y = point  # unpacking

# Named tuples
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)
```

## When to Use What

| Structure | Use When |
|-----------|----------|
| `list` | Ordered, mutable collection |
| `dict` | Key-value lookups |
| `set` | Unique items, membership testing |
| `tuple` | Immutable sequences, dict keys |
