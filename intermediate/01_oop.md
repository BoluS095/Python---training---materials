# Object-Oriented Programming in Python

## Classes and Objects

```python
class User:
    """A user in our system."""
    
    # Class variable
    user_count = 0
    
    def __init__(self, name: str, email: str):
        # Instance variables
        self.name = name
        self.email = email
        self._created_at = datetime.now()  # "private" by convention
        User.user_count += 1
    
    def __repr__(self) -> str:
        return f"User(name={self.name!r}, email={self.email!r})"
    
    def __str__(self) -> str:
        return self.name
    
    def greet(self) -> str:
        return f"Hi, I'm {self.name}"


# Usage
user = User("Jan", "jan@example.com")
print(user.greet())
print(f"Total users: {User.user_count}")
```

## Inheritance

```python
class Employee(User):
    def __init__(self, name: str, email: str, department: str):
        super().__init__(name, email)
        self.department = department
    
    def greet(self) -> str:
        return f"Hi, I'm {self.name} from {self.department}"


class Manager(Employee):
    def __init__(self, name: str, email: str, department: str):
        super().__init__(name, email, department)
        self.reports: list[Employee] = []
    
    def add_report(self, employee: Employee):
        self.reports.append(employee)
```

## Properties

```python
class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius
    
    @property
    def celsius(self) -> float:
        return self._celsius
    
    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9/5 + 32
```

## Protocols (Structural Subtyping)

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str: ...

class Circle:
    def draw(self) -> str:
        return "○"

class Square:
    def draw(self) -> str:
        return "□"

def render(shape: Drawable) -> None:
    print(shape.draw())

# No inheritance needed — just implement the method
render(Circle())  # Works!
render(Square())  # Works!
```

## Dataclasses

```python
from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    tags: list[str] = field(default_factory=list)
    
    @property
    def price_with_vat(self) -> float:
        return self.price * 1.23  # Polish VAT

# Auto-generates __init__, __repr__, __eq__
p = Product("Laptop", 3999.99, ["electronics", "computers"])
```
