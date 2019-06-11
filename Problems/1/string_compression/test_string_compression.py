#!/usr/bin/env python3

import unittest
from string_compression import string_compression


class TestStringCompression(unittest.TestCase):

    def test_string_compression(self):

        self.assertEqual(string_compression(''), '')
        self.assertEqual(string_compression('aa'), 'aa')
        self.assertEqual(string_compression('aaa'), 'a3')
        self.assertEqual(string_compression('aab'), 'aab')
        self.assertEqual(string_compression('aaab'), 'aaab')
        self.assertEqual(string_compression('aaabb'), 'a3b2')
        self.assertEqual(string_compression('abcdef'), 'abcdef')
        self.assertEqual(string_compression('aabcccccaaa'), 'a2b1c5a3')


if __name__ == '__main__':
    unittest.main()
