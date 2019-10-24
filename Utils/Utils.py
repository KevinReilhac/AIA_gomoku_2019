##
## EPITECH PROJECT, 2019
## AIA_gomoku_2019
## File description:
## Utils
##

import sys

def flush_print(text):
    print(text)
    sys.stdout.flush()

def print_pos(x, y):
    flush_print("%d,%d" % (x, y))