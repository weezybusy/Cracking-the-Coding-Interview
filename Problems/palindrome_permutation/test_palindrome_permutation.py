#!/usr/bin/env python3

import unittest
from palindrome_permutation import palindrome_permutation
from palindrome_permutation import palindrome_permutation_bit


class TestPalindromePermutation(unittest.TestCase):

    def test_palindrome_permutation(self):

        # Positive tests.
        self.assertTrue(palindrome_permutation(''))
        self.assertTrue(palindrome_permutation(' '))
        self.assertTrue(palindrome_permutation('a'))
        self.assertTrue(palindrome_permutation('aA'))
        self.assertTrue(palindrome_permutation('aAa'))
        self.assertTrue(palindrome_permutation(' a'))
        self.assertTrue(palindrome_permutation('A'))
        self.assertTrue(palindrome_permutation(' a '))
        self.assertTrue(palindrome_permutation('Aa '))
        self.assertTrue(palindrome_permutation(' Aa'))
        self.assertTrue(palindrome_permutation(' Aa '))
        self.assertTrue(palindrome_permutation('AAA'))
        self.assertTrue(palindrome_permutation('Don\'t nod.'))
        self.assertTrue(palindrome_permutation('tno\'d don.'))
        self.assertTrue(palindrome_permutation('\'tdon dno.'))
        self.assertTrue(palindrome_permutation('I did, did I?'))
        self.assertTrue(palindrome_permutation('I ddi, idd I?'))
        self.assertTrue(palindrome_permutation('I idd, ddi I?'))
        self.assertTrue(palindrome_permutation('My gym'))
        self.assertTrue(palindrome_permutation('yM gmy'))
        self.assertTrue(palindrome_permutation('yM ygm'))
        self.assertTrue(palindrome_permutation('Red rum, sir, is murder'))
        self.assertTrue(palindrome_permutation('deR rmu, sri, si drumre'))
        self.assertTrue(palindrome_permutation('dRe mur, isr, si dermur'))
        self.assertTrue(palindrome_permutation('Top spot'))
        self.assertTrue(palindrome_permutation('Tpo psto'))
        self.assertTrue(palindrome_permutation('pTo tops'))
        self.assertTrue(palindrome_permutation('Was it a cat I saw?'))
        self.assertTrue(palindrome_permutation('saW ti a act I was?'))
        self.assertTrue(palindrome_permutation('aWs ti a tca I wsa?'))
        self.assertTrue(palindrome_permutation('Eva, can I see bees in a cave?'))
        self.assertTrue(palindrome_permutation('vEa, nca I ese sebe ni a acve?'))
        self.assertTrue(palindrome_permutation('avE, anc I ees sbee ni a vace?'))
        self.assertTrue(palindrome_permutation('No lemon, no melon'))
        self.assertTrue(palindrome_permutation('oN nomel, on mleno'))
        self.assertTrue(palindrome_permutation('oN monle, on onlem'))

        # Negative tests.
        self.assertFalse(palindrome_permutation('apple'))
        self.assertFalse(palindrome_permutation('banana'))
        self.assertFalse(palindrome_permutation('Don\'t node.'))
        self.assertFalse(palindrome_permutation('I didn\'t, did I?'))
        self.assertFalse(palindrome_permutation('Myn gym'))
        self.assertFalse(palindrome_permutation('Red room, sir, is murder'))
        self.assertFalse(palindrome_permutation('Top spop'))
        self.assertFalse(palindrome_permutation('Was it a cut I saw?'))
        self.assertFalse(palindrome_permutation('Eva, can\'t I see bees in a cave?'))
        self.assertFalse(palindrome_permutation('No lemon, rnok melon'))


    def test_palindrome_permutation_bit(self):

        # Positive tests.
        self.assertTrue(palindrome_permutation_bit(''))
        self.assertTrue(palindrome_permutation_bit(' '))
        self.assertTrue(palindrome_permutation_bit('a'))
        self.assertTrue(palindrome_permutation_bit('aA'))
        self.assertTrue(palindrome_permutation_bit('aAa'))
        self.assertTrue(palindrome_permutation_bit(' a'))
        self.assertTrue(palindrome_permutation_bit('A'))
        self.assertTrue(palindrome_permutation_bit(' a '))
        self.assertTrue(palindrome_permutation_bit('Aa '))
        self.assertTrue(palindrome_permutation_bit(' Aa'))
        self.assertTrue(palindrome_permutation_bit(' Aa '))
        self.assertTrue(palindrome_permutation_bit('AAA'))
        self.assertTrue(palindrome_permutation_bit('Don\'t nod.'))
        self.assertTrue(palindrome_permutation_bit('tno\'d don.'))
        self.assertTrue(palindrome_permutation_bit('\'tdon dno.'))
        self.assertTrue(palindrome_permutation_bit('I did, did I?'))
        self.assertTrue(palindrome_permutation_bit('I ddi, idd I?'))
        self.assertTrue(palindrome_permutation_bit('I idd, ddi I?'))
        self.assertTrue(palindrome_permutation_bit('My gym'))
        self.assertTrue(palindrome_permutation_bit('yM gmy'))
        self.assertTrue(palindrome_permutation_bit('yM ygm'))
        self.assertTrue(palindrome_permutation_bit('Red rum, sir, is murder'))
        self.assertTrue(palindrome_permutation_bit('deR rmu, sri, si drumre'))
        self.assertTrue(palindrome_permutation_bit('dRe mur, isr, si dermur'))
        self.assertTrue(palindrome_permutation_bit('Top spot'))
        self.assertTrue(palindrome_permutation_bit('Tpo psto'))
        self.assertTrue(palindrome_permutation_bit('pTo tops'))
        self.assertTrue(palindrome_permutation_bit('Was it a cat I saw?'))
        self.assertTrue(palindrome_permutation_bit('saW ti a act I was?'))
        self.assertTrue(palindrome_permutation_bit('aWs ti a tca I wsa?'))
        self.assertTrue(palindrome_permutation_bit('Eva, can I see bees in a cave?'))
        self.assertTrue(palindrome_permutation_bit('vEa, nca I ese sebe ni a acve?'))
        self.assertTrue(palindrome_permutation_bit('avE, anc I ees sbee ni a vace?'))
        self.assertTrue(palindrome_permutation_bit('No lemon, no melon'))
        self.assertTrue(palindrome_permutation_bit('oN nomel, on mleno'))
        self.assertTrue(palindrome_permutation_bit('oN monle, on onlem'))

        # Negative tests.
        self.assertFalse(palindrome_permutation_bit('apple'))
        self.assertFalse(palindrome_permutation_bit('banana'))
        self.assertFalse(palindrome_permutation_bit('Don\'t node.'))
        self.assertFalse(palindrome_permutation_bit('I didn\'t, did I?'))
        self.assertFalse(palindrome_permutation_bit('Myn gym'))
        self.assertFalse(palindrome_permutation_bit('Red room, sir, is murder'))
        self.assertFalse(palindrome_permutation_bit('Top spop'))
        self.assertFalse(palindrome_permutation_bit('Was it a cut I saw?'))
        self.assertFalse(palindrome_permutation_bit('Eva, can\'t I see bees in a cave?'))
        self.assertFalse(palindrome_permutation_bit('No lemon, rnok melon'))


if __name__ == '__main__':
    unittest.main()
