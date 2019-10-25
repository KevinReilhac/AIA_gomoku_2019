##
## EPITECH PROJECT, 2017
## Makfile
## File description:
## Thomaskas06
##


all:
		cp ./copy/pbrain-gomoku-ai.py pbrain-gomoku-ai

clean:
		@rm -f pbrain-gomoku-ai
		@rm -rf dist
		@rm -rf build
		@rm -f pbrain-gomoku-ai.spec

exe: all
		wine pyinstaller pbrain-gomoku-ai --onefile

fclean:		clean

re:		fclean all

.PHONY:	 clean, fclean, re
