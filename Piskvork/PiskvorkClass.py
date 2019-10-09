#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## Gomoku
## File description:
## brainClass
##

import fileinput
import string
import array
from Piskvork.InfosClass import Infos


class Piskvork:
    infos = Infos()
    quit_loop = False

    def read_entry_loop(self):
        try:
            for line in fileinput.input():
                if (self.quit_loop):
                    break
                self.treat_input(line)
        except EOFError:
            pass
        except KeyboardInterrupt:
            pass

    def treat_input(self, line : str):
        line = line.lower()
        line = line.strip()
        arguments = line.split()
        command = self._get_function_from_name(arguments[0])
        if (command == AttributeError):
            self.unknow(arguments[0].upper())
        else:
            command(arguments)

    def _get_function_from_name(self, function_name : str):
        commands = [
            self.start, self.turn, self.begin, self.board, self.info, 
            self.end, self.about, self.rectstart,
            self.restart, self.takeback, self.play
        ]

        try:
            method = getattr(self, function_name)
            if (method in commands):
                return (method)
        except AttributeError:
            return (AttributeError)
        method()

    #-------------------------------[Commands]---------------------------------#

    def start(self, arguments : list):
        print("debug start")
        pass

    def turn(self, arguments : list):
        print("debug turn")
        pass

    def begin(self, arguments : list):
        print("debug begin")
        pass

    def board(self, arguments : list):
        print("debug board")
        pass

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
        pass

    def about(self, arguments : list):
        print("debug about")
        pass

    def rectstart(self, arguments : list):
        print("debug rectstart")
        pass

    def restart(self, arguments : list):
        print("debug restart")
        pass

    def takeback(self, arguments : list):
        print("debug takeback")
        pass

    def play(self, arguments : list):
        print("debug play")
        pass

    #------------------------------[Responces]---------------------------------#

    def unknow(self, message : str):
        print("UNKNOWN %s" % (message))

    def error(self, message : str):
        print("ERROR %s" % (message))
        pass
    
    def debug(self, message : str):
        pass

    def suggest(self, x : int, y : int):
        pass