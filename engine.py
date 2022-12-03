from board import *
from piece import *

LIST_PIECE = ["p", "c", "f", "t", "d"]

vecteur_tour = [-15, 15]
vecteur_fou = [16, -16, 14, -14]
vecteur_dame = [-15, 15, -16, 16, -14, 14]
coup_cavalier = [29, 31, 13, 17, -17, -13, -31, -29]


def verif_format_move(move):
    """
    Methode qui vérifie si le déplacement encodé est valide ou pas
    :param move: le déplacement mémorisé via l input main
    :type move: string
    :return: true ou false
    :rtype: Boolean
    """
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
    """
    Methode qui recoit la table actuele avec la position initiale d'une piece et sa destination
    et qui va verifier si cette piece a le champ libre pour son déplacement vers sa destination ou pas
    :param table: passe la table de jeu en parametre
    :type table: objet de class Board
    :param arrive:la partie de move qui correspond a son arrivée
    :type arrive: string
    :param depart: la partie de move qui correspond a son départ
    :type depart: string
    :param vecteur:la liste des déplacement pour le type de piece correspondant
    :type vecteur:Liste
    :return: si le champ est libre pour le déplacement ou pas
    :rtype: Bollean
    """
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
    """
    Methode qui vérifie l'intégralité des parametres a prendre en compte pour un déplacement 
    inclus la méthode  verif_piece_dans_vecteur en ce qui concerne le vecteur libre 
    :param move: le déplacement mémorisé via l input main
    :type move: string
    :param table: passe la table de jeu en parametre
    :type table: objet de class Board
    :param equipe: indique l'équipe qui joue le coup a vérifier
    :type equipe: strin 
    :return: un print de la raison pour la quel le coup serait impossible,vrai si le déplacement est possible false dans le cas contraire
    :rtype: string,boolean
    """""
    piece = move[0]
    depart = move[1:4]
    arrive = move[4:7]
    if piece == "p":
        if equipe == "green":
    if COORD.index(depart) - COORD.index(arrive) == 15:
        return True
    elif table.cases[COORD.index(arrive)].equipe != "white" and COORD.index(depart) - COORD.index(arrive) in [
        14, 16]:
        return True
    else:
        print("coup impossible")
        return False
    elif equipe == "blue":
    if COORD.index(arrive) - COORD.index(depart) == 15:
        return True
    elif table.cases[COORD.index(arrive)].equipe != "white" and COORD.index(arrive) - COORD.index(depart) in [
        14, 16]:
        return True
    else:
        print("coup impossible")
        return False

elif equipe == "red":
if COORD.index(arrive) - COORD.index(depart) == 1:
    return True
elif table.cases[COORD.index(arrive)].equipe != "white" and COORD.index(arrive) - COORD.index(depart) in [
    -14, 16]:
    return True
else:
    print("coup impossible")
    return False
elif equipe == "yellow":
if COORD.index(depart) - COORD.index(arrive) == 1:
    return True
elif table.cases[COORD.index(arrive)].equipe != "white" and COORD.index(depart) - COORD.index(arrive) in [
    16, -14]:
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
