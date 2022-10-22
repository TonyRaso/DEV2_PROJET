from board import *
from piece import *

LIST_PIECE = ["p"]


def verif_format_move(move):
    piece = move[0]
    depart = move[1:4]
    arrive = move[4:7]
    if (piece in LIST_PIECE) and (depart in COORD) and (arrive in COORD):
        return True
    else:
        print("Format non valide")
        return False
