#!/usr/bin/env python3

import unittest
import check_permutation as cp


class TestCheckPermutation(unittest.TestCase):

    def test_check_permutation_sort(self):
        # Positive tests.
        self.assertTrue(cp.check_permutation_sort('', ''))
        self.assertTrue(cp.check_permutation_sort('a', 'a'))
        self.assertTrue(cp.check_permutation_sort('ab', 'ab'))
        self.assertTrue(cp.check_permutation_sort('ab', 'ba'))
        self.assertTrue(cp.check_permutation_sort('ba', 'ab'))
        self.assertTrue(cp.check_permutation_sort('abc', 'abc'))
        self.assertTrue(cp.check_permutation_sort('abc', 'acb'))
        self.assertTrue(cp.check_permutation_sort('abc', 'cab'))
        self.assertTrue(cp.check_permutation_sort('abc', 'cba'))
        self.assertTrue(cp.check_permutation_sort('abc', 'bca'))
        self.assertTrue(cp.check_permutation_sort('abc', 'bac'))
        self.assertTrue(cp.check_permutation_sort('aac', 'aca'))
        self.assertTrue(cp.check_permutation_sort('aaaa', 'aaaa'))

        # Negative tests.
        self.assertFalse(cp.check_permutation_sort('', 'a'))
        self.assertFalse(cp.check_permutation_sort('a', ''))
        self.assertFalse(cp.check_permutation_sort('ab', 'a'))
        self.assertFalse(cp.check_permutation_sort('a', 'ab'))
        self.assertFalse(cp.check_permutation_sort('aa', 'ab'))
        self.assertFalse(cp.check_permutation_sort('abc', 'aabc'))
        self.assertFalse(cp.check_permutation_sort('aabc', 'abc'))
        self.assertFalse(cp.check_permutation_sort('abc', 'aac'))
        self.assertFalse(cp.check_permutation_sort('ccc', 'cac'))


    def test_check_permutation_hash(self):
        # Positive tests.
        self.assertTrue(cp.check_permutation_hash('', ''))
        self.assertTrue(cp.check_permutation_hash('a', 'a'))
        self.assertTrue(cp.check_permutation_hash('ab', 'ab'))
        self.assertTrue(cp.check_permutation_hash('ab', 'ba'))
        self.assertTrue(cp.check_permutation_hash('ba', 'ab'))
        self.assertTrue(cp.check_permutation_hash('abc', 'abc'))
        self.assertTrue(cp.check_permutation_hash('abc', 'acb'))
        self.assertTrue(cp.check_permutation_hash('abc', 'cab'))
        self.assertTrue(cp.check_permutation_hash('abc', 'cba'))
        self.assertTrue(cp.check_permutation_hash('abc', 'bca'))
        self.assertTrue(cp.check_permutation_hash('abc', 'bac'))
        self.assertTrue(cp.check_permutation_hash('aac', 'aca'))
        self.assertTrue(cp.check_permutation_hash('aaaa', 'aaaa'))

        # Negative tests.
        self.assertFalse(cp.check_permutation_hash('', 'a'))
        self.assertFalse(cp.check_permutation_hash('a', ''))
        self.assertFalse(cp.check_permutation_hash('ab', 'a'))
        self.assertFalse(cp.check_permutation_hash('a', 'ab'))
        self.assertFalse(cp.check_permutation_hash('aa', 'ab'))
        self.assertFalse(cp.check_permutation_hash('abc', 'aabc'))
        self.assertFalse(cp.check_permutation_hash('aabc', 'abc'))
        self.assertFalse(cp.check_permutation_hash('abc', 'aac'))
        self.assertFalse(cp.check_permutation_hash('ccc', 'cac'))


    def test_check_permutation_list(self):
        # Positive tests.
        self.assertTrue(cp.check_permutation_list('', ''))
        self.assertTrue(cp.check_permutation_list('a', 'a'))
        self.assertTrue(cp.check_permutation_list('ab', 'ab'))
        self.assertTrue(cp.check_permutation_list('ab', 'ba'))
        self.assertTrue(cp.check_permutation_list('ba', 'ab'))
        self.assertTrue(cp.check_permutation_list('abc', 'abc'))
        self.assertTrue(cp.check_permutation_list('abc', 'acb'))
        self.assertTrue(cp.check_permutation_list('abc', 'cab'))
        self.assertTrue(cp.check_permutation_list('abc', 'cba'))
        self.assertTrue(cp.check_permutation_list('abc', 'bca'))
        self.assertTrue(cp.check_permutation_list('abc', 'bac'))
        self.assertTrue(cp.check_permutation_list('aac', 'aca'))
        self.assertTrue(cp.check_permutation_list('aaaa', 'aaaa'))

        # Negative tests.
        self.assertFalse(cp.check_permutation_list('', 'a'))
        self.assertFalse(cp.check_permutation_list('a', ''))
        self.assertFalse(cp.check_permutation_list('ab', 'a'))
        self.assertFalse(cp.check_permutation_list('a', 'ab'))
        self.assertFalse(cp.check_permutation_list('aa', 'ab'))
        self.assertFalse(cp.check_permutation_list('abc', 'aabc'))
        self.assertFalse(cp.check_permutation_list('aabc', 'abc'))
        self.assertFalse(cp.check_permutation_list('abc', 'aac'))
        self.assertFalse(cp.check_permutation_list('ccc', 'cac'))


if __name__ == '__main__':
    unittest.main()
