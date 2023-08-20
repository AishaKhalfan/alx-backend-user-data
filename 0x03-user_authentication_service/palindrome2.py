#!/usr/bin/env python3
def is_palindrome(num):
    """
    Convert to string and compare reversing
    """
    string = str(num)
    return string == string[::-1]

print(is_palindrome(1234321)) # True
print(is_palindrome(123456)) # False
