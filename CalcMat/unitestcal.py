import unittest
from CalcMat import Matrix  # Import the Matrix class from matrix_operations.py

class TestMatrixOperations(unittest.TestCase):

    def test_addition(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        expected_result = Matrix([[6, 8], [10, 12]])
        result = matrix1 + matrix2
        self.assertEqual(result.values, expected_result.values)

    def test_subtraction(self):
        matrix1 = Matrix([[10, 20], [30, 40]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        expected_result = Matrix([[5, 14], [23, 32]])
        result = matrix1 - matrix2
        self.assertEqual(result.values, expected_result.values)

    def test_multiplication(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        expected_result = Matrix([[19, 22], [43, 50]])
        result = matrix1 * matrix2
        self.assertEqual(result.values, expected_result.values)

    def test_invalid_addition(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[1, 2]])  # This is a 1x2 matrix, not 2x2
        with self.assertRaises(TypeError):  # Expecting an error if trying to add matrices of different sizes
            _ = matrix1 + matrix2

if __name__ == "__main__":
    unittest.main()
