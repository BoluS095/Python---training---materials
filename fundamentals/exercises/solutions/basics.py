"""
Python Fundamentals — Solutions
Author: Rafał Korzeniewski
"""


def fizzbuzz(n: int) -> list[str]:
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def count_words(text: str) -> dict[str, int]:
    words = text.lower().split()
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    return counter


def transpose(matrix: list[list]) -> list[list]:
    return [list(row) for row in zip(*matrix)]


def flatten(nested: list) -> list:
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def caesar_encrypt(text: str, shift: int) -> str:
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)


def caesar_decrypt(text: str, shift: int) -> str:
    return caesar_encrypt(text, -shift)


if __name__ == "__main__":
    result = fizzbuzz(15)
    assert result[2] == "Fizz"
    assert result[4] == "Buzz"
    assert result[14] == "FizzBuzz"
    print("✅ Exercise 1 passed")

    assert count_words("hello world hello") == {"hello": 2, "world": 1}
    print("✅ Exercise 2 passed")

    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    print("✅ Exercise 3 passed")

    assert flatten([1, [2, [3, 4], 5], 6]) == [1, 2, 3, 4, 5, 6]
    print("✅ Exercise 4 passed")

    assert caesar_encrypt("hello", 3) == "khoor"
    assert caesar_decrypt("khoor", 3) == "hello"
    print("✅ Exercise 5 passed")

    print("\n🎉 All exercises passed!")
