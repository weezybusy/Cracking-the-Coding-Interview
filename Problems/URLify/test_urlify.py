#!/usr/bin/env python3

import unittest
from urlify import urlify, urlify_better


class TestURLify(unittest.TestCase):

    def test_urlify(self):

        s = list('a')
        urlify(s, 1)
        self.assertEqual(s, list('a'))

        s = list('ab')
        urlify(s, 2)
        self.assertEqual(s, list('ab'))

        s = list('abc')
        urlify(s, 3)
        self.assertEqual(s, list('abc'))

        s = list('   ')
        urlify(s, 1)
        self.assertEqual(s, list('%20'))

        s = list('      ')
        urlify(s, 2)
        self.assertEqual(s, list('%20%20'))

        s = list('         ')
        urlify(s, 3)
        self.assertEqual(s, list('%20%20%20'))

        s = list('a   ')
        urlify(s, 2)
        self.assertEqual(s, list('a%20'))

        s = list('a b  ')
        urlify(s, 3)
        self.assertEqual(s, list('a%20b'))

        s = list('ab c  ')
        urlify(s, 4)
        self.assertEqual(s, list('ab%20c'))

        s = list('a b c    ')
        urlify(s, 5)
        self.assertEqual(s, list('a%20b%20c'))

        s = list(' a  ')
        urlify(s, 2)
        self.assertEqual(s, list('%20a'))

        s = list(' a     ')
        urlify(s, 3)
        self.assertEqual(s, list('%20a%20'))

        s = list(' a b    ')
        urlify(s, 4)
        self.assertEqual(s, list('%20a%20b'))

        s = list(' ab c    ')
        urlify(s, 5)
        self.assertEqual(s, list('%20ab%20c'))

        s = list(' a b c      ')
        urlify(s, 6)
        self.assertEqual(s, list('%20a%20b%20c'))

        s = list(' a b c              ')
        urlify(s, 6)
        self.assertEqual(s, list('%20a%20b%20c        '))


    def test_urlify_better(self):

        s = list('a')
        urlify_better(s, 1)
        self.assertEqual(s, list('a'))

        s = list('ab')
        urlify_better(s, 2)
        self.assertEqual(s, list('ab'))

        s = list('abc')
        urlify_better(s, 3)
        self.assertEqual(s, list('abc'))

        s = list('   ')
        urlify_better(s, 1)
        self.assertEqual(s, list('%20'))

        s = list('      ')
        urlify_better(s, 2)
        self.assertEqual(s, list('%20%20'))

        s = list('         ')
        urlify_better(s, 3)
        self.assertEqual(s, list('%20%20%20'))

        s = list('a   ')
        urlify_better(s, 2)
        self.assertEqual(s, list('a%20'))

        s = list('a b  ')
        urlify_better(s, 3)
        self.assertEqual(s, list('a%20b'))

        s = list('ab c  ')
        urlify_better(s, 4)
        self.assertEqual(s, list('ab%20c'))

        s = list('a b c    ')
        urlify_better(s, 5)
        self.assertEqual(s, list('a%20b%20c'))

        s = list(' a  ')
        urlify_better(s, 2)
        self.assertEqual(s, list('%20a'))

        s = list(' a     ')
        urlify_better(s, 3)
        self.assertEqual(s, list('%20a%20'))

        s = list(' a b    ')
        urlify_better(s, 4)
        self.assertEqual(s, list('%20a%20b'))

        s = list(' ab c    ')
        urlify_better(s, 5)
        self.assertEqual(s, list('%20ab%20c'))

        s = list(' a b c      ')
        urlify_better(s, 6)
        self.assertEqual(s, list('%20a%20b%20c'))

        s = list(' a b c              ')
        urlify_better(s, 6)
        self.assertEqual(s, list('%20a%20b%20c        '))


if __name__ == '__main__':
    unittest.main()
