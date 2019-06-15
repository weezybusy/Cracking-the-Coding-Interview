#!/usr/bin/env python3

import unittest
from rotate_matrix import rotate_matrix, rotate_matrix_in_place


class TestRotateMatrix(unittest.TestCase):

    def test_rotate_matrix(self):
 
        # Positive tests.

        original_matrix = [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]
                ]
        expected_matrix = [
                [13, 9, 5, 1],
                [14, 10, 6, 2],
                [15, 11, 7, 3],
                [16, 12, 8, 4]
                ]
        self.assertEqual(expected_matrix, rotate_matrix(original_matrix))

        # Negative tests.

        original_matrix = []
        self.assertEqual(None, rotate_matrix(original_matrix))

        original_matrix = [[1], []]
        self.assertEqual(None, rotate_matrix(original_matrix))

        original_matrix = [[1, 2], [3]]
        self.assertEqual(None, rotate_matrix(original_matrix))

        original_matrix = [[1], [2, 3]]
        self.assertEqual(None, rotate_matrix(original_matrix))

        original_matrix = [[1]]
        self.assertEqual(None, rotate_matrix(original_matrix))

        original_matrix = [[3, 1], [4, 2]]
        self.assertEqual(None, rotate_matrix(original_matrix))

        original_matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.assertEqual(None, rotate_matrix(original_matrix))


    def test_rotate_matrix_in_place(self):

        # Positive tests.

        original_matrix = [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]
                ]
        expected_matrix = [
                [13, 9, 5, 1],
                [14, 10, 6, 2],
                [15, 11, 7, 3],
                [16, 12, 8, 4]
                ]
        rotate_matrix_in_place(original_matrix)
        self.assertEqual(expected_matrix, original_matrix)

        # Negative tests.

        original_matrix = []
        self.assertEqual(False, rotate_matrix_in_place(original_matrix))

        original_matrix = [[1], []]
        self.assertEqual(False, rotate_matrix_in_place(original_matrix))

        original_matrix = [[1, 2], [3]]
        self.assertEqual(False, rotate_matrix_in_place(original_matrix))

        original_matrix = [[1], [2, 3]]
        self.assertEqual(False, rotate_matrix_in_place(original_matrix))

        original_matrix = [[1]]
        self.assertEqual(False, rotate_matrix_in_place(original_matrix))

        original_matrix = [[3, 1], [4, 2]]
        self.assertEqual(False, rotate_matrix_in_place(original_matrix))

        original_matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.assertEqual(False, rotate_matrix_in_place(original_matrix))


if __name__ == '__main__':
    unittest.main()
