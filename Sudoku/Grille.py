# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 22:51:47 2022

@author: louva
"""

from random import *


def nombreAleatoire(M):
    """
    Rajoute un entier en 1 et 9 aléatoirement pour chaque case de la grille
    :param M: la matrice 9x9
    :return: un nombre aléatoire pour chaque case
    """
    p = randint(1, 9)
    for i in range(9):
        for j in range(9):
            M[i][j] = (M[i][j] + p) % 9 + 1


def grilleValide():
    """
    Part d'une grille valide est modifie chaque nombre aléatoirement
    en 1 et 9
    :return: une grille aléatoire valide (matrice 9x9)
    """
    M = [[1, 2, 3, 7, 8, 9, 4, 5, 6],
         [4, 5, 6, 1, 2, 3, 7, 8, 9],
         [7, 8, 9, 4, 5, 6, 1, 2, 3],
         [2, 3, 1, 8, 9, 7, 5, 6, 4],
         [5, 6, 4, 2, 3, 1, 8, 9, 7],
         [8, 9, 7, 5, 6, 4, 2, 3, 1],
         [3, 1, 2, 9, 7, 8, 6, 4, 5],
         [6, 4, 5, 3, 1, 2, 9, 7, 8],
         [9, 7, 8, 6, 4, 5, 3, 1, 2]]

    p = randint(1, 9)
    for i in range(9):
        for j in range(9):
            M[i][j] = (M[i][j] + p) % 9 + 1

    return M


def genererGrille(casesVidesMin = 17, casesVidesMax = 26):
    """
    Genere une grille à résoudre pour l'utilisateur, en partant d'une grille
    valide. Le nombre de cases restantes sera choisi aleatoirement dans l'intervalle fourni.
    :param casesVidesMin: le nombre de case minimum qu'il faudra remplir
    :param casesVidesMax: le nombre de case maximum qu'il faudra remplir
    :return: une grille de sudoku aléatoire valide
    """
    M = grilleValide()
    nb_restant = randint(casesVidesMin, casesVidesMax)  # le nombre de cases à remplir
    n = len(M)
    nb_elem = n * n

    while nb_elem > nb_restant:
        i, j = randint(0, n - 1), randint(0, n - 1)
        if M[i][j] != 0:  # si l'element n'a pas encore ete efface
            M[i][j] = 0  # l'effacer
            nb_elem -= 1  # mettre a jour le nombre d'elements
    return M


if __name__ == '__main__':
    print(genererGrille(30, 40))
