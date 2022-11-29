"""
Ce module implemente le jeu du pendu.
"""
import random


class Hangman:
    """
    Class du jeu du pendu.
    """
    # Declaration des attributs de classes

    # Mot à devinner
    __word: str = None
    # Liste de lettre trouvée
    __letters_found: list[str] = None
    # Liste de lettre utilisée mais pas dans le mot
    __false_letters: set[str] = None
    # Mots devinées qui ne sont pas le mot
    __false_words: set[str] = None
    # Nombre de vies 
    __lives: int = 0
    # Est-ce que le mot a été deviné ?
    __word_has_been_guessed: bool = None

    def __init__(self) -> None:
        with open("liste_francais.txt", "r", encoding="utf8") as word_file:
            self.__word = random.choice(word_file.readlines())[:-1]
        self.__lives = len(self.__word) + 5
        self.__letters_found = ["_" for _ in self.__word]
        self.put_know_letter(
            self.__word[0], verbose=False
        )  # On devoile toujours la première lettre!
        self.__false_letters = set()
        self.__false_words = set()
        self.__word_has_been_guessed = False

    def __is_letter_in_word(self, letter: str) -> bool:
        """
        Vérifie si la lettre est dans le mot a deviner.
        Args:
            letter (str): la lettre.
        Returns:
            bool: True si la lettre est dans le mot, False sinon.
        """
        return letter in self.__word

    def get_word(self) -> str:
        """
        Renvoie le mot à deviner.
        """
        return self.__word

    def put_know_letter(self, letter: str, verbose=True):
        """
        Si la lettre est dans le mot à deviner, devoile son/ses emplacement(s),
        sinon ajoute la lettre à la liste des lettres fausses et diminue d'une vie.
        Args:
            letter (str): La lettre a mettre dans la liste des lettres trouvées.
            verbose (bool): Si True, affiche le print.
        """
        
        if ...: # Si la lettre est dans le mot à deviner
            print(verbose * f"{letter=} was in word !")
            for index, _letter in enumerate(...): # On parcourt les lettres du mot
                if _letter == letter:
                    self.__letters_found[...] = ... # Decouvre la lettre à son emplacement si la lettre du mot correspond à la lettre deviné
        else:
            print(verbose * f"{letter=} was not in word....")
            self.__lives = ... # Diminue le nombre de vies
            self.__false_letters.add(...) # Ajoute la lettre trouvée à la liste des mauvaises lettres

    def put_know_word(self, word: str):
        """
        Si le mot est deviné, le joueur gagne la partie.
        sinon, sinon on ajoute le mot à la liste des mauvais mot,
        et on diminue de 2 les vies.
        Args:
            word (str): Le mot donné.
        """
        if word == self.__word:
            print("This was the word GG bro !")
            self.__word_has_been_guessed = ... # Mettre à jour la condition de victoire
        else:
            print("This was not the word... ")
            self.__lives = ...  # Diminue le nombre de vie par 2
            self.__false_words.add(word)

    def is_game_over(self) -> bool:
        """
        Returns:
            bool: True si la partie est terminée, False sinon.
        """
        return (
            self.__lives <= 0
            or self.__word_has_been_guessed
            or ("_" not in self.__letters_found)
        )

    def is_word_guess_by_user_prompt(self) -> bool:
        """
        Return True si le mot a été deviné par l'utilisateur, en entrant le mot complet.
        """
        return self.__word_has_been_guessed

    def get_game_stats(
        self,
    ) -> tuple[int, int, int]:
        """
        Renvoie les informations suivantes :
            - nombre de vies restantes.
            - longueur du mot.
            - nombre de lettres restantes à être trouvées.
        """
        return (
            self.__lives,
            len(self.__word),
            self.__letters_found.count("_"),
        )

    def __repr__(self) -> str:
        return f"Word to guess : \033[1;32;40m{self.__letters_found} \033[1;37;40m. Wrong letters : \033[1;31;40m {list(self.__false_letters) + list(self.__false_words)} \033[1;37;40m"
