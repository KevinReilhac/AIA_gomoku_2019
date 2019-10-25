#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## Gomoku
## File description:
## brainClass
##

import string
import array
import sys
from Piskvork.InfosClass import Infos
from Piskvork.GameClass import Game
from AI.EmacsBrain import EmacsBrain
from Utils.Utils import flush_print, print_pos


class Piskvork:
    infos = Infos()
    quit_loop = False
    game = None
    brain = None

    def read_entry_loop(self):
        try:
            for line in sys.stdin:
                self.treat_input(line)
                if (self.quit_loop):
                    break
        except EOFError:
            pass
        except KeyboardInterrupt:
            pass

    def treat_input(self, line : str):
        line = line.lower()
        line = line.replace(',', ' ')
        line = line.strip()
        arguments = line.split()
        if (len(arguments) == 0):
            return
        command = self._get_function_from_name(arguments[0])
        if (command == AttributeError):
            self.unknow(arguments[0].upper())
        else:
            command(arguments)

    def _get_function_from_name(self, function_name : str):
        commands = [
            self.start, self.turn, self.begin, self.board, self.info, 
            self.end, self.about, self.rectstart,
            self.restart, self.takeback, self.play, self.displayboard
        ]

        try:
            method = getattr(self, function_name)
            if (method in commands):
                return (method)
        except AttributeError:
            return (AttributeError)

    #-------------------------------[Commands]---------------------------------#

    def start(self, arguments : list):
        size = 0
        error_message = "unsupported size or other error"

        if (len(arguments) != 2):
            self.error(error_message)
            return
        try:
            size = int(arguments[1])
        except ValueError:
            self.error(error_message)
            return
        if (size < 5 or size > 20):
            self.error(error_message)
            return
        self.game = Game(size, size)
        self.brain = EmacsBrain(self.game, self.infos)
        self.brain.init_pos()
        flush_print("OK")

    def turn(self, arguments : list):
        x = 0
        y = 0

        if (self.game == None):
            self.error("Need to START before")
            return
        if (len(arguments) != 3):
            self.error("TURN need X and Y.")
            return
        try:
            x = int(arguments[1])
            y = int(arguments[2])
        except ValueError:
            self.error("TURN need X and Y as 2 integers.")
            return
        if not (self.game.set_piece(x, y, 2)):
            self.error("Opponent say bullshit.")
            return
        answer = self.brain.play()
        print_pos(answer[0], answer[1])
        self.game.set_piece(answer[0], answer[1], 1)

    def begin(self, arguments : list):
        if self.game == None:
            self.error("Need to START before")
            return
        answer = self.brain.play()
        print_pos(answer[0], answer[1])
        self.game.set_piece(answer[0], answer[1], 1)

    def board(self, arguments : list):
        if (self.game == None):
            self.error("Need to START before")
            return
        try:
            for line in sys.stdin:
                 if not (self.board_treat_line(line)):
                    return
        except EOFError:
            pass
        except KeyboardInterrupt:
            pass

    def board_treat_line(self, line : str):
        line = line.strip()
        if (line.upper() == "DONE"):
            answer = self.brain.play()
            print("%d,%d" % (answer[0], answer[1]))
            self.game.set_piece(answer[0], answer[1], 1)
            return (False)
        arguments = line.split(",")
        arguments = list(map(lambda arg: arg.strip(), arguments))

        try:
            x = int(arguments[0])
            y = int(arguments[1])
            player = int(arguments[2])

            if not (self.game.set_piece(x, y, player)):
                self.error("Invalid values.")
            return (True)
        except ValueError:
            self.error("Invalid arguments.")
            return (True)

    def info(self, arguments : list):
        if (len(arguments) < 2):
            self.error("INFO need a key.")
            return
        if (arguments[1] == "evaluate"):
            if (len(arguments) != 4):
                self.error("evaluate need 2 arguments.")
                return
            else:
                try:
                    self.infos.change_value(arguments[1], (int(arguments[2]), int(arguments[3])))
                except ValueError:
                    self.error("evaluate parameters need to be 2 integers")
        else:
            if (len(arguments) != 3):
                self.error(arguments[1] + " invalid arguments.")
                return
            else:
                return_value = self.infos.change_value(arguments[1], arguments[2])
                if not return_value:
                    self.error("Invalid Key.")
                if (return_value == ValueError):
                    self.error(arguments[1] + " wrong parameter type")
                

    def end(self, arguments : list):
        self.quit_loop = True

    def about(self, arguments : list):
        flush_print("name=\"%s\", version=\"%s\", author=\"%s\", country=\"%s\"" % ("Gomme au fesses", "0.2.0", "Toto & Kebab", "FR"))

    def rectstart(self, arguments : list):
        size_x = 0
        size_y = 0
        error_message = "rectangular board is not supported or other error"

        if (len(arguments) != 3):
            self.error(error_message)
            return
        try:
            size_x = int(arguments[1])
            size_y = int(arguments[2])
        except ValueError:
            self.error(error_message)
            return
        if (size_x < 5 or size_x > 20):
            self.error(error_message)
            return
        if (size_y < 5 or size_y > 20):
            self.error(error_message)
            return
        self.game = Game(size_x, size_y)
        self.brain = EmacsBrain(self.game, self.infos)
        flush_print("OK")
        pass

    def restart(self, arguments : list):
        self.game = Game(self.game.size_x, self.game.size_y)
        flush_print("OK")

    def takeback(self, arguments : list):
        x = 0
        y = 0

        try:
            x = int(arguments[1])
            y = int(arguments[2])
        except ValueError:
            self.error("Invalid positions.")
        if not (self.game.set_piece(x, y, 0)):
            self.error("Wrong positions.")

    def play(self, arguments : list):
        pass
    #------------------------------[Debug]---------------------------------#
    def displayboard(self, arguments : list):
        self.game.debug_print()
    #------------------------------[Responces]---------------------------------#

    def unknow(self, message : str):
        print("UNKNOWN %s" % (message))

    def error(self, message : str):
        print("ERROR - %s" % (message))

    def debug(self, message : str):
        pass

    def suggest(self, x : int, y : int):
        pass