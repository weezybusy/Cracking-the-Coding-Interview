#!/usr/bin/env python3

import unittest
import check_permutation


class TestCheckPermutation(unittest.TestCase):

    def test_check_permutation_sort(self):
        self.assertTrue(check_permutation.check_permutation_sort('', ''))
        self.assertFalse(check_permutation.check_permutation_sort('hell', 'olleh'))
        self.assertFalse(check_permutation.check_permutation_sort('hello', 'olle'))
        self.assertTrue(check_permutation.check_permutation_sort('hello', 'olleh'))
        self.assertFalse(check_permutation.check_permutation_sort('hello', 'olllh'))
        self.assertFalse(check_permutation.check_permutation_sort('hlllo', 'olleh'))

    def test_check_permutation_hash(self):
        self.assertTrue(check_permutation.check_permutation_hash('', ''))
        self.assertFalse(check_permutation.check_permutation_hash('hell', 'olleh'))
        self.assertFalse(check_permutation.check_permutation_hash('hello', 'olle'))
        self.assertTrue(check_permutation.check_permutation_hash('hello', 'olleh'))
        self.assertFalse(check_permutation.check_permutation_hash('hello', 'olllh'))
        self.assertFalse(check_permutation.check_permutation_hash('hlllo', 'olleh'))
        self.assertTrue(check_permutation.check_permutation_hash('hello', 'hello'))


if __name__ == '__main__':
    unittest.main()
