#!/usr/bin/env python3

"""
One Away: There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character. Given two
strings, write a function to check if they are one edit (or zero edits)
away.

EXAMPLE:
    pale,  ple  -> true
    pales, pale -> true
    pale,  bale -> true
    pale,  bae  -> false
"""


# n = len(s1), m = len(s2).
# Time complexity:  O(n + m).
# Space complexity: O(max(n, m)).
def one_away(s1: str, s2: str):

    if s1 == s2:
        return True

    difference = abs(len(s1) - len(s2))
    if difference > 1:
        return False

    changes = 0
    letters = {}

    for ch in s1:
        if letters.get(ch) is None:
            letters[ch] = 1
        else:
            letters[ch] += 1

    for ch in s2:
        if letters.get(ch) is None:
            changes += 1
        else:
            if letters.get(ch) == 1:
                letters.pop(ch)
            else:
                letters[ch] -= 1
        if changes > 1:
            return False

    if len(letters) > 0 and difference > 0:
        changes += 1

    return changes == 1
