import unittest

class SamePlanceException(Exception):
    pass
class SameRowException(Exception):
    pass
class SameColumnException(Exception):
    pass
class SameNumberException(Exception):
    pass



class Sudoku:
    
    #create sudoku game
    def __init__(self):
       
        self.board = [[0 for i in range(9)] for j in range(9)]

    #print sudoku game
    def __str__(self):
        board = ""
        for i in range(9):
            for j in range(9):
                board += str(self.board[i][j]) + " "
            board += " "
        return board

    
    def is_valid(self, row, col, value):
        if value in self.board[row]:
            return False
        for i in range(9):
            if self.board[i][col] == value:
                return False
        return True

   
    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    for k in range(1, 9 + 1):
                        if self.is_valid(i, j, k):
                            self.board[i][j] = k
                            self.solve()
                            self.board[i][j] = 0
                    return
        print(self)


    def add(self, row, col, value):
        self.check_exceptions(row, col, value)
        if self.board[row][col] != 0:
            raise SamePlanceException
        self.board[row][col] = value

   
    def remove(self, row, col):
        self.board[row][col] = 0

    
    def is_solved(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return False
        return True
    
    #check exceptions
    def check_exceptions(self, row, col, value):
        if self.board[row][col] != 0:
            raise SamePlanceException
        if value in self.board[row]:
            raise SameRowException
        for i in range(9):
            if self.board[i][col] == value:
                raise SameColumnException
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == value:
                    raise SameNumberException





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