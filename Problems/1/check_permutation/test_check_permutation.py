#!/usr/bin/env python3

import unittest
from check_permutation import check_permutation_sort, check_permutation_hash, \
        check_permutation_list


class TestCheckPermutation(unittest.TestCase):

    def test_check_permutation_sort(self):
        # Positive tests.
        self.assertTrue(check_permutation_sort('', ''))
        self.assertTrue(check_permutation_sort('a', 'a'))
        self.assertTrue(check_permutation_sort('ab', 'ab'))
        self.assertTrue(check_permutation_sort('ab', 'ba'))
        self.assertTrue(check_permutation_sort('ba', 'ab'))
        self.assertTrue(check_permutation_sort('abc', 'abc'))
        self.assertTrue(check_permutation_sort('abc', 'acb'))
        self.assertTrue(check_permutation_sort('abc', 'cab'))
        self.assertTrue(check_permutation_sort('abc', 'cba'))
        self.assertTrue(check_permutation_sort('abc', 'bca'))
        self.assertTrue(check_permutation_sort('abc', 'bac'))
        self.assertTrue(check_permutation_sort('aac', 'aca'))
        self.assertTrue(check_permutation_sort('aaaa', 'aaaa'))

        # Negative tests.
        self.assertFalse(check_permutation_sort('', 'a'))
        self.assertFalse(check_permutation_sort('a', ''))
        self.assertFalse(check_permutation_sort('ab', 'a'))
        self.assertFalse(check_permutation_sort('a', 'ab'))
        self.assertFalse(check_permutation_sort('aa', 'ab'))
        self.assertFalse(check_permutation_sort('abc', 'aabc'))
        self.assertFalse(check_permutation_sort('aabc', 'abc'))
        self.assertFalse(check_permutation_sort('abc', 'aac'))
        self.assertFalse(check_permutation_sort('ccc', 'cac'))


    def test_check_permutation_hash(self):
        # Positive tests.
        self.assertTrue(check_permutation_hash('', ''))
        self.assertTrue(check_permutation_hash('a', 'a'))
        self.assertTrue(check_permutation_hash('ab', 'ab'))
        self.assertTrue(check_permutation_hash('ab', 'ba'))
        self.assertTrue(check_permutation_hash('ba', 'ab'))
        self.assertTrue(check_permutation_hash('abc', 'abc'))
        self.assertTrue(check_permutation_hash('abc', 'acb'))
        self.assertTrue(check_permutation_hash('abc', 'cab'))
        self.assertTrue(check_permutation_hash('abc', 'cba'))
        self.assertTrue(check_permutation_hash('abc', 'bca'))
        self.assertTrue(check_permutation_hash('abc', 'bac'))
        self.assertTrue(check_permutation_hash('aac', 'aca'))
        self.assertTrue(check_permutation_hash('aaaa', 'aaaa'))

        # Negative tests.
        self.assertFalse(check_permutation_hash('', 'a'))
        self.assertFalse(check_permutation_hash('a', ''))
        self.assertFalse(check_permutation_hash('ab', 'a'))
        self.assertFalse(check_permutation_hash('a', 'ab'))
        self.assertFalse(check_permutation_hash('aa', 'ab'))
        self.assertFalse(check_permutation_hash('abc', 'aabc'))
        self.assertFalse(check_permutation_hash('aabc', 'abc'))
        self.assertFalse(check_permutation_hash('abc', 'aac'))
        self.assertFalse(check_permutation_hash('ccc', 'cac'))


    def test_check_permutation_list(self):
        # Positive tests.
        self.assertTrue(check_permutation_list('', ''))
        self.assertTrue(check_permutation_list('a', 'a'))
        self.assertTrue(check_permutation_list('ab', 'ab'))
        self.assertTrue(check_permutation_list('ab', 'ba'))
        self.assertTrue(check_permutation_list('ba', 'ab'))
        self.assertTrue(check_permutation_list('abc', 'abc'))
        self.assertTrue(check_permutation_list('abc', 'acb'))
        self.assertTrue(check_permutation_list('abc', 'cab'))
        self.assertTrue(check_permutation_list('abc', 'cba'))
        self.assertTrue(check_permutation_list('abc', 'bca'))
        self.assertTrue(check_permutation_list('abc', 'bac'))
        self.assertTrue(check_permutation_list('aac', 'aca'))
        self.assertTrue(check_permutation_list('aaaa', 'aaaa'))

        # Negative tests.
        self.assertFalse(check_permutation_list('', 'a'))
        self.assertFalse(check_permutation_list('a', ''))
        self.assertFalse(check_permutation_list('ab', 'a'))
        self.assertFalse(check_permutation_list('a', 'ab'))
        self.assertFalse(check_permutation_list('aa', 'ab'))
        self.assertFalse(check_permutation_list('abc', 'aabc'))
        self.assertFalse(check_permutation_list('aabc', 'abc'))
        self.assertFalse(check_permutation_list('abc', 'aac'))
        self.assertFalse(check_permutation_list('ccc', 'cac'))


if __name__ == '__main__':
    unittest.main()
