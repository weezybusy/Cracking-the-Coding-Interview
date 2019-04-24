#!/usr/bin/env python3

import unittest
import is_unique


class TestIsUnique(unittest.TestCase):

    def test_is_unique_hash(self):
        self.assertTrue(is_unique.is_unique_hash(''))
        self.assertTrue(is_unique.is_unique_hash('a'))
        self.assertTrue(is_unique.is_unique_hash('ab'))
        self.assertTrue(is_unique.is_unique_hash('abc'))
        self.assertFalse(is_unique.is_unique_hash('aa'))
        self.assertFalse(is_unique.is_unique_hash('aba'))
        self.assertFalse(is_unique.is_unique_hash('aab'))
        self.assertFalse(is_unique.is_unique_hash('baa'))

    def test_is_unique_sort(self):
        self.assertTrue(is_unique.is_unique_sort(''))
        self.assertTrue(is_unique.is_unique_sort('a'))
        self.assertTrue(is_unique.is_unique_sort('ab'))
        self.assertTrue(is_unique.is_unique_sort('abc'))
        self.assertFalse(is_unique.is_unique_sort('aa'))
        self.assertFalse(is_unique.is_unique_sort('aba'))
        self.assertFalse(is_unique.is_unique_sort('aab'))
        self.assertFalse(is_unique.is_unique_sort('baa'))

    def test_is_unique_bruteforce(self):
        self.assertTrue(is_unique.is_unique_bruteforce(''))
        self.assertTrue(is_unique.is_unique_bruteforce('a'))
        self.assertTrue(is_unique.is_unique_bruteforce('ab'))
        self.assertTrue(is_unique.is_unique_bruteforce('abc'))
        self.assertFalse(is_unique.is_unique_bruteforce('aa'))
        self.assertFalse(is_unique.is_unique_bruteforce('aba'))
        self.assertFalse(is_unique.is_unique_bruteforce('aab'))
        self.assertFalse(is_unique.is_unique_bruteforce('baa'))


if __name__ == '__main__':
    unittest.main()
