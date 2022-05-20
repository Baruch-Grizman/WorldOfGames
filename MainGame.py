"""
The purpose of this file is to call the functions from Live.py
"""

from Live import *
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame
from Utils import Utils

# call the functions from Live.py
print(Live.welcome())
Live.load_game()

# Launch game based on user selection
if Live.GAME == 1:
    Utils.screen_cleaner()
    MemoryGame = MemoryGame()
    MemoryGame.play()
elif Live.GAME == 2:
    Utils.screen_cleaner()
    GuessGame = GuessGame()
    GuessGame.play()
elif Live.GAME == 3:
    Utils.screen_cleaner()
    CurrencyRouletteGame = CurrencyRouletteGame()
    CurrencyRouletteGame.play()

