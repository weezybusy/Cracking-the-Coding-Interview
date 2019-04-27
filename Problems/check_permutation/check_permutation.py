#!/usr/bin/env python3

"""
check_permutation: given two strings, write a method to decide if one is a
permutation of the other.
"""


# Time complaxity: O(nlogn)
def check_permutation_sort(s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


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

def check_permutation_list(s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    letters1 = [0] * 128
    letters2 = [0] * 128
    for letter in s1:
        letters1[ord(letter)] += 1
    for letter in s2:
        letters2[ord(letter)] += 1
    return letters1 == letters2
