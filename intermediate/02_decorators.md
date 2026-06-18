# Decorators

## Function Decorators

```python
import functools
import time

def timer(func):
    """Measure execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "done"
```

## Decorators with Arguments

```python
def retry(max_attempts: int = 3, delay: float = 1.0):
    """Retry a function on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"Attempt {attempt} failed: {e}. Retrying...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def fetch_data(url: str):
    # might fail sometimes
    pass
```

## Class Decorators

```python
def singleton(cls):
    """Ensure only one instance of a class exists."""
    instances = {}
    
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class Database:
    def __init__(self):
        self.connection = "connected"
```

## Built-in Decorators

```python
class MyClass:
    @staticmethod
    def utility_method():
        """No access to instance or class."""
        pass
    
    @classmethod
    def from_string(cls, data: str):
        """Alternative constructor."""
        return cls(*data.split(","))
    
    @property
    def computed_value(self):
        """Accessed like an attribute."""
        return self._value * 2
```
