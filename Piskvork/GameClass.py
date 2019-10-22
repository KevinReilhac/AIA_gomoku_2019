##
## EPITECH PROJECT, 2019
## AIA_gomoku_2019
## File description:
## GameClass
##
from enum import Enum

class Game:
    board = None
    size_x = 0
    size_y = 0

    def __init__(self, size_x : int, size_y : int):
        matrix = []
        for _ in range(size_y):
            a = []
            for _ in range(size_x):
                a.append(0)
            matrix.append(a)
        self.board = matrix
        self.size_x = size_x
        self.size_y = size_y

    def debug_print(self):
        for i in range(self.size_y): 
            for j in range(self.size_x): 
                print(self.board[j][i], end = " ") 
            print() 

    def set_piece(self, x : int, y : int, player : int):
        if (self.board == None):
            return (False)
        if (x < 0 or x >= self.size_x):
            return (False)
        if (y < 0 or y >= self.size_y):
            return (False)
        self.board[x][y] = player
        return (True)
    
    def get_piece(self, x : int, y : int):
        if (x < 0 or x >= self.size_x):
            return (None)
        if (y < 0 or y >= self.size_y):
            return (None)
        return (self.board[x][y])