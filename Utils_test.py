"""
A general purpose python file. This file will contain general information and operations we need
for our game.
1. SCORES_FILE_NAME - A string representing a file name. By default “Scores.txt”
2. BAD_RETURN_CODE - A number representing a bad return code for a function.
3. Screen_cleaner - A function to clear the screen (useful when playing memory game or
before a new game starts).
"""

import os
from time import sleep


class Utils:

    def __init__(self):
        self.SCORES_FILE_NAME = "Scores.txt"
        self.BAD_RETURN_CODE = -1
        self.VALID_RANGE = 0

    def screen_cleaner(self):
        return os.system('cls' if os.name == 'nt' else 'clear')

    def input_validator(self, VALID_RANGE):
        while True:
            try:
                # game selection
                input_number = int(input())
            # check if entered numbers only
            except ValueError:
                print("""*********************************
        **  Please enter numbers only  **
        *********************************""")
                continue
            # check if entered numbers in valid range only
            if not 1 <= input_number <= self.VALID_RANGE-1:
                print(f'*******************************************'
                      f'**  Please choose game from 1 to {self.VALID_RANGE-1} only  **'
                      f'*******************************************')
                continue
            else:
                break


Utils = Utils()
# test.screen_cleaner()

