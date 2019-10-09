##
## EPITECH PROJECT, 2019
## AIA_gomoku_2019
## File description:
## InfosClass
##

class Infos:
    timeout_turn = 0
    timeout_match = 0
    max_memory = 0
    time_left = 0
    game_type = 0
    rule = 0 
    evaluate = (0, 0)
    folder = ""

    def change_value(self, name : str, value):
        try :
            if (name == "timeout_turn"):
                self.timeout_turn = int(value)
            elif (name == "timeout_match"):
                self.timeout_match = int(value)
            elif (name == "max_memory"):
                self.max_memory = int(value)
            elif (name == "time_left"):
                self.time_left = int(value)
            elif (name == "game_type"):
                self.game_type = int(value)
            elif (name == "rule"):
                self.rule = int(value)
            elif (name == "evaluate"):
                self.evaluate = (int(value[0]), int(value[1]))
            elif (name == "folder"):
                self.folder = value
            else:
                return (False)
            return (True)
        except ValueError:
            return (ValueError)
