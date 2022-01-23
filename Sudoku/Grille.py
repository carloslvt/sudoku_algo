# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 22:51:47 2022

@author: louva
"""

from random import *

def grilleValideAleatoire():
    """
    Renvoie une matrice 9x9 d'entiers choisis au hasard qui constitue une
    grille valide (d'apres les criteres Sudoku).
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
    renommageAleatoire(M)
    return M

def renommageAleatoire(M):
    """
    Rajoute un entier aleatoire modulo 9 puis incremente chaque entree de M.
    """
    p = randint(1, 8)
    for i in range(9):
        for j in range(9):
            M[i][j] = (M[i][j] + p) % 9 + 1

def genererGrille(casesRestantesMin=17, casesRestantesMax=26):
    """
    Genere une grille à résoudre pour l'utilisateur, en partant d'une grille
    valide. Le nombre de cases restantes sera choisi aleatoirement dans l'intervalle fourni.
    """
    M = grilleValideAleatoire()
    nb_restants = randint(casesRestantesMin,casesRestantesMax)  # le nombre de cases qu'on va laisser
    n = len(M)
    nb_elem = n * n  # 81 dans le cas du Sudoku classique
    # generer des paires d'indices valides aleatoires tant qu'on doit supprimer
    # des elements
    while nb_elem > nb_restants:
        i, j = randint(0, n - 1), randint(0, n - 1)
        if M[i][j] != 0:  # si l'element n'a pas encore ete efface
            M[i][j] = 0  # l'effacer
            nb_elem -= 1  # mettre a jour le nombre d'elements


    return M


if __name__ == '__main__':
    print(genererGrille(30, 40))