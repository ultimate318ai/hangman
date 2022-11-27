"""
This file is used for hangman game.
"""
import random


class Hangman:
    """
    Class used for hangman game.
    """

    __word: str = None
    __letters_found: list[str] = None
    __false_letters: set[str] = None
    __lives: int = 0
    __word_has_been_guessed: bool = None

    def __init__(self) -> None:
        with open("liste_francais.txt", "r", encoding="utf8") as word_file:
            self.__word = random.choice(word_file.readlines())[:-1]
        self.__lives = len(self.__word) + 5
        self.__letters_found = ["_" for _ in self.__word]
        self.put_know_letter(
            self.__word[0], verbose=False
        )  # The first letter is alway printed!
        self.__false_letters = set()
        self.__word_has_been_guessed = False

    def __is_letter_in_word(self, letter: str) -> bool:
        """
        check if the letter is in the word used for the game.
        Args:
            letter (str): the letter used for checking.
        Returns:
            bool: True if the letter is in the word, False otherwise.
        """
        return letter in self.__word

    def get_word(self) -> str:
        """
        Return the initial word to guess.
        """
        return self.__word

    def put_know_letter(self, letter: str, verbose=True):
        """
        If the letter is in the word, update the content displayed, else decrease by 1 user life
        and add letter to wrong ones list.
        Args:
            letter (str): the letter to put in the found letters if the letter is in word.
            verbose (bool): If True, the print messages will be displayed.
        """
        if self.__is_letter_in_word(letter):
            print(verbose * f"{letter=} was in word !")
            for index, _letter in enumerate(self.__word):
                if _letter == letter:
                    self.__letters_found[index] = _letter
        else:
            print(verbose * f"{letter=} was not in word....")
            self.__lives -= 1
            self.__false_letters.add(letter)

    def put_know_word(self, word: str):
        """
        If the word is the word expected, player should won,
        else, add word to wrong list and decrease by 2 player life.
        Args:
            word (str): The word given.
        """
        if word == self.__word:
            print("This was the word GG bro !")
            self.__word_has_been_guessed = True
        else:
            print("This was not the word... ")
            self.__lives -= 2
            self.__false_letters.add(word)

    def is_game_over(self) -> bool:
        """
        Returns:
            bool: True if the game is finished, False otherwise.
        """
        return (
            self.__lives <= 0
            or self.__word_has_been_guessed
            or ("_" not in self.__letters_found)
        )

    def is_word_guess_by_user_prompt(self) -> bool:
        """
        Return True if the word has been guessed by the user, entering the full word.
        """
        return self.__word_has_been_guessed

    def get_game_stats(
        self,
    ) -> tuple[int, int, int]:
        """
        Return the following information :
            - nb lives left
            - word len
            - letter_standing (if the word has been found in word attempt)
        """
        return (
            self.__lives,
            len(self.__word),
            self.__letters_found.count("_"),
        )

    def __repr__(self) -> str:
        return f"Word to guess : \033[1;32;40m{self.__letters_found} \033[1;37;40m. Wrong letters : \033[1;31;40m {list(self.__false_letters)} \033[1;37;40m"
