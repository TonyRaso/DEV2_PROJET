from board import *
from piece import *

LIST_PIECE = ["p", "c", "f", "t", "d"]

vecteur_tour = [-15, 15]
vecteur_fou = [16, -16, 14, -14]
vecteur_dame = [-15, 15, -16, 16, -14, 14]
coup_cavalier = [29, 31, 13, 17, -17, -13, -31, -29]


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


def verif_piece_dans_vecteur(table, arrive, depart, vecteur):
    for n in vecteur:
        if ((COORD.index(arrive) - COORD.index(depart)) / n) % 1 == 0:  # si une directions est possible
            distance = int((COORD.index(arrive) - COORD.index(depart)) / n)
            # trouve la distance entre le départ et l'arrivée
            for k in range(1, distance):  # pour chaque case entre le départ et l'arrivée
                if table.cases[(COORD.index(depart) + k * n)].nom != "":
                    # si une case n'est pas vide, return False
                    print("une pièce bloque le passage !")
                    return False
            if distance > 0:  # uniquement si le déplacement est positif, sinon il risque de tombé dans le mauvais vecteur
                return True
    print("coup invalide")
    return False


def verif_deplacment(move, table, equipe):
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
        return verif_piece_dans_vecteur(table, arrive, depart, vecteur_fou)  # deplacement diagonale

    elif piece == "t":
        if depart[1:4] == arrive[1:4]:  # déplacement horizontal
            for k in range(min(COORD.index(arrive), COORD.index(depart)) + 1,
                           max(COORD.index(arrive), COORD.index(depart))):
                # parcour le plateau entre les deux cases depart et arrivée
                if table.cases[k].nom != "":
                    print("une pièce bloque le passage !")
                    return False
            return True

        return verif_piece_dans_vecteur(table, arrive, depart, vecteur_tour)  # deplacement vetrical

    elif piece == "d":
        if depart[1:4] == arrive[1:4]:  # déplacement horizontal
            distance = int(COORD.index(arrive) - COORD.index(depart))
            for k in range(min(COORD.index(arrive), COORD.index(depart)) + 1,
                           max(COORD.index(arrive), COORD.index(depart))):
                # parcour le plateau entre les deux cases depart et arrivée
                if table.cases[k].nom != "":
                    print("une pièce bloque le passage !")
                    return False
            return True

        return verif_piece_dans_vecteur(table, arrive, depart, vecteur_dame)  # deplacement vetrical + diagonale
