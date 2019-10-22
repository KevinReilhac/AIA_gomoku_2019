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
        self.qtuples = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,True, True, True, True, True]


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
        if self.game.board[x][y] == 0:
            return (True)
        else:
            return (False)

    def heuristic_value(self, position):
        value = 0

        value += self.check_qtuple_1(position)
        value += self.check_qtuple_2(position)
        value += self.check_qtuple_3(position)
        value += self.check_qtuple_4(position)
        value += self.check_qtuple_5(position)
        value += self.check_qtuple_6(position)
        value += self.check_qtuple_7(position)
        value += self.check_qtuple_8(position)
        value += self.check_qtuple_9(position)
        value += self.check_qtuple_10(position)
        value += self.check_qtuple_11(position)
        value += self.check_qtuple_12(position)
        value += self.check_qtuple_13(position)
        value += self.check_qtuple_14(position)
        value += self.check_qtuple_15(position)
        value += self.check_qtuple_16(position)
        value += self.check_qtuple_17(position)
        value += self.check_qtuple_18(position)
        value += self.check_qtuple_19(position)
        value += self.check_qtuple_20(position)
        print(value)
        return (value)
    
    def explore_board(self):
        current_val = 0

        for position in self.positions:
            if self.is_empty_pos(position.x, position.y):
                current_val = self.heuristic_value(position)
                if current_val > self.best_value:
                    self.best_value = current_val
                    self.best_x = position.x
                    self.best_y = position.y
    

    def evaluate_qtuple(self, qtuple):
        own_stone_counter = 0
        enemy_stone_counter = 0
        for elem in qtuple:
            if elem == 1:
                own_stone_counter += 1
            elif elem == 2:
                enemy_stone_counter += 1
        if own_stone_counter > 0 and enemy_stone_counter > 0:
            return (1)
        elif own_stone_counter > enemy_stone_counter:
            return (update_score(0, own_stone_counter, True))
        elif enemy_stone_counter > own_stone_counter:
            return (update_score(0, enemy_stone_counter, False))
        return (0)


    def check_qtuple_1(self, position : Position):
        x = position.x
        y = position.y
        qtuple = []
        value = 0

        if 0 <= x - 4 < self.game.size_x and 0 <= y + 4 < self.game.size_y:
            qtuple.append(self.game.board[x - 4][y + 4])
            qtuple.append(self.game.board[x - 3][y + 3])
            qtuple.append(self.game.board[x - 2][y + 2])
            qtuple.append(self.game.board[x - 1][y + 1])
            if value == 1:
                position.qtuples[0] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)

    def check_qtuple_2(self, position):
        x = position.x
        y = position.y
        qtuple = []
        value = 0

        if 0 <= x - 4 < self.game.size_x:
            qtuple.append(self.game.board[x - 4][y])
            qtuple.append(self.game.board[x - 3][y])
            qtuple.append(self.game.board[x - 2][y])
            qtuple.append(self.game.board[x - 1][y])
            value = self.evaluate_qtuple(qtuple)
            if value == 1:
                position.qtuples[1] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)


    def check_qtuple_3(self, position):
        x = position.x
        y = position.y
        qtuple = []
        value = 0

        if 0 <= x - 4 < self.game.size_x and 0 <= y - 4 < self.game.size_y:
            qtuple.append(self.game.board[x - 4][y - 4])
            qtuple.append(self.game.board[x - 3][y - 3])
            qtuple.append(self.game.board[x - 2][y - 2])
            qtuple.append(self.game.board[x - 1][y - 1])
            value = self.evaluate_qtuple(qtuple)
            if value == 1:
                position.qtuples[2] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)

    def check_qtuple_4(self, position):
        x = position.x
        y = position.y
        qtuple = []
        value = 0

        if 0 <= y - 4 < self.game.size_y:
            qtuple.append(self.game.board[x][y - 4])
            qtuple.append(self.game.board[x][y - 3])
            qtuple.append(self.game.board[x][y - 2])
            qtuple.append(self.game.board[x][y - 1])
            value = self.evaluate_qtuple(qtuple)
            if value == 1:
                position.qtuples[3] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)


    def check_qtuple_5(self, position):
        x = position.x
        y = position.y
        qtuple = []
        value = 0

        if 0 <= x - 4 < self.game.size_x:
            qtuple.append(self.game.board[x][y])
            qtuple.append(self.game.board[x][y])
            qtuple.append(self.game.board[x][y])
            qtuple.append(self.game.board[x][y])
            value = self.evaluate_qtuple(qtuple)
            if value == 1:
                position.qtuples[4] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)

    def check_qtuple_6(self, position):
    return 0


    def check_qtuple_7(self, position):
        return 0
    def check_qtuple_8(self, position):
        return 0
    def check_qtuple_9(self, position):
        return 0
    def check_qtuple_10(self, position):
        return 0
    def check_qtuple_11(self, position): 
        return 0
    def check_qtuple_12(self, position):
        return 0
    def check_qtuple_13(self, position):
        return 0
    def check_qtuple_14(self, position):
        return 0
    def check_qtuple_15(self, position):
        return 0
    def check_qtuple_16(self, position): 
        return 0   
    def check_qtuple_17(self, position):
        return 0
    def check_qtuple_18(self, position):
        return 0
    def check_qtuple_19(self, position):
        return 0
    def check_qtuple_20(self, position):
         return 0   
    
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