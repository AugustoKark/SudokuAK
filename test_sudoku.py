import unittest

from exceptions import *
from sudoku import Sudoku


class TestSudoku(unittest.TestCase):
    def test_create_board(self):
        sudoku = Sudoku()
        self.assertEqual(len(sudoku.board), 9)
        self.assertEqual(len(sudoku.board[0]), 9)

    def test_set_number_basic(self):
        sudoku = Sudoku()
        sudoku.add(1, 1, 9)
        self.assertEqual(sudoku.board[1][1], 9)

    def test_set_number_validate_column(self):
        sudoku = Sudoku()
        sudoku.add(1, 1, 9)
        
        with self.assertRaises(SamePlanceException):
            sudoku.add(1, 1, 9)
        self.assertEqual(sudoku.board[1][1], 9)
        self.assertEqual(sudoku.board[1][2], 0)

    def test_set_number_validate_matrix3(self):
        sudoku = Sudoku()
        sudoku.add(6, 6, 9)
        with self.assertRaises(SameNumberException):
            sudoku.add(8, 8, 9)
        self.assertEqual(sudoku.board[6][6], 9)
        self.assertEqual(sudoku.board[8][8], 0)
    
    def test_set_number_validate_matrix2(self):
        sudoku = Sudoku()
        sudoku.add(6, 6, 9)
        with self.assertRaises(SameColumnException):
            sudoku.add(8, 6, 9)
        self.assertEqual(sudoku.board[6][6], 9)
        self.assertEqual(sudoku.board[8][6], 0)
    
    def test_set_number_validate_matrix1(self):
        sudoku = Sudoku()
        sudoku.add(6, 6, 9)
        with self.assertRaises(SameRowException):
            sudoku.add(6, 8, 9)
        self.assertEqual(sudoku.board[6][6], 9)
        self.assertEqual(sudoku.board[6][8], 0)






if __name__ == '__main__':
    unittest.main()