##
## EPITECH PROJECT, 2019
## AIA_gomoku_2019
## File description:
## ABrain
##

from abc import ABC, abstractmethod
from Piskvork.GameClass import Game
from Piskvork.InfosClass import Infos

class ABrain(ABC):
    game = None
    infos = None

    def __init__(self, game : Game, infos : Infos):
        self.game = game
        self.infos = infos

    #Play may return a tuple (x, y)
    @abstractmethod
    def play(self):
        pass
