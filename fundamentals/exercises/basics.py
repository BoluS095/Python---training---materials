"""
Python Fundamentals — Exercises
Author: Rafał Korzeniewski
Used in PyWaw workshops and professional training sessions.
"""


# === Exercise 1: FizzBuzz ===
# Print numbers 1-100. For multiples of 3 print "Fizz",
# for multiples of 5 print "Buzz", for both print "FizzBuzz".

def fizzbuzz(n: int) -> list[str]:
    """Return FizzBuzz results for numbers 1 to n."""
    # YOUR CODE HERE
    pass


# === Exercise 2: Word Counter ===
# Count the frequency of each word in a text.

def count_words(text: str) -> dict[str, int]:
    """Count word frequency in text (case-insensitive)."""
    # YOUR CODE HERE
    pass


# === Exercise 3: Matrix Transpose ===
# Transpose a matrix (list of lists).

def transpose(matrix: list[list]) -> list[list]:
    """Transpose a matrix."""
    # YOUR CODE HERE
    pass


# === Exercise 4: Flatten Nested List ===
# Flatten a deeply nested list into a single list.

def flatten(nested: list) -> list:
    """Flatten a nested list of arbitrary depth."""
    # YOUR CODE HERE
    pass


# === Exercise 5: Caesar Cipher ===
# Encrypt a message by shifting each letter by n positions.

def caesar_encrypt(text: str, shift: int) -> str:
    """Encrypt text using Caesar cipher."""
    # YOUR CODE HERE
    pass


def caesar_decrypt(text: str, shift: int) -> str:
    """Decrypt Caesar cipher text."""
    # YOUR CODE HERE
    pass


# === Tests ===
if __name__ == "__main__":
    # Test Exercise 1
    result = fizzbuzz(15)
    assert result[2] == "Fizz"     # 3
    assert result[4] == "Buzz"     # 5
    assert result[14] == "FizzBuzz"  # 15
    print("✅ Exercise 1 passed")

    # Test Exercise 2
    assert count_words("hello world hello") == {"hello": 2, "world": 1}
    print("✅ Exercise 2 passed")

    # Test Exercise 3
    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    print("✅ Exercise 3 passed")

    # Test Exercise 4
    assert flatten([1, [2, [3, 4], 5], 6]) == [1, 2, 3, 4, 5, 6]
    print("✅ Exercise 4 passed")

    # Test Exercise 5
    assert caesar_encrypt("hello", 3) == "khoor"
    assert caesar_decrypt("khoor", 3) == "hello"
    print("✅ Exercise 5 passed")

    print("\n🎉 All exercises passed!")
