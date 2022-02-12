# sudoku_algo
Projet CAA  : mise en place d'un algorithme pour résoudre un sudoku

# Introduction
Le sudoku est l'un des jeux de puzzle de placement de nombres basés sur la logique les plus populaires. La signification littérale de "Su-doku" en japonais est "le nombre qui est unique".

Le but du jeu est de remplir une grille de neuf par neuf (9x9) avec des chiffres de sorte que chaque ligne, colonne et section 3x3 contienne un nombre compris entre 1 et 9, chaque nombre étant utilisé une fois et une seule dans chaque section. Les joueurs du jeu Sudoku reçoivent une grille partiellement remplie qu'ils doivent résoudre.

Pour résoudre un sudoku, il n'est pas nécessaire d'avoir des connaissances en mathématiques mais de faire preuve de logique et de raisonnement. Résoudre des grilles de sudoku quotidiennement fait travailler votre cerveau. Elle améliore la concentration et la pensée logique. On peut chercher des grilles de sudoku dans les journaux ou les jouer en ligne sur de nombreux sites Web.

# A propos :
Ce script est un solveur de Sudoku qui résout presque toutes les énigmes de Sudoku avec la méthode récursive. Cette technique consiste à supposer que la valeur d'une case est un certain nombre et à faire de même pour toutes les cases suivantes jusqu'à rencontrer une impossibilité. On recule alors autant que nécessaire en incrémentant les valeurs des cases, et ce jusqu'à remplir la grille. 

Vous avez déjà essayé de résoudre des énigmes de Sudoku dans les journaux, les magazines et en ligne, mais vous êtes resté bloqué. Vous pouvez utiliser ce script pour obtenir sa solution instantanément et aller plus loin.

# Fonctionnement :
Pour faire fonctionner le solveur de sudoku, il suffit d'exécuter le script App.py.
Quand le script est exécuté, un page principale s'affiche. Cette page propose de générer, soit une grille de sudoku aléatoire, soit une grille de sudoku vide pour pouvoir résoudre les grilles papier.

Si le bouton "grille aléatoire" est sélectionné, une grille vide va apparaitre, et il suffira de cliquer sur le bouton nouveau pour générer une grille aléatoire. Ensuite, il suffira de modifier les case "0" par les bonnes valeurs, ou cliquer sur résoudre pour afficher la solution.

Si le bouton "grille vide" est sélectionné, une grille vide va apparaitre. Cette grille pourra être rempli par les numéros d'une grille papier pour pouvoir afficher la solution.

