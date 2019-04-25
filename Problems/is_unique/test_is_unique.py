#!/usr/bin/env python3

import unittest
import is_unique as iu


class TestIsUnique(unittest.TestCase):

    def test_is_unique_hash(self):

        # Positive tests.
        self.assertTrue(iu.is_unique_hash(''))
        self.assertTrue(iu.is_unique_hash('a'))
        self.assertTrue(iu.is_unique_hash('ab'))
        self.assertTrue(iu.is_unique_hash('abc'))

        # Negative tests.
        self.assertFalse(iu.is_unique_hash('aa'))
        self.assertFalse(iu.is_unique_hash('aba'))
        self.assertFalse(iu.is_unique_hash('aab'))
        self.assertFalse(iu.is_unique_hash('baa'))


    def test_is_unique_sort(self):

        # Positive tests.
        self.assertTrue(iu.is_unique_sort(''))
        self.assertTrue(iu.is_unique_sort('a'))
        self.assertTrue(iu.is_unique_sort('ab'))
        self.assertTrue(iu.is_unique_sort('abc'))

        # Negative tests.
        self.assertFalse(iu.is_unique_sort('aa'))
        self.assertFalse(iu.is_unique_sort('aba'))
        self.assertFalse(iu.is_unique_sort('aab'))
        self.assertFalse(iu.is_unique_sort('baa'))


    def test_is_unique_bruteforce(self):

        # Positive tests.
        self.assertTrue(iu.is_unique_bruteforce(''))
        self.assertTrue(iu.is_unique_bruteforce('a'))
        self.assertTrue(iu.is_unique_bruteforce('ab'))
        self.assertTrue(iu.is_unique_bruteforce('abc'))

        # Negative tests.
        self.assertFalse(iu.is_unique_bruteforce('aa'))
        self.assertFalse(iu.is_unique_bruteforce('aba'))
        self.assertFalse(iu.is_unique_bruteforce('aab'))
        self.assertFalse(iu.is_unique_bruteforce('baa'))


if __name__ == '__main__':
    unittest.main()
