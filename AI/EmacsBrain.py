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

    def __init__(self, game : Game, infos : Infos):
        super(EmacsBrain, self).__init__(game, infos)
    
    def play(self):
        return (0, 0)
