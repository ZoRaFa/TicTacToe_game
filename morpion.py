"""

Cration du jeu du morpion

"""

# Importation des modules
import os
import time
import random


# Définition des fonctions
def affichage_plateau(plateau):
    """
    Affiche le plateau de jeu
    """
    print("\n")
    print("   1   2   3")
    print("A  " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
    print("   ----------")
    print("B  " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
    print("   ----------")
    print("C  " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])
    print("\n")


def initialisation_plateau(plateau):
    """
    Initialise le plateau de jeu
    """
    for i in range(9):
        plateau[i] = " "


def saisie_joueur(plateau, joueur):
    """
    Demande au joueur de saisir un emplacement
    """
    while True:
        emplacement = input("\n" + joueur + ", choisissez un emplacement (1-9): ")
        if emplacement in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            emplacement = int(emplacement) - 1
            if plateau[emplacement] == " ":
                return emplacement
            else:
                print("\n" + "Cet emplacement est déjà pris, veuillez en choisir un autre.")
        else:
            print("\n" + "Veuillez saisir un chiffre entre 1 et 9.")


def mise_a_jour_plateau(plateau, emplacement, joueur):
    """
    Met à jour le plateau de jeu
    """
    plateau[emplacement] = joueur


def test_victoire(plateau, joueur):
    """
    Teste si le joueur a gagné
    """
    if (plateau[0] == joueur and plateau[1] == joueur and plateau[2] == joueur) or \
       (plateau[3] == joueur and plateau[4] == joueur and plateau[5] == joueur) or \
       (plateau[6] == joueur and plateau[7] == joueur and plateau[8] == joueur) or \
       (plateau[0] == joueur and plateau[3] == joueur and plateau[6] == joueur) or \
       (plateau[1] == joueur and plateau[4] == joueur and plateau[7] == joueur) or \
       (plateau[2] == joueur and plateau[5] == joueur and plateau[8] == joueur) or \
       (plateau[0] == joueur and plateau[4] == joueur and plateau[8] == joueur) or \
       (plateau[2] == joueur and plateau[4] == joueur and plateau[6] == joueur):
        return True
    else:
        return False




# Programme principal


# Définition des variables
plateau = [" "] * 9
joueur = "X"
joueur_actif = True


# Initialisation du plateau
initialisation_plateau(plateau)


# Affichage du plateau
affichage_plateau(plateau)


# Boucle de jeu
while True:
    # Test victoire
    if test_victoire(plateau, joueur):
        print("\n" + joueur + " a gagné!")
        break

    # Test égalité
    if " " not in plateau:
        print("\n" + "Égalité!")
        break

    # Tour du joueur
    if joueur_actif:
        emplacement = saisie_joueur(plateau, joueur)
        mise_a_jour_plateau(plateau, emplacement, joueur)
        affichage_plateau(plateau)
        joueur_actif = False
    else:
        emplacement = saisie_joueur(plateau, "O")
        mise_a_jour_plateau(plateau, emplacement, "O")
        affichage_plateau(plateau)
        joueur_actif = True

    # Changement de joueur
    if joueur == "X":
        joueur = "O"
    else:
        joueur = "X"


# Fin du jeu