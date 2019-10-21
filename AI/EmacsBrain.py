##
## EPITECH PROJECT, 2019
## AIA_gomoku_2019
## File description:
## EmacsBrain
##

from AI.ABrain import ABrain
from Piskvork.GameClass import Game
from Piskvork.InfosClass import Infos

class Position():

    def __init__(self, game, infos, x, y):
        self.game = game
        self.infos = infos
        self.x = x
        self.y = y
        self.qtuples = []

    def init_qtuples(self):
        i = 0
        while i < 20:
            self.qtuples.append(True)

class EmacsBrain(ABrain):

    def __init__(self, game : Game, infos : Infos):
        super(EmacsBrain, self).__init__(game, infos)
        self.best_value = 0
        self.best_x = 0
        self.best_y = 0
        self.positions = []

    def init_pos(self):
        x = 0
        y = 0
        for line in self.game.board:
            for column in line:
                self.positions.append(Position(self.game, self.infos, x, y))
                y += 1
            y = 0
            x += 1

    def play(self):
        self.explore_board()
        return (self.best_x, self.best_y)

    def is_empty_pos(self, x, y):
        if self.game.board[x][y] == "0":
            return (True)
        else:
            return (False)

    def heuristic_value(self, position):
        
        return (0)
    
    def explore_board(self):
        current_val = -1

        for position in self.positions:
            if self.is_empty_pos(position.x, position.y):
                current_val = self.heuristic_value(position)
                if current_val > self.best_value:
                    self.best_value = current_val
                    self.best_x = position.x
                    self.best_y = position.y
    
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