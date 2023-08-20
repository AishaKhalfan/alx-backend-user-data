#!/usr/bin/env python3

def is_palindrome(num):
    """
    Reverse the number and compare:
    """
    reverse = int(str(num)[::-1])
    return num == reverse

print(is_palindrome(1221)) # True
print(is_palindrome(120)) # False
