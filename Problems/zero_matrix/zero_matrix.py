#!/usr/bin/env python3


"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0.
"""


# Time complexity:  O(mn).
# Space complexity: O(mn).
def zero_matrix(matrix):

    m = len(matrix)
    n = len(matrix[0])
    zero_rows = []
    zero_cols = []

    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                if row not in zero_rows:
                    zero_rows.append(row)
                if col not in zero_cols:
                    zero_cols.append(col)

    for row in range(m):
        for col in range(n):
            if row in zero_rows or col in zero_cols:
                matrix[row][col] = 0


# Time complexity:  O(mn).
# Space complexity: O(1).
def zero_matrix_alt(matrix):

    m = len(matrix)
    n = len(matrix[0])
    row_has_zero = False
    column_has_zero = False

    # Check if the first row has zeroes.
    for column in range(n):
        if matrix[0][column] == 0:
            row_has_zero = True
            break

    # Check if the first column has zeroes.
    for row in range(m):
        if matrix[row][0] == 0:
            column_has_zero = True
            break

    # Check the rest of the matrix.
    for row in range(1, m):
        for column in range(1, n):
            if matrix[row][column] == 0:
                matrix[row][0] = 0;
                matrix[0][column] = 0;

    # Nullify rows based on values in first column.
    for row in range(1, m):
        if matrix[row][0] == 0:
            nullify_row(matrix, row)

    # Nullify columns based on values in first row.
    for column in range(1, n):
        if matrix[0][column] == 0:
            nullify_column(matrix, column)

    # Nullify the first row.
    if row_has_zero:
        nullify_row(matrix, 0)

    # Nullify the first column.
    if column_has_zero:
        nullify_column(matrix, 0)


def nullify_row(matrix, row):
    for column in range(len(matrix[0])):
        matrix[row][column] = 0


def nullify_column(matrix, column):
    for row in range(len(matrix)):
        matrix[row][column] = 0
