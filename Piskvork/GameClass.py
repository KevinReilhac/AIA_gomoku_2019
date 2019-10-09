##
## EPITECH PROJECT, 2019
## AIA_gomoku_2019
## File description:
## GameClass
##
from enum import Enum

class CaseState(Enum):
    NONE = 0
    ME = 1
    OTHER = 2

class Game:
    board = None
    size = 0

    def __init__(self, size : int):
        self.board = [[CaseState.NONE] * size] * size
        self.size = size

    def debug_print(self):
        for row in self.board:
            print(' '.join([str(elem) for elem in row]))

    def set_piece(self, x : int, y : int, player : CaseState):
        if (x < 0 or x >= self.size):
            return (False)
        if (y < 0 or y >= self.size):
            return (False)
        self.board[x][y] = player
    
    def get_piece(self, x : int, y : int):
        if (x < 0 or x >= self.size):
            return (None)
        if (y < 0 or y >= self.size):
            return (None)
        return (self.board[x][y])