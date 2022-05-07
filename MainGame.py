"""
The purpose of this file is to call the functions from Live.py
"""

from Live import Live
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame

# call the functions from Live.py
print(Live.welcome())
print(Live.load_game())

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


