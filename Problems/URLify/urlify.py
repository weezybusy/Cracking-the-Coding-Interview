#!/usr/bin/env python3

"""
URLify: write a method to replace all spaces in a string with '%20': You may
assume that the string has sufficient space at the end to hold the additional
characters, and that you are given the "true" length of the string.
(Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)

EXAMPLE:
    Input:  "Mr John Smith    ", 13
    Output: "Mr%20John%20Smith"
"""

# Time complexity:  O(n^2)
# Space complexity: O(1)
def urlify(s: list, n: int):
    spaces = s[:n].count(' ')
    length = n + 2 * spaces
    shift = 2
    for i in range(length):
        if s[i] == ' ':
            for j in range(1, n-i):
                s[n-j+shift] = s[n-j]
            s[i] = '%'
            s[i+1] = '2'
            s[i+2] = '0'
            i += shift
            n += shift


# Time complexity:  O(n)
# Space complexity: O(1)
def urlify_better(s: list, n: int):
    spaces = s[:n].count(' ')
    index = n + spaces * 2
    for i in reversed(range(n)):
        if s[i] == ' ':
            s[index-1] = '0'
            s[index-2] = '2'
            s[index-3] = '%'
            index -= 3
        else:
            s[index-1] = s[i]
            index -= 1
