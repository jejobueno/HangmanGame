# Hangman-Game

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-360/)

The Hangman game is a simple game where one or more players try to guess a word, each turn suggesting a letter.

After each turn, it will print a resume of the game that looks like:
```
######  RESUME OF THE GAME ########"
Correctly guessed letters: List[chr],
Bad guessed letters: List[chr],
Lives remaining: int,
Error count: int
This is the turn # : int
```
The player will have 5 lives, that means only 5 opportunities to give a wrong asnwer. After this, the game is over!

- ## Why?
This is the first code I've made in becode to practice my python knowledge and object oriented programming.

- ## How?
The scrips is made of a object `Hangman()` which will be initialized in the `main.py` file and have the following attibrutes and functions:

### Attributes:

   - `possible_words`:
      It contains a list of words. Out of these words, one will be
    selected as the word to find. The list must also contain the following words:
    ['becode', 'learning', 'mathematics', 'sessions'].
   - `word_to_find`: 
      attribute that contains a list of strings. Each element will be a letter of
    the word.
   - `lives`:
   attribute that contains the number of lives that the player still has left. It should
    start at 5.
   - `correctly_guessed_letters`:
   attribute that contains a list of strings where each element will
    be a letter guessed by the user. At the start, it should be equal to: ```['_', '_', '_', '_', '_']```, with the
     same number of '_' as the length of the word to find.
   - `wrongly_guessed_letters`:
    attribute that contains a list of strings where each element will be
   a letter guessed by the user that is not in the word_to_find.
   - `turn_count`:
      attribute that contain the number of turns played by the player. This will be
   represented as an int.
   -`error_count`: attribute that contains the number of errors made by the player.
   
### Methods:

  - `__init__(self, possible_words: List[str])`:
        This method initialize the Hangman object with a list of possbile words
        :param possible_words: contains all possible word that can be chosen
        as word to find. Default value = ["becode", "learning", "mathematics", "sessions"]
  - `game_over(self)`:
       This method will print 'game over...' before breaking the loop
       and finishing the game.
   
  - `play(self)`:
       `play()` method will has to the player for a single letter, if it is not
       a letter it will ask again a new input. If it is a uppercase later it
       transform it in a lowercase letter.
       :self.turn_count: is increased by one each time the player plays
       The method checks if word_to_find contains the letter,
       :if True: it sets the letter in the correspondent indexes in the
       `correctly_guessed_letters` attribute.
      :if False: it sets the letter in the correspondent indexes in the
       `wrongly_guessed_letters` attribute, incrementing the `error_count` and
       decreasing the `lives` attributes by one.
   
  - `start_game(self)`:
       This function will first to choose randomly one of the "possible words" and
       saves it as a list of single chars into `word_to_find` attribute. Then create
       a list of spaces of the same size as `word_to_find`and initialize all the attributes.
       Afterwards, it calls the `play()` method letting the user play.
       If the player has no more lives, it calls the `game_over()` method
       If the player has guessed correctly the word, it calls `well_played()` method
       (`correctly_guessed_letters == self.word_to_find`)
   
  - `well_played(self)`:
       This method will print a review of the game after the player guessed
       correctly the word. It prints the guessed word (`word_to_find`), and the
       count of turns and error
 

