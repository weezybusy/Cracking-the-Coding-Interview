#!/usr/bin/env python3

import unittest
from one_away import one_away

class TestOneWay(unittest.TestCase):

    def test_one_way(self):

        # Positive tests.
        self.assertTrue(one_away('', ''))
        self.assertTrue(one_away('p', ''))
        self.assertTrue(one_away('', 'p'))
        self.assertTrue(one_away('p', 'pa'))
        self.assertTrue(one_away('pa', 'p'))
        self.assertTrue(one_away('pale', 'pale'))
        self.assertTrue(one_away('pale', 'ple'))
        self.assertTrue(one_away('ple', 'pale'))
        self.assertTrue(one_away('pales', 'pale'))
        self.assertTrue(one_away('pale', 'pales'))
        self.assertTrue(one_away('pale', 'bale'))
        self.assertTrue(one_away('bale', 'pale'))
        self.assertTrue(one_away('p', 'pp'))
        self.assertTrue(one_away('pp', 'p'))

        # Negative tests.
        self.assertFalse(one_away('pa', ''))
        self.assertFalse(one_away('', 'pa'))
        self.assertFalse(one_away('pale', 'bae'))
        self.assertFalse(one_away('bae', 'pale'))
        self.assertFalse(one_away('pppppp', 'pppp'))


if __name__ == "__main__":
    unittest.main()
