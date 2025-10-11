# 代码生成时间: 2025-10-11 22:33:49
import numpy as np

"""
A matrix operations library using Python and PyQT framework."""

class MatrixOperations:
    """
    A class to perform various matrix operations.
    """

    def __init__(self):
        pass

    def add_matrices(self, matrix_a, matrix_b):
        """
        Add two matrices together.

        Args:
            matrix_a (np.ndarray): First matrix.
            matrix_b (np.ndarray): Second matrix.

        Returns:
            np.ndarray: Sum of the two matrices.

        Raises:
            ValueError: If matrices are not of the same shape.
        """
        if matrix_a.shape != matrix_b.shape:
            raise ValueError("Matrices must be of the same shape.")
        return np.add(matrix_a, matrix_b)

    def subtract_matrices(self, matrix_a, matrix_b):
        """
        Subtract one matrix from another.

        Args:
            matrix_a (np.ndarray): First matrix.
            matrix_b (np.ndarray): Second matrix.

        Returns:
            np.ndarray: Difference of the two matrices.

        Raises:
            ValueError: If matrices are not of the same shape.
        """
        if matrix_a.shape != matrix_b.shape:
            raise ValueError("Matrices must be of the same shape.")
        return np.subtract(matrix_a, matrix_b)

    def multiply_matrices(self, matrix_a, matrix_b):
        """
        Multiply two matrices together.

        Args:
            matrix_a (np.ndarray): First matrix.
            matrix_b (np.ndarray): Second matrix.

        Returns:
            np.ndarray: Product of the two matrices.

        Raises:
            ValueError: If the number of columns in the first matrix does not match the number of rows in the second matrix.
        """
        if matrix_a.shape[1] != matrix_b.shape[0]:
            raise ValueError("The number of columns in the first matrix must match the number of rows in the second matrix.")
        return np.matmul(matrix_a, matrix_b)

    def transpose_matrix(self, matrix):
        """
        Transpose a matrix.

        Args:
            matrix (np.ndarray): The matrix to transpose.

        Returns:
            np.ndarray: Transposed matrix.
        """
        return np.transpose(matrix)

    def determinant_matrix(self, matrix):
        """
        Calculate the determinant of a square matrix.

        Args:
            matrix (np.ndarray): The square matrix.

        Returns:
            float: The determinant of the matrix.

        Raises:
            ValueError: If the matrix is not square.
        """
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Matrix must be square.")
        return np.linalg.det(matrix)

    def inverse_matrix(self, matrix):
        """
        Calculate the inverse of a square matrix.

        Args:
            matrix (np.ndarray): The square matrix.

        Returns:
            np.ndarray: The inverse of the matrix.

        Raises:
            ValueError: If the matrix is not square or not invertible.
        """
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Matrix must be square.")
        try:
            return np.linalg.inv(matrix)
        except np.linalg.LinAlgError:
            raise ValueError("Matrix is not invertible.")
