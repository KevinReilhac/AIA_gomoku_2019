##
## EPITECH PROJECT, 2019
## AIA_gomoku_2019
## File description:
## EmacsBrain
##

from AI.ABrain import ABrain
from Piskvork.GameClass import Game
from Piskvork.InfosClass import Infos
from Utils.Sort import natural_keys

class Position():

    def __init__(self, game, infos, x, y):
        self.game = game
        self.infos = infos
        self.x = x
        self.y = y
        self.qtuples = [True] * 20

class EmacsBrain(ABrain):

    def __init__(self, game : Game, infos : Infos):
        super(EmacsBrain, self).__init__(game, infos)
        self.best_value = 0
        self.best_x = 0
        self.best_y = 0
        self.positions = []
        self.init_pos()

    def init_pos(self):
        x = 0
        y = 0
        for line in self.game.board:
            for _ in line:
                self.positions.append(Position(self.game, self.infos, x, y))
                y += 1
            y = 0
            x += 1

    def play(self):
        self.best_value = 0
        self.best_x = 0
        self.best_y = 0
        self.explore_board()
        if self.best_value == 0:
            return (int(self.game.size_x / 2), int(self.game.size_y / 2))
        return (self.best_x, self.best_y)

    def is_empty_pos(self, x, y):
        if self.game.board[x][y] == 0:
            return (True)
        else:
            return (False)

    def heuristic_value(self, position):
        value = 0
        check_qtuple_list = self.get_check_methods()
        for check_qtuple in check_qtuple_list:
            value += check_qtuple(position)            
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

    def get_check_methods(self):
        allMethods = dir(self)
        allMethods.sort(key=natural_keys)
        allMethods = map(lambda x: getattr(self, x), allMethods)
        checkMethods = [x for x in allMethods if callable(x) and "check_qtuple" in x.__name__]
        return checkMethods

    def special_check(self, qtuple, value):
        if qtuple[0] == 0 and qtuple[1] == 1 and qtuple[2] == 1 and qtuple[3] == 1:
            print("DEBUG SPECIAL")
            return (value + 5000000)
        elif qtuple[0] == 0 and qtuple[1] == 2 and qtuple[2] == 2 and qtuple[3] == 2:
            print("DEBUG SPECIAL DEFENSE")
            return (value + 1000000)
        else:
            return (value)

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
            value = self.evaluate_qtuple(qtuple)
            if x + 1 < self.game.size_x and y - 1 >= 0 and self.game.board[x + 1][y - 1] == 0:
                value = self.special_check(qtuple, value)
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
            if x + 1 < self.game.size_x and self.game.board[x + 1][y] == 0:
                value = self.special_check(qtuple, value)
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
            if x + 1 < self.game.size_x and y + 1 < self.game.size_y and self.game.board[x + 1][y + 1] == 0:
                value = self.special_check(qtuple, value)
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
            if y + 1 < self.game.size_y and self.game.board[x][y + 1] == 0:
                value = self.special_check(qtuple, value)
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

        if 0 <= x + 4 < self.game.size_x and 0 <= y - 4 < self.game.size_y:
            qtuple.append(self.game.board[x + 4][y - 4])
            qtuple.append(self.game.board[x + 3][y - 3])
            qtuple.append(self.game.board[x + 2][y - 2])
            qtuple.append(self.game.board[x + 1][y - 1])
            value = self.evaluate_qtuple(qtuple)
            if y + 1 < self.game.size_y and x - 1 >= 0 and self.game.board[x - 1][y + 1] == 0:
                value = self.special_check(qtuple, value)
            if value == 1:
                position.qtuples[4] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)

    def check_qtuple_6(self, position):
        x = position.x
        y = position.y
        qtuple = []
        value = 0

        if 0 <= x + 4 < self.game.size_x:
            qtuple.append(self.game.board[x + 4][y])
            qtuple.append(self.game.board[x + 3][y])
            qtuple.append(self.game.board[x + 2][y])
            qtuple.append(self.game.board[x + 1][y])
            value = self.evaluate_qtuple(qtuple)
            if x - 1 >= 0 and self.game.board[x - 1][y] == 0:
                value = self.special_check(qtuple, value)
            if value == 1:
                position.qtuples[5] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)


    def check_qtuple_7(self, position):
        x = position.x
        y = position.y
        qtuple = []
        value = 0

        if 0 <= x + 4 < self.game.size_x and 0 <= y + 4 < self.game.size_y:
            qtuple.append(self.game.board[x + 4][y + 4])
            qtuple.append(self.game.board[x + 3][y + 3])
            qtuple.append(self.game.board[x + 2][y + 2])
            qtuple.append(self.game.board[x + 1][y + 1])
            value = self.evaluate_qtuple(qtuple)
            if x - 1 >= 0 and y - 1 >= 0 and self.game.board[x - 1][y - 1] == 0:
                value = self.special_check(qtuple, value)
            if value == 1:
                position.qtuples[6] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)

    def check_qtuple_8(self, position):
        x = position.x
        y = position.y
        qtuple = []
        value = 0

        if 0 <= y + 4 < self.game.size_y:
            qtuple.append(self.game.board[x][y + 4])
            qtuple.append(self.game.board[x][y + 3])
            qtuple.append(self.game.board[x][y + 2])
            qtuple.append(self.game.board[x][y + 1])
            value = self.evaluate_qtuple(qtuple)
            if y - 1 >= 0 and self.game.board[x][y - 1] == 0:
                value = self.special_check(qtuple, value)
            if value == 1:
                position.qtuples[7] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)


    def check_qtuple_9(self, position):
        x = position.x
        y = position.y
        qtuple = []
        value = 0

        if 0 <= x - 3 and x + 1 < self.game.size_x and y + 3 < self.game.size_y and 0 <= y - 1:
            qtuple.append(self.game.board[x - 3][y + 3])
            qtuple.append(self.game.board[x - 2][y + 2])
            qtuple.append(self.game.board[x - 1][y + 1])
            qtuple.append(self.game.board[x + 1][y - 1])
            value = self.evaluate_qtuple(qtuple)
            if value == 1:
                position.qtuples[8] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)


    def check_qtuple_10(self, position):
        x = position.x
        y = position.y
        qtuple = []
        value = 0

        if 0 <= x - 2 and x + 2 < self.game.size_x and y + 2 < self.game.size_y and 0 <= y - 2:
            qtuple.append(self.game.board[x - 2][y + 2])
            qtuple.append(self.game.board[x - 1][y + 1])
            qtuple.append(self.game.board[x + 1][y - 1])
            qtuple.append(self.game.board[x + 2][y - 2])
            value = self.evaluate_qtuple(qtuple)
            if value == 1:
                position.qtuples[9] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)
    

    def check_qtuple_11(self, position): 
        x = position.x
        y = position.y
        qtuple = []
        value = 0

        if 0 <= x - 1 and x + 3 < self.game.size_x and y + 1 < self.game.size_y and 0 <= y - 3:
            qtuple.append(self.game.board[x - 1][y + 1])
            qtuple.append(self.game.board[x - 1][y - 1])
            qtuple.append(self.game.board[x + 2][y - 2])
            qtuple.append(self.game.board[x + 3][y - 3])
            value = self.evaluate_qtuple(qtuple)
            if value == 1:
                position.qtuples[10] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)


    def check_qtuple_12(self, position):
        x = position.x
        y = position.y
        qtuple = []
        value = 0

        if 0 <= x - 3 and x + 1 < self.game.size_x:
            qtuple.append(self.game.board[x - 3][y])
            qtuple.append(self.game.board[x - 2][y])
            qtuple.append(self.game.board[x - 1][y])
            qtuple.append(self.game.board[x + 1][y])
            value = self.evaluate_qtuple(qtuple)
            if value == 1:
                position.qtuples[11] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)


    def check_qtuple_13(self, position):
        x = position.x
        y = position.y
        qtuple = []
        value = 0

        if 0 <= x - 2 and x + 2 < self.game.size_x:
            qtuple.append(self.game.board[x - 2][y])
            qtuple.append(self.game.board[x - 1][y])
            qtuple.append(self.game.board[x + 1][y])
            qtuple.append(self.game.board[x + 2][y])
            value = self.evaluate_qtuple(qtuple)
            if value == 1:
                position.qtuples[12] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)


    def check_qtuple_14(self, position):
        x = position.x
        y = position.y
        qtuple = []
        value = 0

        if 0 <= x - 1 and x + 3 < self.game.size_x:
            qtuple.append(self.game.board[x - 1][y])
            qtuple.append(self.game.board[x + 1][y])
            qtuple.append(self.game.board[x + 2][y])
            qtuple.append(self.game.board[x + 3][y])
            value = self.evaluate_qtuple(qtuple)
            if value == 1:
                position.qtuples[13] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)


    def check_qtuple_15(self, position):
        x = position.x
        y = position.y
        qtuple = []
        value = 0

        if 0 <= x - 3 and x + 1 < self.game.size_x and 0 <= y - 3 and y + 1 < self.game.size_y:
            qtuple.append(self.game.board[x - 3][y - 3])
            qtuple.append(self.game.board[x - 2][y - 2])
            qtuple.append(self.game.board[x - 1][y - 1])
            qtuple.append(self.game.board[x + 1][y + 1])
            value = self.evaluate_qtuple(qtuple)
            if value == 1:
                position.qtuples[14] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)


    def check_qtuple_16(self, position): 
        x = position.x
        y = position.y
        qtuple = []
        value = 0

        if 0 <= x - 2 and x + 2 < self.game.size_x and 0 <= y - 2 and y + 2 < self.game.size_y:
            qtuple.append(self.game.board[x - 2][y - 2])
            qtuple.append(self.game.board[x - 1][y - 1])
            qtuple.append(self.game.board[x + 1][y + 1])
            qtuple.append(self.game.board[x + 2][y + 2])
            value = self.evaluate_qtuple(qtuple)
            if value == 1:
                position.qtuples[15] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)


    def check_qtuple_17(self, position):
        x = position.x
        y = position.y
        qtuple = []
        value = 0

        if 0 <= x - 1 and x + 3 < self.game.size_x and 0 <= y - 1 and y + 3 < self.game.size_y:
            qtuple.append(self.game.board[x - 1][y - 1])
            qtuple.append(self.game.board[x + 1][y + 1])
            qtuple.append(self.game.board[x + 2][y + 2])
            qtuple.append(self.game.board[x + 3][y + 3])
            value = self.evaluate_qtuple(qtuple)
            if value == 1:
                position.qtuples[16] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)

    def check_qtuple_18(self, position):
        x = position.x
        y = position.y
        qtuple = []
        value = 0

        if 0 <= y - 3 and y + 1 < self.game.size_y:
            qtuple.append(self.game.board[x][y - 3])
            qtuple.append(self.game.board[x][y - 2])
            qtuple.append(self.game.board[x][y - 1])
            qtuple.append(self.game.board[x][y + 1])
            value = self.evaluate_qtuple(qtuple)
            if value == 1:
                position.qtuples[17] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)


    def check_qtuple_19(self, position):
        x = position.x
        y = position.y
        qtuple = []
        value = 0

        if 0 <= y - 2 and y + 2 < self.game.size_y:
            qtuple.append(self.game.board[x][y - 2])
            qtuple.append(self.game.board[x][y - 1])
            qtuple.append(self.game.board[x][y + 1])
            qtuple.append(self.game.board[x][y + 2])
            value = self.evaluate_qtuple(qtuple)
            if value == 1:
                position.qtuples[18] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)


    def check_qtuple_20(self, position):
        x = position.x
        y = position.y
        qtuple = []
        value = 0

        if 0 <= y - 1 and y + 3 < self.game.size_y:
            qtuple.append(self.game.board[x][y - 1])
            qtuple.append(self.game.board[x][y + 1])
            qtuple.append(self.game.board[x][y + 2])
            qtuple.append(self.game.board[x][y + 3])
            value = self.evaluate_qtuple(qtuple)
            if value == 1:
                position.qtuples[18] = False
                value = 0
            return (value)
        else :
            return (0)
        return (0)


def update_score(value : int, stone_nb : int, attack : bool):

        if attack == True and stone_nb == 1:
            return value + 35
        if attack == True and stone_nb == 2:
            return value + 800
        if attack == True and stone_nb == 3:
            return value + 15000
        if attack == True and stone_nb == 4:
            return value + 8000000000
        if attack == False and stone_nb == 1:
            return value + 15
        if attack ==   False and stone_nb == 2:
            return value + 400
        if attack == False and stone_nb == 3:
            return value + 1800
        if attack == False and stone_nb == 4:
            return value + 1000000000