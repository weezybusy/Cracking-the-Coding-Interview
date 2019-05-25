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
# Time complexity:  O(max(n, m)).
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


def one_away_alt(s1: str, s2: str):
    difference = len(s1) - len(s2)
    if difference == 0:
        return one_replace(s1, s2)
    elif difference + 1 == 0:
        return one_insert(s1, s2)
    elif difference - 1 == 0:
        return one_insert(s2, s1)
    print('too big: ', end='')
    return False


def one_replace(s1: str, s2: str):
    print('replace: ', end='')
    found_difference = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if found_difference:
                return False
            found_difference = True
    return True


def one_insert(s1: str, s2: str):
    print('insert/delete: ', end='')
    i = 0
    j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if i != j:
                return False
            j += 1
        else:
            i += 1
            j += 1
    return True


print(one_away_alt('sale', 'sale'))
print(one_away_alt('sale', 'sal'))
print(one_away_alt('sale', 'gale'))
print(one_away_alt('sale', 'gole'))
print(one_away_alt('sale', 'soledo'))
