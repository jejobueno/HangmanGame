import random
import re
from random import randint
from typing import List


class Hangman:
    """
    This object will have the following attributes:
    -> possible_words attribute that contains a list of words. Out of these
     words, one will be selected as the word to find. The list must also
     contain the following words:
     ['becode', 'learning', 'mathematics', 'sessions'].
    -> word_to_find attribute that contains a list of strings. Each element
    will be a letter of the word.
    -> lives attribute that contains the number of lives that the player
    still has left. It should start at 5.
    -> correctly_guessed_letters attribute that contains a list of strings
    where each element will be a letter guessed by the user. At the start,
    it should be equal to: _ _ _ _ _, with the same number of `_` as the
     length of the word to find.
    -> wrongly_guessed_letters attribute that contains a list of strings
     where each element will be
    a letter guessed by the user that is not in the word_to_find.
    -> turn_count attribute that contain the number of turns played by
    the player. This will be represented as an int.
    -> error_count attribute that contains the number of errors made by
     the player.
    """

    possible_words: List[str] 
    word_to_find: List[str] = list()
    lives: int
    correctly_guessed_letters: List[str]
    wrongly_guessed_letters: List[str]
    turn_count: int
    error_count: int

    def __init__(self, possible_words: List[str] = ["becode", "learning", "mathematics", "sessions"]):
        """
         This method initialize the Hangman object choose randomly one of the
        'possible words' and saves it as a list of single chars into
        'word_to_find' attribute. Then create a list of spaces of the same
        size as 'word_to_find'
        :param possible_words: contains all possible word that can be chosen
        as word to find.
        """
        self.possible_words = possible_words
        self.word_to_find: List[chr] = list(random.choice(self.possible_words))
        self.correctly_guessed_letters: List[chr] = ["_"] * len(self.word_to_find)
        self.lives: int = 5
        self.wrongly_guessed_letters: List[str] = list()
        self.turn_count: int = 0
        self.error_count: int = 0

    def play(self):
        """
        Play() method will has to the player for a single letter, if it is not
        a letter it will ask again a new input. If it is a uppercase later it
        transform it in a lowercase letter.
        :self.turn_count: is increased by one each time the player plays
        The method checks if word_to_find contains the letter,
        :if True: it sets the letter in the correspondent indexes in the
        correctly_guessed_letters attribute.
        :if False: it sets the letter in the correspondent indexes in the
        wrongly_guessed_letters attribute, incrementing the error_count and
        decreasing the lives by one.
        """
        while True:
            letter: chr = input("Please enter a letter: ")
            if re.search(r"\b[a-zA-Z]\b", letter):
                if self.wrongly_guessed_letters.__contains__(letter) or self.correctly_guessed_letters.__contains__(
                    letter
                ):
                    print("You've already entered this letter." " Try a new one!")
                else:
                    break
            else:
                print("Please only one letter. Try again!")

        letter = letter.lower()
        self.turn_count += 1

        if self.word_to_find.__contains__(letter):
            indexes = [i for i, x in enumerate(self.word_to_find) if x == letter]
            for index in indexes:
                self.correctly_guessed_letters[index] = letter
        else:
            self.wrongly_guessed_letters.append(letter)
            self.error_count += 1
            self.lives -= 1

    def start_game(self):
        """
        This function will call the "play" method
        letting the user play. If the player has no more lives, it calls the
        "game_over" method. If the player has guessed correctly the word, it
        calls "well_played" method
        (correctly_guessed_letters == self.word_to_find)
        """
        print("Let's start this game!")

        while True:
            self.play()

            if self.lives == 0:
                self.game_over()
                break

            if self.correctly_guessed_letters == self.word_to_find:
                self.well_played()
                break

            print(
                f'######  RESUME OF THE GAME ########"\n'
                f"Correctly guessed letters: "
                f"{''.join(self.correctly_guessed_letters)}\n,"
                f"Bad guessed letters: {self.wrongly_guessed_letters},\n"
                f"Lives remaining: {self.lives},\n"
                f"Error count: {self.error_count},\n"
                f"This is the turn # : {self.turn_count}\n"
            )

    def game_over(self):
        """
        this method will print 'game over...' before breaking the loop
        and finishing the game.
        """
        print("Oups! Game over...")

    def well_played(self):
        """
        This method will print a review of the game after the player guessed
        correctly the word. It prints the guessed word (word_to_find), and the
        count of turns and error
        """
        print(f"You found the word: '{''.join(self.word_to_find)}' in {self.turn_count} turns with {self.error_count} errors!")

