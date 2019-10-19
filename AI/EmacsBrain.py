##
## EPITECH PROJECT, 2019
## AIA_gomoku_2019
## File description:
## EmacsBrain
##

from AI.ABrain import ABrain
from Piskvork.GameClass import Game
from Piskvork.InfosClass import Infos

class EmacsBrain(ABrain):
    best_value = 0
    best_x = 0
    best_y = 0


    def __init__(self, game : Game, infos : Infos):
        super(EmacsBrain, self).__init__(game, infos)


    def play(self):
        return (self.best_x, self.best_y)

    def explore_board(self):
        x = 0
        y = 0

        while x <= self.game.size_x:
            while y <= self.game.size_y:

                y += 1
            x += 1
    
"""    def has_neighbours(self, x, y):
        i = 0

        while i < 4 and 0 <= x < len(self.game.size_x):
            if (self.game.board[x][y] != "0")
                return True
            i += 1
            x -= 1
        i = 0
        while i < 4 and 0 <= x < len(self.game.size_x):
            if (self.game.board[x][y] != "0")
                return True
            i += 1
            x += 1
        i = 0
        while i < 4 and 0 <= y < len(self.game.size_y):
            if (self.game.board[x][y] != "0")
                return True
            i += 1
            y -= 1
        i = 0
        while i < 4 and 0 <= y < len(self.game.size_y):
            if (self.game.board[x][y] != "0")
                return True
            i += 1
            y += 1
        i = 0
"""
def update_score(value : int, stone_nb : int, attack : bool):

        if attack == True and stone_nb == 1:
            return value + 35
        if attack == True and stone_nb == 2:
            return value + 800
        if attack == True and stone_nb == 3:
            return value + 15000
        if attack == True and stone_nb == 4:
            return value + 800000
        if attack == False and stone_nb == 1:
            return value + 15
        if attack ==   False and stone_nb == 2:
            return value + 400
        if attack == False and stone_nb == 3:
            return value + 1800
        if attack == False and stone_nb == 4:
            return value + 100000