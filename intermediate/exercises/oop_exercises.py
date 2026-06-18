"""
OOP & Decorators — Exercises
Author: Rafał Korzeniewski
"""
from dataclasses import dataclass


# === Exercise 1: Bank Account ===
# Create a BankAccount class with deposit, withdraw, and balance.
# Withdrawals should not allow negative balance.

class BankAccount:
    """A simple bank account."""
    # YOUR CODE HERE
    pass


# === Exercise 2: Shape Hierarchy ===
# Create an abstract Shape class with area() and perimeter().
# Implement Circle and Rectangle.

# YOUR CODE HERE


# === Exercise 3: Cache Decorator ===
# Write a decorator that caches function results.

def cache(func):
    """Cache decorator — store results of previous calls."""
    # YOUR CODE HERE
    pass


# === Exercise 4: Validated Dataclass ===
# Create a dataclass for an email message with validation.

@dataclass
class Email:
    """Email message with validation."""
    # YOUR CODE HERE
    pass


# === Tests ===
if __name__ == "__main__":
    # Test Exercise 1
    account = BankAccount("Jan", 1000)
    account.deposit(500)
    assert account.balance == 1500
    account.withdraw(200)
    assert account.balance == 1300
    try:
        account.withdraw(2000)
        assert False, "Should raise ValueError"
    except ValueError:
        pass
    print("✅ Exercise 1 passed")

    print("\n🎉 All exercises passed!")
