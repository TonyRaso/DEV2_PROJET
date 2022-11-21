from piece import *

COORD = [
    'a15', 'b15', 'c15', 'd15', 'e15', 'f15', 'g15', 'h15', 'i15', 'j15', 'k15', 'l15', 'm15', 'n15', 'o15',
    'a14', 'b14', 'c14', 'd14', 'e14', 'f14', 'g14', 'h14', 'i14', 'j14', 'k14', 'l14', 'm14', 'n14', 'o14',
    'a13', 'b13', 'c13', 'd13', 'e13', 'f13', 'g13', 'h13', 'i13', 'j13', 'k13', 'l13', 'm13', 'n13', 'o13',
    'a12', 'b12', 'c12', 'd12', 'e12', 'f12', 'g12', 'h12', 'i12', 'j12', 'k12', 'l12', 'm12', 'n12', 'o12',
    'a11', 'b11', 'c11', 'd11', 'e11', 'f11', 'g11', 'h11', 'i11', 'j11', 'k11', 'l11', 'm11', 'n11', 'o11',
    'a10', 'b10', 'c10', 'd10', 'e10', 'f10', 'g10', 'h10', 'i10', 'j10', 'k10', 'l10', 'm10', 'n10', 'o10',
    'a09', 'b09', 'c09', 'd09', 'e09', 'f09', 'g09', 'h09', 'i09', 'j09', 'k09', 'l09', 'm09', 'n09', 'o09',
    'a08', 'b08', 'c08', 'd08', 'e08', 'f08', 'g08', 'h08', 'i08', 'j08', 'k08', 'l08', 'm08', 'n08', 'o08',
    'a07', 'b07', 'c07', 'd07', 'e07', 'f07', 'g07', 'h07', 'i07', 'j07', 'k07', 'l07', 'm07', 'n07', 'o07',
    'a06', 'b06', 'c06', 'd06', 'e06', 'f06', 'g06', 'h06', 'i06', 'j06', 'k06', 'l06', 'm06', 'n06', 'o06',
    'a05', 'b05', 'c05', 'd05', 'e05', 'f05', 'g05', 'h05', 'i05', 'j05', 'k05', 'l05', 'm05', 'n05', 'o05',
    'a04', 'b04', 'c04', 'd04', 'e04', 'f04', 'g04', 'h04', 'i04', 'j04', 'k04', 'l04', 'm04', 'n04', 'o04',
    'a03', 'b03', 'c03', 'd03', 'e03', 'f03', 'g03', 'h03', 'i03', 'j03', 'k03', 'l03', 'm03', 'n03', 'o03',
    'a02', 'b02', 'c02', 'd02', 'e02', 'f02', 'g02', 'h02', 'i02', 'j02', 'k02', 'l02', 'm02', 'n02', 'o02',
    'a01', 'b01', 'c01', 'd01', 'e01', 'f01', 'g01', 'h01', 'i01', 'j01', 'k01', 'l01', 'm01', 'n01', 'o01',
]
LIST_PIECE = ["p", "c", "f", "t", "d"]

vecteur_tour = [-15, 15]
vecteur_fou = [16, -16, 14, -14]
vecteur_dame = [-15, 15, -16, 16, -14, 14]
coup_cavalier = [29, 31, 13, 17, -17, -13, -31, -29]


def verif_format_coup(coup):
    if len(coup) == 0:
        print("Format non valide")
        return False
    piece = coup[0]
    depart = coup[1:4]
    arrive = coup[4:7]
    if (piece in LIST_PIECE) and (depart in COORD) and (arrive in COORD):
        return True
    else:
        print("Format non valide")
        return False


def is_case_interdit(plateau, move):
    arrive = move[4:7]
    if plateau.cases[COORD.index(arrive)].nom == "INTERDIT":
        print("Case d'arrivée interdite !")
        return False
    return True


def is_place_occupee(plateau, move, equipe):
    arrive = move[4:7]
    if plateau.cases[COORD.index(arrive)].nom != "" and plateau.cases[COORD.index(arrive)].equipe == equipe:
        # Vérifie que la case n'est pas occupée
        print("case occupée par une pièce alliée")
        return False
    return True


def verif_piece_dans_vecteur(plateau, arrive, depart, vecteur, print_enable=True):
    for n in vecteur:
        if ((COORD.index(arrive) - COORD.index(depart)) / n) % 1 == 0:  # si une directions est possible
            distance = int((COORD.index(arrive) - COORD.index(depart)) / n)
            # trouve la distance entre le départ et l'arrivée
            for k in range(1, distance):  # pour chaque case entre le départ et l'arrivée
                if plateau.cases[(COORD.index(depart) + k * n)].nom != "":
                    # si une case n'est pas vide, return False
                    if print_enable:
                        print("une pièce bloque le passage !")
                    return False
            if distance > 0:
                # uniquement si le déplacement est positif, sinon il risque de tombé dans le mauvais vecteur
                return True
    if print_enable:
        print("coup invalide")
    return False


def verif_deplacment(move, plateau, equipe, print_enable=True):
    piece = move[0]
    depart = move[1:4]
    arrive = move[4:7]
    if piece == "p":
        if equipe == "green":
            if COORD.index(depart) - COORD.index(arrive) == 15 and plateau.cases[COORD.index(arrive)].equipe == "white":
                return True
            elif plateau.cases[COORD.index(arrive)].equipe != "white" and COORD.index(depart) - COORD.index(arrive) in [
                14, 16]:
                return True
            else:
                if print_enable:
                    print("coup impossible")
                return False
        elif equipe == "blue":
            if COORD.index(arrive) - COORD.index(depart) == 15 and plateau.cases[COORD.index(arrive)].equipe == "white":
                return True
            elif plateau.cases[COORD.index(arrive)].equipe != "white" and COORD.index(arrive) - COORD.index(depart) in [
                14, 16]:
                return True
            else:
                if print_enable:
                    print("coup impossible")
                return False
        elif equipe == "red":
            if COORD.index(arrive) - COORD.index(depart) == 1 and plateau.cases[COORD.index(arrive)].equipe == "white":
                return True
            elif plateau.cases[COORD.index(arrive)].equipe != "white" and COORD.index(arrive) - COORD.index(depart) in [
                -14, 16]:
                return True
            else:
                if print_enable:
                    print("coup impossible")
                return False
        elif equipe == "yellow":
            if COORD.index(depart) - COORD.index(arrive) == 1 and plateau.cases[COORD.index(arrive)].equipe == "white":
                return True
            elif plateau.cases[COORD.index(arrive)].equipe != "white" and COORD.index(depart) - COORD.index(arrive) in [
                16, -14]:
                return True
            else:
                if print_enable:
                    print("coup impossible")
                return False

    elif piece == "c":
        if COORD.index(arrive) - COORD.index(depart) in coup_cavalier:
            return True
        else:
            if print_enable:
                print("coup impossible")
            return False

    elif piece == "f":
        return verif_piece_dans_vecteur(plateau, arrive, depart, vecteur_fou, print_enable)  # deplacement diagonale

    elif piece == "t":
        if depart[1:4] == arrive[1:4]:  # déplacement horizontal
            for k in range(min(COORD.index(arrive), COORD.index(depart)) + 1,
                           max(COORD.index(arrive), COORD.index(depart))):
                # parcour le plateau entre les deux cases depart et arrivée
                if plateau.cases[k].nom != "":
                    if print_enable:
                        print("une pièce bloque le passage !")
                    return False
            return True

        return verif_piece_dans_vecteur(plateau, arrive, depart, vecteur_tour, print_enable)  # deplacement vetrical

    elif piece == "d":
        if depart[1:4] == arrive[1:4]:  # déplacement horizontal
            distance = int(COORD.index(arrive) - COORD.index(depart))
            for k in range(min(COORD.index(arrive), COORD.index(depart)) + 1,
                           max(COORD.index(arrive), COORD.index(depart))):
                # parcour le plateau entre les deux cases depart et arrivée
                if plateau.cases[k].nom != "":
                    if print_enable:
                        print("une pièce bloque le passage !")
                    return False
            return True

        return verif_piece_dans_vecteur(plateau, arrive, depart, vecteur_dame,
                                        print_enable)  # deplacement vetrical + diagonale


def Is_contre_attaque_sur_flag_possible(plateau, equipe):
    coup_possible = []
    case_flag = "h08"
    for case in plateau.cases:
        if case.equipe == equipe:
            move = case.nom[0].lower() + COORD[plateau.cases.index(case)] + case_flag
            if verif_deplacment(move, plateau, equipe, False):
                coup_possible.append(move)

    if len(coup_possible) == 0:
        print("pas de contre-attaque possible")
        return False
    else:
        print("les coups possible sont:")
        for coup in coup_possible:
            print(coup)
        return coup_possible


def Is_drapeau_prenable(plateau):
    equipe_drapeau = plateau.cases[COORD.index("h08")].equipe
    for piece in plateau.cases:
        if piece.equipe != equipe_drapeau:
            # on regarde les pièces restantes ennemies
            if piece == "DAME" or piece == "TOUR" or piece == "CAVALIER" or piece.nom == "FOU":
                # si il y a une dame ou tour ou cavalier, on joue
                # si un fou se trouve sur les case %2==0, donc dans l'alignement du drapeau mais tt les fous le sont
                return True

            # pour les pions, regarder où ils sont
            elif piece.equipe == "green":
                if (COORD[plateau.cases.index(piece)][0] == "g" or COORD[plateau.cases.index(piece)][0] == "i") \
                        and COORD[plateau.cases.index(piece)][1:3] <= "07":
                    # dans la bonne colonne et pas au-dessus du drapeau
                    return True
            elif piece.equipe == "blue":
                if (COORD[plateau.cases.index(piece)][0] == "g" or COORD[plateau.cases.index(piece)][0] == "i") \
                        and COORD[plateau.cases.index(piece)][1:3] >= "09":
                    # dans la bonne colonne et pas au-dessus du drapeau
                    return True
            elif piece.equipe == "red":
                if COORD[plateau.cases.index(piece)][0] in ["b", "c", "d", "e", "f", "g"] and (
                        COORD[plateau.cases.index(piece)][1:3] == "07" or COORD[plateau.cases.index(piece)][
                                                                          1:3] == "09"):
                    # dans la bonne colonne et pas au-dessus du drapeau
                    return True
            elif piece.equipe == "yellow":
                if COORD[plateau.cases.index(piece)][0] in ["i", "j", "k", "l", "m", "n"] and (
                        COORD[plateau.cases.index(piece)][1:3] == "07" or COORD[plateau.cases.index(piece)][
                                                                          1:3] == "09"):
                    # dans la bonne colonne et pas au-dessus du drapeau
                    return True

    return False
