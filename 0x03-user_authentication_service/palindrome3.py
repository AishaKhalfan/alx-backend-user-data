#!/usr/bin/env python3
def is_palindrome(num):
    """
    Convert to list and compare:
    """
    num_list = list(str(num))
    return num_list == num_list[::-1] 

print(is_palindrome(9009)) # Tru
