from exceptions import *

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





