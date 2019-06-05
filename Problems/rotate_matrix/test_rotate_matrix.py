#!/usr/bin/env python3

import unittest
import rotate_matrix as rm


class TestRotateMatrix(unittest.TestCase):

    def test_rotate_matrix(self):

        # Positive tests.
        original_matrix = [[1]]
        rotated_matrix = [[1]]
        self.assertEqual(rotated_matrix, rm.rotate_matrix(original_matrix))

        original_matrix = [[3, 1], [4, 2]]
        rotated_matrix = [[1, 2], [3, 4]]
        self.assertEqual(rotated_matrix, rm.rotate_matrix(original_matrix))

        original_matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        rotated_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(rotated_matrix, rm.rotate_matrix(original_matrix))

        original_matrix = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
        rotated_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        self.assertEqual(rotated_matrix, rm.rotate_matrix(original_matrix))

        # Negative tests.

        original_matrix = []
        self.assertEqual(None, rm.rotate_matrix(original_matrix))

        original_matrix = [[1], []]
        self.assertEqual(None, rm.rotate_matrix(original_matrix))

        original_matrix = [[1, 2], [3]]
        self.assertEqual(None, rm.rotate_matrix(original_matrix))

        original_matrix = [[1], [2, 3]]
        self.assertEqual(None, rm.rotate_matrix(original_matrix))


    def test_rotate_matrix_in_place(self):
        pass

if __name__ == '__main__':
    unittest.main()
