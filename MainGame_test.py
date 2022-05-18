"""
The purpose of this file is to call the functions from Live.py
"""

from Live_test import *
from GuessGame_test import GuessGame
from MemoryGame_test import MemoryGame
from CurrencyRouletteGame_test import CurrencyRouletteGame

# call the functions from Live.py
print(Live.welcome())
Live.load_game()

# Launch game based on user selection
if Live.GAME == 1:
    MemoryGame = MemoryGame()
    MemoryGame.play()
elif Live.GAME == 2:
    GuessGame = GuessGame()
    GuessGame.play()
elif Live.GAME == 3:
    CurrencyRouletteGame = CurrencyRouletteGame()
    CurrencyRouletteGame.play()


# Launch game based on user selection
# def launch_game():
#    if Live.GAME == 1:
#        MemoryGame = MemoryGame_test.MemoryGame()
#        MemoryGame.play()
#    elif Live.GAME == 2:
#        GuessGame = GuessGame_test.GuessGame()
#        GuessGame.play()
#    elif Live.GAME == 3:
#        CurrencyRouletteGame = CurrencyRouletteGame_test.CurrencyRouletteGame()
#        CurrencyRouletteGame.play()
#
#


# launch_game()

# while True:
#
#     play_again = input('\nWould you like to play again? Yes/No ').lower()
#     while play_again == 'yes' or play_again == 'y':
#         # print(Live.welcome())
#         print(Live.load_game())
#         # launch_game()
#         break
#
#     if play_again == 'no' or play_again == 'n':
#         print('Goodbye')
#         break
#
#     else:
#         print('Please enter yes or no only')
