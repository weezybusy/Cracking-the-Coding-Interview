#!/usr/bin/env python3

"""
Palindrome Permutation: Given a string, write a function to check if it is a
permutation of a palindrome. A palindrome is a word or phrase that is the
same forwards and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

EXAMPLE:
    Input:  Tact Coa
    Output: True (permutations: "taco cat", "atco cta", etc.)
"""

# Time complexity:  O(n).
# Space complexity: O(1).
def palindrome_permutation(phrase: str):
    size = ord('z') - ord('a') + 1
    table = [0] * size
    for ch in phrase.lower():
        if ch.isalpha():
            index = ord(ch) - ord('a')
            table[index] = 1 - table[index]
    return sum(table) <= 1


# Time complexity:  O(n).
# Space complexity: O(1).
def palindrome_permutation_bit(phrase: str):
    bits = 0
    for ch in phrase.lower():
        if ch.isalpha():
            mask = 1 << (ord(ch) - ord('a'))
            if bits & mask:
                bits &= ~mask
            else:
                bits |= mask
    return (bits & (bits - 1)) == 0
