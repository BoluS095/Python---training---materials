# Functions

## Defining Functions

```python
def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

# Call it
message = greet("Rafał")
```

## Arguments

```python
# Positional and keyword
def create_user(name, age, city="Warsaw"):
    return {"name": name, "age": age, "city": city}

create_user("Jan", 25)
create_user("Jan", 25, city="Kraków")

# *args and **kwargs
def log(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

log(1, 2, 3, level="INFO", source="app")

# Positional-only (/) and keyword-only (*)
def divide(a, b, /, *, round_result=False):
    result = a / b
    return round(result) if round_result else result
```

## Lambda Functions

```python
# Short anonymous functions
square = lambda x: x ** 2
add = lambda a, b: a + b

# Common use: sorting
users = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_users = sorted(users, key=lambda u: u[1])
```

## Scope and Closures

```python
# LEGB rule: Local → Enclosing → Global → Built-in

x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)  # "local"
    
    inner()
    print(x)  # "enclosing"

# Closure
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
double(5)  # 10
```

## Decorators Preview

```python
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.2f}s")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
```
