#!/usr/bin/env python3

"""
is_unique: implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
"""


# TODO: write unit tests


def main():
    strings = ['Hello, World', 'Hello', 'World', 'Good', 'Friend']
    functions = [is_unique_hash, is_unique_sort, is_unique_bruteforce]
    for f in functions:
        for s in strings:
            if f(s):
                print('{:<15} -> unique'.format(s))
            else:
                print('{:<15} -> not unique'.format(s))


# Growth rate: O(n)
def is_unique_hash(s):
    letters = {}
    for letter in s:
        if letters.get(letter) != None:
            return False
        letters[letter] = 1
    return True


# Growth rate: O(n*log(n))
def is_unique_sort(s):
    s2 = sorted(s)
    for i in range(len(s2) - 1):
        if s2[i] == s2[i+1]:
            return False
    return True


# Growth rate: O(n^2)
def is_unique_bruteforce(s):
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True


if __name__ == '__main__':
    main()
