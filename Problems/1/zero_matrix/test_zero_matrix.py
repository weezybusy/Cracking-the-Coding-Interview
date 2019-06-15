#!/usr/bin/env python3


import unittest
from zero_matrix import zero_matrix, zero_matrix_alt


class TestZeroMatrix(unittest.TestCase):

    def test_zero_matrix(self):

        matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
        expected_output = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
        zero_matrix(matrix)
        self.assertEqual(matrix, expected_output)

        matrix = [[1, 0, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
        zero_matrix(matrix)
        expected_output = [[0, 0, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1]]
        self.assertEqual(matrix, expected_output)

        matrix = [[1, 1, 1], [1, 1, 0], [1, 1, 1], [1, 1, 1]]
        zero_matrix(matrix)
        expected_output = [[1, 1, 0], [0, 0, 0], [1, 1, 0], [1, 1, 0]]
        self.assertEqual(matrix, expected_output)

        matrix = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]]
        zero_matrix(matrix)
        expected_output = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
        self.assertEqual(matrix, expected_output)

        matrix = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
        zero_matrix(matrix)
        expected_output = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(matrix, expected_output)

    def test_zero_matrix_alt(self):

        matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
        expected_output = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
        zero_matrix_alt(matrix)
        self.assertEqual(matrix, expected_output)

        matrix = [[1, 0, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
        zero_matrix_alt(matrix)
        expected_output = [[0, 0, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1]]
        self.assertEqual(matrix, expected_output)

        matrix = [[1, 1, 1], [1, 1, 0], [1, 1, 1], [1, 1, 1]]
        zero_matrix_alt(matrix)
        expected_output = [[1, 1, 0], [0, 0, 0], [1, 1, 0], [1, 1, 0]]
        self.assertEqual(matrix, expected_output)

        matrix = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]]
        zero_matrix_alt(matrix)
        expected_output = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
        self.assertEqual(matrix, expected_output)

        matrix = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
        zero_matrix_alt(matrix)
        expected_output = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(matrix, expected_output)


if __name__ == '__main__':
    unittest.main()
