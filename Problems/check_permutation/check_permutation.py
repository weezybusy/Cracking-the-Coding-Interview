#!/usr/bin/env python3

"""
check_permutation: given two strings, write a method to decide if one is a
permutation of the other.
"""


# Time complaxity: O(nlogn)
def check_permutation_sort(s1: str, s2: str):
    length = len(s1)
    if length != len(s2):
            return False
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)
    for i in range(length):
        if s1_sorted[i] != s2_sorted[i]:
            return False
    return True


# Time complaxity: O(n)
def check_permutation_hash(s1: str, s2: str):
    if len(s1) != len(s2):
            return False
    letters = {}
    for letter in s1:
        if letters.get(letter) is None:
            letters[letter] = 0
        letters[letter] += 1
    for letter in s2:
        if letters.get(letter) is None:
            return False
        elif letters[letter] > 1:
            letters[letter] -= 1
        else:
            letters.pop(letter)
    return True
