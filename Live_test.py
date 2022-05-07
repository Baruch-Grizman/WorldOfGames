"""
this program is for getting inputs for WorldOfGames, includes name, game, difficulty
"""

import GuessGame_test
import MemoryGame_test
import CurrencyRouletteGame_test
class Live:

    def __init__(self):
        self.NAME = input('Please enter your name: ')
        self.GAME = 0           # game selection
        self.DIFFICULTY = 0     # difficulty selection
        self.GAME_DIFF = 0      # in game difficulty for all games

    def welcome(self):
        return f'Hello {Live.NAME} and welcome to the World of Games (WoG).' \
               f'\nHere you can find many cool games to play.\n'

    # getting inputs for WorldOfGames
    def load_game(self):
        while True:
            try:
                # game selection
                self.GAME = int(input("""Our Games:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you choose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS

    Please choose a game to play: """))
            # check if entered numbers only
            except ValueError:
                print("""*********************************
**  Please enter numbers only  **
*********************************""")
                continue
            # check if entered numbers in valid range only
            if not 1 <= self.GAME <= 3:
                print("""*******************************************
**  Please choose game from 1 to 3 only  **
*******************************************""")
                continue
            else:
                break

        while True:
            try:
                # difficulty selection
                self.DIFFICULTY = int(input('Please choose game difficulty from 1 to 5: '))
            # check if entered numbers only
            except ValueError:
                print("""*********************************
**  Please enter numbers only  **
*********************************""")
                continue
            # check if entered numbers in valid range only
            if not 1 <= self.DIFFICULTY <= 5:
                print("""*************************************************
**  Please choose difficulty from 1 to 5 only  **
*************************************************""")
                continue
            else:
                break
        # settings in game difficulty for all games
        if self.DIFFICULTY == 1:
            self.GAME_DIFF = 3
        elif self.DIFFICULTY == 2:
            self.GAME_DIFF = 6
        elif self.DIFFICULTY == 3:
            self.GAME_DIFF = 9
        elif self.DIFFICULTY == 4:
            self.GAME_DIFF = 12
        elif self.DIFFICULTY == 5:
            self.GAME_DIFF = 15


Live = Live()

# Launch game based on user selection
if Live.GAME == 1:
    memorygame = MemoryGame_test.MemoryGame()
    memorygame.play()
elif Live.GAME == 2:
    guessgame = GuessGame_test.GuessGame()
    guessgame.play()
elif Live.GAME == 3:
    currencyrouletteGame = CurrencyRouletteGame_test.CurrencyRouletteGame()
    currencyrouletteGame.play()

# print(Live.welcome())
# print(Live.load_game())
# print(Live.GAME)
# print(Live.DIFFICULTY)
# print(Live.GAME_DIFF)
