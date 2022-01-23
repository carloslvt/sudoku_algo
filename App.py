from Sudoku import Sudoku
import tkinter as tk
import numpy as np
from Grille import genererGrille

class App:
    def __init__(self, fenetre=None):
        """
        initialise la page principale
        :param fenetre: la fenetre interface
        """
        self.fenetre = fenetre
        self.fenetre.title("Sudoku")
        self.fenetre.geometry("760x655")
        self.fenetre.config(background='#41B77F')
        self.fenetre.resizable(False, False)

        # mise en place d'un cadre pour contenir les widgets
        self.frame = tk.Frame(self.fenetre, bg='#41B77F')
        self.frame.grid()

        self.grille_alea = Grille_aleatoire(master=self.fenetre, app=self)
        self.grille_vide = Grille_vide(master=self.fenetre, app=self)

        # creation des composants
        self.widgets()

        # empaquetage
        self.frame.pack(expand=tk.YES)

    def widgets(self):
        """
        regroupe les widgets (titre, sous-titre, boutons)
        :return: titre, sous-titre, boutons
        """
        self.titre()
        self.sous_titre()
        self.boutons()

    def titre(self):
        """
        Creation du titre
        :return: titre
        """
        titre = tk.Label(self.frame, text="Sudoku", font=("Courrier", 40), bg='#41B77F',
                                    fg='white')
        titre.grid()

    def sous_titre(self):
        """
        Creation du sous-titre
        :return: sous-titre
        """
        sous_titre = tk.Label(self.frame, text="Vous voulez jouer ?", font=("Courrier", 25), bg='#41B77F',
                                       fg='white')
        sous_titre.grid()

    def boutons(self):
        """
        Creation des différents boutons
        :return: bouton resoudre, nouveau, quitter
        """
        aleatoire = tk.Button(self.frame, text="Grille aléatoire", font=("Courrier", 25), bg='white', fg='#41B77F',
                                    command= self.grilleAlea, width=15)
        aleatoire.grid(pady=50,padx=50)

        vide = tk.Button(self.frame, text="Grille vide", font=("Courrier", 25), bg='white', fg='#41B77F',
                               command= self.grilleVide, width=18)
        vide.grid()

        quitter = tk.Button(self.frame, text="Quitter", font=("Courrier", 25), bg='white', fg='#41B77F',
                         command=self.quitter, width=18)
        quitter.grid(pady=50)

    def page_principale(self):
        self.frame.pack()

    def grilleAlea(self):
        self.frame.pack_forget()
        self.grille_alea.page()

    def grilleVide(self):
        self.frame.pack_forget()
        self.grille_vide.page()

    def quitter(self):
        """
        Retourne sur le menu principal
        :return: page principale
        """
        self.fenetre.destroy()


class Grille_aleatoire:
    def __init__(self, master=None, app=None):
        """
        initialise la grille aléatoire
        :param master: lien avec la page principale
        :param app:
        """
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)

        # creation de la grille
        self.grille()

        # creation des boutons
        self.boutons()

    def boutons(self):
        """
        Creation des différents boutons
        :return: bouton resoudre, nouveau, quitter
        """
        self.resoudre = tk.Button(self.frame,text = 'Résoudre',
                                        font=("Courrier", 15), bg='white', fg='black', command=self.resoudre)
        self.resoudre.grid(column=0, row=10, columnspan=3)

        self.relancer = tk.Button(self.frame, text='Nouveau',
                                        font=("Courrier", 15), bg='white', fg='black', command=self.nouveau)
        self.relancer.grid(column=3, row=10, columnspan=3)

        self.quitter = tk.Button(self.frame, text='Quitter',
                                       font=("Courrier", 15), bg='white', fg='black', command=self.quitter)
        self.quitter.grid(column=6, row=10, columnspan=3)

    def grille(self):
        """
        initialisation des entrees et ajout a la fenetre
        :return: grille vide
        """
        self.entree = []
        for i in range(9):
            self.entree += [[]]
            for j in range(9):
                self.entree[i] += [tk.StringVar()]
        for i in range(9):
            for j in range(9):
                if (i // 3 == 0 and j // 3 == 0) or (i // 3 == 0 and j // 3 == 2) or (i // 3 == 2 and j // 3 == 0) or (
                        i // 3 == 2 and j // 3 == 2) or (i // 3 == 1 and j // 3 == 1):
                    tk.Entry(self.frame, textvariable=self.entree[i][j],
                                  width=3, font=("Calibri", 40), justify='center', bg="#41B77F"
                                  ).grid(row=i, column=j)
                else:
                    tk.Entry(self.frame, textvariable=self.entree[i][j],
                                  width=3, font=("Calibri", 40), justify='center', bg="white"
                                  ).grid(row=i, column=j)
                self.entree[i][j].set("")

    def resoudre(self):
        """
        résoud le sudoku et affiche la solution
        :return: grille sudoku résolue
        """
        # on recupere les valeurs
        tableau = np.zeros((9, 9))
        for i in range(9):
            for j in range(9):
                val = self.entree[i][j].get()
                if est_valide(val):
                    val = int(val)
                else:
                    val = 0
                tableau[i, j] = val

        # on resout le sudoku
        grid = tableau.astype(int)
        mSudok = Sudoku(grid)
        mSudok.solve()

        # on affiche la solution
        for i in range(9):
            for j in range(9):
                self.entree[i][j].set(str(int(mSudok.solution[i, j])))
        return

    def nouveau(self):
        """
        on reinitialise le tableau d'entrees
        :return: grille aleatoire
        """
        grid = genererGrille(30, 35)
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                self.entree[i][j].set(grid[i][j])
                j += 1
            i += 1

    def quitter(self):
        """
        Retourne sur le menu principal
        :return: page principale
        """
        self.frame.pack_forget()
        self.app.page_principale()

    def page(self):
        self.frame.pack()

class Grille_vide:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)

        # creation de la grille
        self.grille()

        # creation des boutons
        self.boutons()

    def boutons(self):
        """
        Creation des différents boutons
        :return: bouton resoudre, nouveau, quitter
        """
        # boutons
        self.resoudre = tk.Button(self.frame, text='Résoudre',
                                        font=("Courrier", 15), bg='white', fg='black', command=self.resoudre)
        self.resoudre.grid(column=0, row=10, columnspan=3)

        self.relancer = tk.Button(self.frame, text='Nouveau',
                                        font=("Courrier", 15), bg='white', fg='black', command=self.nouveau)
        self.relancer.grid(column=3, row=10, columnspan=3)

        self.quitter = tk.Button(self.frame, text='Quitter',
                                       font=("Courrier", 15), bg='white', fg='black', command=self.quitter)
        self.quitter.grid(column=6, row=10, columnspan=3)

    def grille(self):
        """
        initialisation des entrees et ajout a la fenetre
        :return: grille vide
        """
        self.entree = []
        for i in range(9):
            self.entree += [[]]
            for j in range(9):
                self.entree[i] += [tk.StringVar()]
        for i in range(9):
            for j in range(9):
                if (i // 3 == 0 and j // 3 == 0) or (i // 3 == 0 and j // 3 == 2) or (i // 3 == 2 and j // 3 == 0) or (
                        i // 3 == 2 and j // 3 == 2) or (i // 3 == 1 and j // 3 == 1):
                    tk.Entry(self.frame, textvariable=self.entree[i][j],
                                  width=3, font=("Calibri", 40), justify='center', bg="#41B77F"
                                  ).grid(row=i, column=j)
                else:
                    tk.Entry(self.frame, textvariable=self.entree[i][j],
                                  width=3, font=("Calibri", 40), justify='center', bg="white"
                                  ).grid(row=i, column=j)
                self.entree[i][j].set("")

    def resoudre(self):
        """
        résoud le sudoku et affiche la solution
        :return: grille sudoku résolue
        """
        # on recupere les valeurs
        tableau = np.zeros((9, 9))
        for i in range(9):
            for j in range(9):
                val = self.entree[i][j].get()
                if est_valide(val):
                    val = int(val)
                else:
                    val = 0
                tableau[i, j] = val

        # on resoud le sudoku
        mSudok = Sudoku(tableau)
        mSudok.solve()

        # on affiche la solution
        for i in range(9):
            for j in range(9):
                self.entree[i][j].set(str(int(mSudok.solution[i, j])))
        return

    def nouveau(self):
        """
        on reinitialise le tableau d'entrees
        :return: grille vide
        """
        for i in range(9):
            for j in range(9):
                self.entree[i][j].set("")
        return

    def quitter(self):
        """
        Retourne sur le menu principal
        :return: page principale
        """
        self.frame.pack_forget()
        self.app.page_principale()

    def page(self):
        self.frame.pack()


def est_valide(val):
    """
    test la valeur dans les cases
    - vrai si nombre entier entre 1 et 10
    - faux sinon
    """
    try:
        val=int(val)
        if val>0 and val<10:
            return True
        else:
            return False
    except:
        return False


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()