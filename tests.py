"""
_File used for testing the hangman_

This file is typically a QA file, the things done here are quite mysterious but...
you don't need to change it, just make them PASS !
"""
import string

from random import choice
from numpy.random import choice as npchoice

from hangman import Hangman

class TestFailedError(Exception):
    "Classe pour les erreurs de tests"


class HangmanTest:
    """_Hangman test class_
    Here all the tests are written, we use python because it is less
    complicated and.... more fun !
    """

    ROBOT_LIBRARY_SCOPE = "TEST"

    def set_up(self):
        """
        Setup all the components needed.
        """
        self.hangman = Hangman()

    def guess_letter(self, good=True):
        """
        Devine une lettre correcte si good, devine une lettre pas dans le mot sinon.
        """
        word = self.hangman.get_word()
        chosen_letter = choice(word)
        while (chosen_letter in list(word)) ^ (not good):
            chosen_letter = choice(string.ascii_lowercase)

        lives_before, _, _ = self.hangman.get_game_stats()
        self.hangman.put_know_letter(chosen_letter, verbose=False)
        lives_after, _, _ = self.hangman.get_game_stats()

        try:
            assert (lives_after == lives_before) ^ good
        except AssertionError as error:
            raise TestFailedError(f"Chose letter {chosen_letter} and expected word was {word} and expected to {'I was supposed to guess a good letter' if good else 'I was supposed to lose a life'}") from error

    def guess_word_letter(self, good=True):
        """
        Devine le mot lettre par lettre si good est true.
        Perds la partie lettre par lettre sinon
        """
        N = len(self.hangman.get_word()) if good else self.hangman.get_game_stats()[0]
        for i in range(N):
            if good:
                self.hangman.put_know_letter(letter=self.hangman.get_word()[i], verbose=False)
            else:
                self.guess_letter(good=good)

        try:
            assert self.hangman.is_game_over()
            assert self.hangman.get_game_stats()[0] ^ good
        except AssertionError as error:
            raise TestFailedError("La partie n'est pas terminée") from error

    def guess_word_word(self):
        """
        Devine le mot correctement
        """
        word = self.hangman.get_word()
        self.hangman.put_know_word(word=word)
        try:
            assert self.hangman.is_word_guess_by_user_prompt()
        except AssertionError as error:
            raise TestFailedError("La partie n'est pas gagnée") from error

    def guess_incorect_word(self):
        """
        Devine des mots incorects tant que il reste des vies.
        """
        lives, _, _ = self.hangman.get_game_stats()
        n_iter = 1 + lives//2  if lives % 2 else lives // 2
        for _ in range(n_iter):
            random_word = ''.join(npchoice(list(string.ascii_lowercase), (self.hangman.get_game_stats()[1])))
            self.hangman.put_know_word(random_word)

        try:
            assert self.hangman.is_game_over()
            assert self.hangman.get_game_stats()[0] <= 0
        except AssertionError as error:
            raise TestFailedError("La partie n'est pas terminée") from error

