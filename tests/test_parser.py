import unittest
from matrix.parser import parse_matrix, spiral_traversal
from matrix.exceptions import MatrixFormatError

class TestMatrixParser(unittest.TestCase):

    def test_parse_matrix(self):
        text = """
        | 10 | 20 |
        | 30 | 40 |
        """

        expected = [[10, 20], [30, 40]]

        self.assertEqual(parse_matrix(text), expected)

    def test_spiral_traversal(self):
        matrix = [
            [10, 20, 30, 40],
            [50, 60, 70, 80],
            [90, 100, 110, 120],
            [130, 140, 150, 160]
        ]

        expected = [
            10, 50, 90, 130,
            140, 150, 160, 120,
            80, 40, 30, 20,
            60, 100, 110, 70
        ]

        self.assertEqual(spiral_traversal(matrix), expected)

    def test_empty_matrix(self):
        with self.assertRaises(MatrixFormatError):
            parse_matrix("")

    def test_non_square_matrix(self):
        text = """
        | 10 | 20 |
        | 30 | 40 |
        | 50 | 60 |
        """

        with self.assertRaises(MatrixFormatError):
            parse_matrix(text)

    def test_one_element_matrix(self):
        self.assertEqual(
            spiral_traversal([[5]]),
            [5]
        )


    def test_invalid_value(self):
        text = """
        | 10 | abc |
        | 30 | 40  |
        """

        with self.assertRaises(MatrixFormatError):
            parse_matrix(text)

    def test_empty_cell(self):
        text = """
        | 10 | 20 |
        | 30 |    |
        """

        with self.assertRaises(MatrixFormatError):
            parse_matrix(text)

    def test_negative_value(self):
        text = """
        | 10 | -20 |
        | 30 | 40  |
        """

        with self.assertRaises(MatrixFormatError):
            parse_matrix(text)


if __name__ == "__main__":
    unittest.main()
