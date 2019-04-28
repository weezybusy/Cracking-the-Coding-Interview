#!/usr/bin/env python3

"""
is_unique: implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
"""


# Time complexity:  O(n)
# Space complexity: O(n)
def is_unique_hash(s: str):
    letters = {}
    for letter in s:
        if letters.get(letter) is None:
            letters[letter] = 1
        else:
            return False
    return True


# Time complexity:  O(n*log(n))
# Space complexity: O(1)
def is_unique_sort(s: str):
    s2 = sorted(s)
    for i in range(len(s2) - 1):
        if s2[i] == s2[i+1]:
            return False
    return True


# Time complexity:  O(n^2)
# Space complexity: O(1)
def is_unique_bruteforce(s: str):
    length = len(s)
    for i in range(length-1):
        for j in range(i+1, length):
            if s[i] == s[j]:
                return False
    return True
