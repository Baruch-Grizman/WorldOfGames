"""
The purpose of this file is to call the functions from Live.py
"""

from Live_test import Live
import GuessGame_test
import MemoryGame_test
import CurrencyRouletteGame_test

# call the functions from Live.py
print(Live.welcome())
print(Live.load_game())


# Launch game based on user selection
# def launch_game():
#     if Live.GAME == 1:
#         memorygame = MemoryGame_test.MemoryGame()
#         memorygame.play()
#     elif Live.GAME == 2:
#         guessgame = GuessGame_test.GuessGame()
#         guessgame.play()
#     elif Live.GAME == 3:
#         currencyrouletteGame = CurrencyRouletteGame_test.CurrencyRouletteGame()
#         currencyrouletteGame.play()
#
#
# launch_game()

while True:
    # print(Live.welcome())
    # print(Live.load_game())
    # launch_game()

    play_again = input('\nWould you like to play again? Yes/No ').lower()
    while play_again == 'yes' or play_again == 'y':
        # print(Live.welcome())
        print(Live.load_game())
        # launch_game()
        break

    while play_again == 'no' or play_again == 'n':
        print('Goodbye')
        break

    else:
        print('Please enter yes or no only')
