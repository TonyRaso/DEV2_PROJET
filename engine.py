from board import *
from piece import *

LIST_PIECE = ["p", "c", "f", "t", "d"]


def verif_format_move(move):
    piece = move[0]
    depart = move[1:4]
    arrive = move[4:7]
    if (piece in LIST_PIECE) and (depart in COORD) and (arrive in COORD):
        return True
    else:
        print("Format non valide")
        return False


def verif_deplacment(move, equipe):
    piece = move[0]
    depart = move[1:4]
    arrive = move[4:7]
    if piece == "p" and equipe == "green":
        if COORD.index(depart) - COORD.index(arrive) == 15:
            return True

    elif piece == "p" and equipe == "blue":
        if COORD.index(arrive) - COORD.index(depart) == 15:
            return True
    elif piece == "p" and equipe == "red":
        if COORD.index(arrive) - COORD.index(depart) == 1:
            return True
    elif piece == "p" and equipe == "yellow":
        if COORD.index(depart) - COORD.index(arrive) == 1:
            return True
