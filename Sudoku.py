# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 22:33:56 2022

@author: louva
"""

import numpy as np
from Grille import genererGrille


class Sudoku:
    def __init__(self, data):
        """
        initialise le sudoku
        """
        self.tableau = data  # tableau initiale - celui à résoudre
        self.solution = np.zeros((9, 9))  # initialisation - tableau solution

    def presence_valeur(self, i, j, val):
        """
        test booleen pour savoir si un chiffre est déjà dans le tableau
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
        détermine les indices de la case suivante pour la recherche
        """
        # on avance
        j = j + 1
        val = 1
        if j > 9:
            i = i + 1
            j = 1
        return i, j, val

    def recule(self, i, j, val):
        """
        détermine les indices de la case précédente pour la recherche
        """
        # on recule
        j = j - 1
        if j < 0:
            j = 8
            i = i - 1
        # on efface la valeur precedente
        # puis on teste la valeur suivante
        val = self.solution[i, j] + 1
        if self.tableau[i, j] == 0:
            self.solution[i, j] = 0
        else:
            i, j, val = self.recule(i, j, val)
        return i, j, val

    def deplacement(self, i, j, val):
        """
        gère le suivi de la case de recherche
        """
        if val < 10:
            return self.avance(i, j, val)
        else:
            return self.recule(i, j, val)

    def solve(self):
        """
        resolution récursive du sudoku
        """
        self.solution = np.copy(self.tableau)
        # on parcours tout le self.tableau
        i = 0
        while i < 9:
            j = 0
            val = 1
            while j < 9:
                # on teste toutes les valeurs
                if self.tableau[i, j] == 0 and val < 10:
                    if self.presence_valeur(i, j, val):
                        val += 1
                    else:
                        self.solution[i, j] = val
                        i, j, val = self.deplacement(i, j, val)
                else:
                    i, j, val = self.deplacement(i, j, val)
            i = i + 1


if __name__ == '__main__':

    tab_inconnu = genererGrille(15, 25)
    grid = np.array(tab_inconnu)
    mSudok = Sudoku(grid)
    mSudok.solve()
    print(mSudok)
