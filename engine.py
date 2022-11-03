from board import *
from piece import *

LIST_PIECE = ["p", "c", "f", "t", "d"]

coup_cavalier = [29, 31, 13, 17, -17, -13, -31, -29]
coup_tour = []
coup_fou = []
coup_dame = []
for i in range(1, 16):
    coup_tour.append(15 * i)
    coup_tour.append(i)
    coup_tour.append(-15 * i)
    coup_tour.append(-i)
    coup_fou.append(i * 16)
    coup_fou.append(i * 14)
    coup_fou.append(i * -14)
    coup_fou.append(i * -16)
    coup_dame.append(i * 16)
    coup_dame.append(i * 14)
    coup_dame.append(i * -14)
    coup_dame.append(i * -16)
    coup_dame.append(15 * i)
    coup_dame.append(i)
    coup_dame.append(-15 * i)
    coup_dame.append(-i)


def verif_format_move(move):
    if len(move) == 0:
        print("Format non valide")
        return False
    piece = move[0]
    depart = move[1:4]
    arrive = move[4:7]
    if (piece in LIST_PIECE) and (depart in COORD) and (arrive in COORD):
        return True
    else:
        print("Format non valide")
        return False


def verif_deplacment(move, table, equipe="green"):
    piece = move[0]
    depart = move[1:4]
    arrive = move[4:7]
    if piece == "p":
        if equipe == "green":
            if COORD.index(depart) - COORD.index(arrive) == 15:
                return True
            else:
                print("coup impossible")
                return False
        elif equipe == "blue":
            if COORD.index(arrive) - COORD.index(depart) == 15:
                return True
            else:
                print("coup impossible")
                return False
        elif equipe == "red":
            if COORD.index(arrive) - COORD.index(depart) == 1:
                return True
            else:
                print("coup impossible")
                return False
        elif equipe == "yellow":
            if COORD.index(depart) - COORD.index(arrive) == 1:
                return True
            else:
                print("coup impossible")
                return False

    elif piece == "c":
        if COORD.index(arrive) - COORD.index(depart) in coup_cavalier:
            return True
        else:
            print("coup impossible")
            return False

    elif piece == "f":
        if COORD.index(arrive) - COORD.index(depart) in coup_fou:
            return True
        else:
            print("coup impossible")
            return False

    elif piece == "t":

        if COORD.index(arrive) - COORD.index(depart) in coup_tour:
            return True
        else:
            print("coup impossible")
            return False

    elif piece == "d":
        if COORD.index(arrive) - COORD.index(depart) in coup_dame:
            return True
        else:
            print("coup impossible")
            return False
