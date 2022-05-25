# Welcome to World of Games (WoG)

This project is part of **DevOps Course** at DevOps-Experts.\
The purpose of the project is to allow the user to play three different games.\
All code is written using **Python**, while using **FLASK** and **HTML** for page creation and publishing.\
Version control is managed in **GIT**

## Project Description
### An explanation of the various files in the project
Live.py - This program is for getting inputs for WorldOfGames, includes name, game, difficulty.\
After selecting the difficulty level, each level is multiplied by 3 times the selected value, in order to give higher weight to the difficulty level

MainGame.py - The purpose of this file is to call the functions from Live.py and run everything.

### The Games
***located in `../WorldOfGames/games/` folder***

MemoryGame.py - The object of the game is to display a quantity (the quantity is based on the difficulty level selected in the initial stage) of random numbers in the range from 1 to 101, for 1.5 seconds.\
The user will then be prompted to enter the numbers based on the memory.\
At the end both the numbers displayed and the numbers guessed will be displayed.\
If the user was right and remembered all the numbers, it will be printed that he succeeded and in addition the score will be added to the score file.\
If the user made a mistake and did not remember all the numbers, it will be printed that he failed and better luck next time.

GuessGame.py - The object of the game is to ask the user to guess a number in the range of 1 and the difficulty level chosen accordingly.\
Then, a comparison is made between the random number of the computer and the number entered by the user.\
Both the random number and the guessed number will appear on the screen.\
If the user correctly guessed the number, it will be printed that he succeeded and in addition the score will be added to the score file.\
If the user does not guess the number correctly, it will be printed that he failed and better luck next time.

CurrencyRouletteGame.py - This game uses the free **CurrencyConverter** api, to get the conversion rate between USD and ILS.\
The object of the game is to show the user a random number in the range 1 to 100, and ask him to write down how much he thinks the value displayed from USD to ILS.\
Depending on the difficulty level selected, the correct value will be within an interval range around the correct result.\
If the user correctly guessed the value of USD to ILS, it will be printed that he succeeded and in addition the score will be added to the score file.\
If the user does not guess the value of USD to ILS correctly, it will be printed that he failed and better luck next time.

### Data files
***located in `../WorldOfGames/data/` folder***

Utils.py - This file contains variables and functions for general project use.\
*SCORES_FILE_NAME* - A string representing “Scores.txt” file name. Used in the Score.py and MainScores.py files.\
*BAD_RETURN_CODE* - A value that represents an error in case of a function error, Used in MainScores.py file.\
screen_cleaner - Function to clear the screen when starting a new game.\
input_check - Function that checks whether the inserted characters are only numbers and whether they are in the correct range, depending on the requirement in the various files.

Score.py - This file is responsible for keeping the user's score in case of a text file win.\
The score is determined by a formula\
POINTS_OF_WINNING = (DIFFICULTY X 3) + 5\
If there is already a file with a score, the new score will be added to the existing one.\
If no score file exists, a new file will be created.

MainScores.py - This file is responsible for reading the score file and publishing it to HTTP using HTML, this process will be done using Python FLASK library.\
In the event of an error in reading the score file, the error code we defined will be displayed.


## Execution
The Python version, used for this project is 3.10\
All required dependencies are in the file **requirements.txt**\
Run **MainGame.py**, you will be prompt to enter Name, choose Game, and select Difficulty
