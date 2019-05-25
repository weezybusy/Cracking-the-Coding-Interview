#!/usr/bin/env python3

"""
String Compression: Implement a method to perform basic string compression
using the counts of repeated characters. For example, the string "aabcccccaaa"
would become "a2b1c5a3". If the "compressed" string would not become smaller
than the original string, your method should return the original string. You
can assume the string has only uppercase and lowercase letters (a-z).
"""


def string_compression(string):

    new_string = ''
    same_char_count = 1
    i = 0

    while i < len(string):
        ch = string[i]
        new_string += ch
        while i < len(string) - 1 and string[i+1] == ch:
            same_char_count += 1
            i += 1

        new_string += str(same_char_count)
        i += 1
        same_char_count = 1

    return new_string if len(new_string) < len(string) else string
