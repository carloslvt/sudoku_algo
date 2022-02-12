# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 22:33:56 2022

@author: louva
"""

import numpy as np
from Grille import genererGrille


class Sudoku:
    def __init__(self, data):
        self.tableau = data  # tableau initiale - celui à résoudre
        self.solution = np.zeros((9, 9))  # initialisation - tableau solution

    def presence_valeur(self, i, j, val):
        """
        Vérifier si le nombre (val) qui tente d'être placé dans la grille
        n'est pas présente dans la ligne, la colonne, ou le carré
        :param i: la ligne de la grille
        :param j: la colonne de la grille
        :param val: le nombre qui tente d'être placé dans la grille
        :return: True si pas présent et False si présent
        """
        ligne = self.solution[i, :]
        colonne = self.solution[:, j]
        pos_i, pos_j = 3 * (i // 3), 3 * (j // 3)
        carre = self.solution[pos_i:pos_i + 3, pos_j:pos_j + 3]
        return (val in ligne) \
               or (val in colonne) \
               or (val in carre)

    def avance(self, i, j, val):
        """
        Permet de passer à l'index i+1 dans la grille
        :param i: index de la ligne
        :param j: index de la colonne
        :param val: initialise la valeur à 1
        :return: la case suivante dans la grille
        """
        j += 1
        val = 1
        # renvoie à la ligne si on arrive au bout de la grille
        if j > 9:
            i += 1
            j = 1
        return i, j, val

    def recule(self, i, j, val):
        """
        Permet de passer à l'index i-1 dans la grille
        :param i: index de la ligne
        :param j: index de la colonne
        :param val: valeur à l'index (i, j)
        :return: la case precedente dans la grille
        """
        j -= 1
        if j < 0:
            j = 8
            i -= 1

        val = self.solution[i, j] + 1
        if self.tableau[i, j] == 0:
            self.solution[i, j] = 0
        else:
            i, j, val = self.recule(i, j, val)
        return i, j, val

    def deplacement(self, i, j, val):
        """
        Permet d'avancer ou reculer selon l'emplacement dans la grille
        :param i: index de la ligne
        :param j: index de la colonne
        :param val: valeur à l'index (i, j)
        :return: Avance si la valeur est inférieur à 10, recule sinon
        """
        if val < 10:
            return self.avance(i, j, val)
        else:
            return self.recule(i, j, val)

    def solve(self):
        """
        Permet de résoudre le sudoku
        :return: la grille résolu
        """
        self.solution = np.copy(self.tableau)
        # on parcours toutes les lignes du tableau
        i = 0
        while i < 9:
            # on parcours touts les colonnes du tableau
            j = 0
            val = 1
            while j < 9:
                if self.tableau[i, j] == 0 and val < 10:
                    if self.presence_valeur(i, j, val):
                        val += 1
                    else:
                        self.solution[i, j] = val
                        i, j, val = self.deplacement(i, j, val)
                else:
                    i, j, val = self.deplacement(i, j, val)
            i += 1


if __name__ == '__main__':

    tab_inconnu = genererGrille(15, 25)
    grid = np.array(tab_inconnu)
    mSudok = Sudoku(grid)
    mSudok.solve()
    print(mSudok)
