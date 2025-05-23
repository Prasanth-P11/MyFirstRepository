import pytest

from empty6 import palindrome


def test_palindrome_valid():
    assert palindrome(121) == "this is palindrome"
    assert palindrome(123) == "Not a palindrome"


def test_palindrome_invalid():
    assert palindrome("abc") == "Invalid input"
    assert palindrome("12.34") == "Invalid input"
