"""
A package that is in charge of managing the scores file.
The scores file at this point will consist of only a number. That number is the accumulation of the
winnings of the user. Amount of points for winning a game is as follows:
POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
Each time the user is winning a game, the points he won will be added to his current amount of
point saved in a file.
Methods
    1.  add_score - The function’s input is a variable called difficulty. The function will try to read
        the current score in the scores file, if it fails it will create a new one and will use it to save
        the current score.
"""


# from Live_test import *


class Score:

    def __init__(self):
        # self.SCORE_DIFFICULTY = Live.DIFFICULTY
        self.SCORE_DIFFICULTY = 1

    def add_score(self):
        points_of_winning = (self.SCORE_DIFFICULTY*3)+5
        try:
            with open('Scores.txt', encoding='utf-8') as score_file:
                for line in score_file.readlines():
                    points_of_winning += int(line)
            with open('Scores.txt', 'w+', encoding='utf-8') as score_file:
                score_file.write(f'{points_of_winning}')

        except:
            with open('Scores.txt', 'w+', encoding='utf-8') as score_file:
                score_file.write(f'{points_of_winning}')


Score = Score()
print(Score.add_score())



