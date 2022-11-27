"""_hangman_
This is here that all start!
"""

import argparse
import textwrap

from argparse import ArgumentParser

from hangman import Hangman


WELCOME_MESSAGE: str = """

Welcome to this project, the purpose if this file is to understand how does automated 
tests are done on project. This one is not exhaustive but it is used for interactive introduction

"""

CONTEXTUAL_MENU: str = """
              What do you want to do ?
              
              1) Give a letter
              2) Give the word
              3) quit
              """

RULES: str = """
        \033[1;31;43m Les règles du pendu :\033[0;37;40m
    
    - Un mot est tiré\033[1;36;40m au hazard.\033[0;37;40m 
    
    - Ta mission sera\033[1;35;40m de le deviner !\033[0;37;40m

    - Tu peux donner une lettre ou un mot en entier
        + Si\033[2;32;40m la lettre est dans le mot\033[0;37;40m (au moins une fois) :  La lettre est affichée. Sinon...\033[1;31;40m mwouhahaha \033[0;37;40m
        + Si\033[2;32;40m le mot donné est le bon\033[0;37;40m, tu gagnes tout de suite ! Sinon...\033[1;31;40m sanction\033[0;37;40m
    
    -\033[2;34;40m Les scores :\033[0;37;40m
        + Mot trouvé avec que des lettres données : (nombre de vie restantes + taille du mot) - tentatives
        + Mot deviné en entier (en donnant le mot) :(nombre de vie restantes + taille du mot) + (2 * nb de lettres restante) - tentatives
"""


def launch_welcome_menu():
    """_hmmmmmmmm_
    What a strange function, I don't know what does it does, but it does it well (I hope).
    """

    def parse_args(parser: ArgumentParser):
        """_parse args function_
        :param parser: the parser used to get the arguments (mdr)
        """
        # print(parser.parse_args())
        # print(parser.parse_args().play)
        match (args := parser.parse_args()):
            case _ if args.play:
                print("play!")
                play()
            case _ if args.display:
                print("display")
                display_the_game_rules()
            case _:
                if not any(args._get_args()):
                    print("You did'nt gave an argument, such a shame... :(")
                else:
                    print("Unknown argument given : {_}")

    parser = argparse.ArgumentParser(description=textwrap.dedent(WELCOME_MESSAGE))
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-p",
        "--play",
        help="Use this argument if you want to play",
        action="store_true",
    )
    group.add_argument(
        "-d",
        "--display",
        help="display the rules",
        action="store_true",
    )
    parse_args(parser)


def main():
    """
    Main function of the program, will be launched first.
    """
    launch_welcome_menu()


def play():
    """mdr"""
    hangman = Hangman()
    player_quit: bool = False
    attempts: int = 0
    while not (hangman.is_game_over() or player_quit):
        print(hangman)
        print(textwrap.dedent(CONTEXTUAL_MENU))
        try:
            input_player: int = int(input())
            match input_player:
                case 1:
                    letter_given = input("Give your letter : ")
                    hangman.put_know_letter(letter_given)
                case 2:
                    word_given = input("Give the word : ")
                    hangman.put_know_word(word_given)
                case 3:
                    print("bye bye!")
                    player_quit = True
        except ValueError:
            print("Your value is not correct, retry please")
        except KeyboardInterrupt:
            print("bye bye!")
            player_quit = True
        attempts += 1
    (
        nb_lives_standing,
        length_initial_word,
        nb_letter_to_guess_standing,
    ) = hangman.get_game_stats()
    score = (
        (
            nb_lives_standing
            + length_initial_word
            - attempts
            + hangman.is_word_guess_by_user_prompt() * nb_letter_to_guess_standing
        )
        if not player_quit
        else 0
    )
    if nb_lives_standing <= 0:
        print("plus de vie restante!")
    print(f"The initial word was : {hangman.get_word()}")
    print(f"Your score : {score}")


def display_the_game_rules():
    """
    Display the hangman rules.
    """
    print(textwrap.dedent(RULES))


if __name__ == "__main__":
    main()
