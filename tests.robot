*** Settings ***
Library             tests.HangmanTest  WITH NAME  HangmanTest
Test Setup  Set Up

*** Test Cases ***
Hangman - Deviner une lettre juste
    [Documentation]  On vérifie que lorsque devine une lettre correcte, on ne perd pas de vie
    Guess Letter  True

Hangman - Deviner une mauvaise lettre
    [Documentation]  On vérifie que si une mauvaise lettre est donnée, le mot n'est pas mis à jour et on perd une vie
    Guess Letter  False

Hangman - Partie terminée, on a deviné le mot
    [Documentation]  On vérifie que la partie se termine si le 
    Guess Word Letter  True
    Guess Word Word


Hangman - Partie terminée, on a perdu
    [Documentation]  Vérifie que la partie se termine quand on a plus de vies
    Guess Word Letter  False

Hangman - Mot incorrect
    Guess Incorect Word