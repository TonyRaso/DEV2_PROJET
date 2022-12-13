import re
import constante as c


def verif_format_coup(coup):
    """
    Methode qui vérifie si le déplacement encodé est validé ou pas
    :param coup: le déplacement mémorisé via l input main
    :type coup: string
    :return: true ou false pour le format
    :rtype: boolean
    """

    if len(coup) == 0:
        print("Format non valide")
        return False
    regex = re.compile(r"[pfctd][a-o][01]\d[a-o][01]\d")
    if regex.match(coup) is None:
        print("Format non valide")
        return False
    depart = coup[1:4]
    arrive = coup[4:7]
    if (depart in c.COORD) and (arrive in c.COORD):
        return True
    else:
        print("Format non valide")
        return False


def is_case_interdit(plateau, coup):
    """
    Determine si la case est de type interdit lors d'un mouvement
    :param plateau: passe la table de jeu en parametre
    :type plateau: objet de class Plateau
    :param coup: le déplacement mémorisé via l input main
    :type coup: string
    :return: retourne si oui ou non c'est une case interdite
    :rtype: boolean
    """
    arrive = coup[4:7]
    if plateau.cases[c.COORD.index(arrive)].nom == "INTERDIT":
        return False
    return True


def is_place_occupee(plateau, coup, equipe):
    """
    Determine si la case est occupée par une piece de la meme équipe lors d'un mouvement
    :param plateau: passe la table de jeu en parametre
    :type plateau: objet de class Plateau
    :param coup: le déplacement mémorisé via l input main
    :type coup: string
    :param equipe: determine l'equipe a qui appartient la piece
    :type equipe: string
    :return: retourne si oui ou non la case est occupé par une piece alliée
    :rtype: boolean
    """
    arrive = coup[4:7]
    if plateau.cases[c.COORD.index(arrive)].nom != "" and plateau.cases[c.COORD.index(arrive)].equipe == equipe:
        # Vérifie que la case n'est pas occupée
        return False
    return True


def verif_piece_dans_vecteur(plateau, arrive, depart, vecteur):
    """
    Methode qui recoit la table actuele avec la position initiale d'une piece et sa destination
    et qui va verifier si cette piece a le champ libre pour son déplacement vers sa destination ou pas
    :param plateau: passe la table de jeu en parametre
    :type plateau: objet de class Plateau
    :param arrive: la partie de coup qui correspond a son arrivée
    :type arrive: string
    :param depart: la partie de coup qui correspond a son départ
    :type depart: string
    :param vecteur: la liste des déplacement pour le type de piece correspondant
    :type vecteur: Liste de int
    :return: si le champ est libre pour le déplacement ou pas
    :rtype: Boolean
    """

    for n in vecteur:
        if ((c.COORD.index(arrive) - c.COORD.index(depart)) / n) % 1 == 0:  # si une directions est possible
            distance = int((c.COORD.index(arrive) - c.COORD.index(depart)) / n)
            # trouve la distance entre le départ et l'arrivée
            for k in range(1, distance):  # pour chaque case entre le départ et l'arrivée
                if plateau.cases[(c.COORD.index(depart) + k * n)].nom != "":
                    # si une case n'est pas vide, return False
                    return False
            if distance > 0:
                # uniquement si le déplacement est positif, sinon il risque de tombé dans le mauvais vecteur
                return True
    return False


def verif_pion(arrive, case1, case2, liste_deplacement, liste_deplacement_prise, plateau):
    """

    :param arrive: la partie de coup qui correspond a son arrivée
    :type arrive: string
    :param case1:
    :type case1:
    :param case2:
    :type case2:
    :param liste_deplacement:
    :type liste_deplacement:
    :param liste_deplacement_prise:
    :type liste_deplacement_prise:
    :param plateau:
    :type plateau:
    :return:
    :rtype:
    """
    if c.COORD.index(case1) - c.COORD.index(case2) in liste_deplacement and \
            plateau.cases[c.COORD.index(arrive)].equipe == "white":
        return True
    elif plateau.cases[c.COORD.index(arrive)].equipe != "white" and c.COORD.index(
            case1) - c.COORD.index(case2) in liste_deplacement_prise:
        return True
    else:
        return False


def verif_deplacement_horizontal(arrive, depart, plateau):
    """
    Methode qui vérifie si le déplacement horizontal est possible ou pas
    :param arrive: la partie de coup qui correspond a son arrivée
    :type arrive: string
    :param depart: la partie de coup qui correspond a son départ
    :type depart: string
    :param plateau: passe la table de jeu en parametre
    :type plateau: objet de class Plateau
    :return: si le déplacement horizontal est possible ou pas
    :rtype: Boolean
    """
    for k in range(min(c.COORD.index(arrive), c.COORD.index(depart)) + 1,
                   max(c.COORD.index(arrive), c.COORD.index(depart))):
        # parcour le plateau entre les deux cases depart et arrivée
        if plateau.cases[k].nom != "":
            return False
    return True


def verif_deplacement_vecteur_et_horizontal(arrive, depart, plateau, vecteur):
    """
    Methode qui vérifie si le déplacement horizontal et vecteur, est possible grace a la methode verif_deplacement_horizontal
    sinon verifie si une piece est dans le chemin grace a la methode verif_piece_dans_vecteur
    :param arrive: la partie de coup qui correspond a son arrivée
    :type arrive: string
    :param depart: la partie de coup qui correspond a son départ
    :type depart: string
    :param plateau: passe la table de jeu en parametre
    :type plateau: objet de class Plateau
    :param vecteur: la liste des déplacement pour le type de piece correspondant
    :type vecteur: Liste de int
    :return: Retourne le Boolean de la methode verif_déplacement horizontal ou celui de piece_dans_vecteur
    :rtype: Boolean
    """
    if depart[1:4] == arrive[1:4]:  # déplacement horizontal
        return verif_deplacement_horizontal(arrive, depart, plateau)

    return verif_piece_dans_vecteur(plateau, arrive, depart, vecteur)


def verif_deplacement(coup, plateau, equipe):
    """
    Methode qui vérifie l'intégralité des regles de jeu a prendre en compte pour un déplacement
    inclus la méthode  verif_piece_dans_vecteur en ce qui concerne le vecteur libre
    :param coup: le déplacement mémorisé via l input main
    :type coup: string
    :param plateau: passe la table de jeu en parametre
    :type plateau: objet de class Plateau
    :param equipe: determine l'equipe a qui appartient la piece
    :type equipe: string
    :return: true ou false selon que le déplacement est possible ou pas
    :rtype: boolean
    """

    piece = coup[0]
    depart = coup[1:4]
    arrive = coup[4:7]
    multi_premier_coup = 1
    if plateau.cases[c.COORD.index(depart)].Is_premier_coup:
        multi_premier_coup = 2
    if piece == "p":
        if equipe == "green":
            return verif_pion(arrive, depart, arrive, [15 * multi_premier_coup, 15], [14, 16], plateau)

        elif equipe == "blue":
            return verif_pion(arrive, arrive, depart, [15 * multi_premier_coup, 15], [14, 16], plateau)

        elif equipe == "red":
            return verif_pion(arrive, arrive, depart, [1 * multi_premier_coup, 1], [-14, 16], plateau)

        elif equipe == "yellow":
            return verif_pion(arrive, depart, arrive, [1 * multi_premier_coup, 1], [14, -16], plateau)

    elif piece == "c":
        if c.COORD.index(arrive) - c.COORD.index(depart) in c.coup_cavalier:
            return True
        else:
            return False

    elif piece == "f":
        return verif_piece_dans_vecteur(plateau, arrive, depart, c.vecteur_fou)

    elif piece == "t":
        return verif_deplacement_vecteur_et_horizontal(arrive, depart, plateau, c.vecteur_tour)

    elif piece == "d":
        return verif_deplacement_vecteur_et_horizontal(arrive, depart, plateau, c.vecteur_dame)


def is_contre_attaque_sur_flag_possible(plateau, equipe):
    """
    Determine si il y a lieu de réaliser une contre attaque
    :param plateau: passe la table de jeu en parametre
    :type plateau: objet de class Plateau
    :param equipe: determine l'equipe a qui appartient la piece
    :type equipe: string
    :return: est ce que la contre attaque est possible par celui qui vient de le perdre
    :rtype:boolean
    """
    coup_possible = []
    for case in plateau.cases:
        if case.equipe == equipe:
            move = case.nom[0].lower() + c.COORD[plateau.cases.index(case)] + c.CASE_DRAPEAU
            if verif_deplacement(move, plateau, equipe):
                coup_possible.append(move)

    if len(coup_possible) == 0:
        return False
    else:
        return coup_possible


def verif_pion_horizontal_peut_prendre_drapeau(plateau, piece, liste_colonne_possible, liste_ligne_possible):
    """

    :param plateau: passe la table de jeu en parametre
    :type plateau: objet de class Plateau
    :param piece:
    :type piece:
    :param liste_colonne_possible:
    :type liste_colonne_possible:
    :param liste_ligne_possible:
    :type liste_ligne_possible:
    :return:
    :rtype:
    """
    return c.COORD[plateau.cases.index(piece)][0] in liste_colonne_possible and (
            c.COORD[plateau.cases.index(piece)][1:3] in liste_ligne_possible)


def verif_pion_vertical_peut_prendre_drapeau(plateau, piece, liste_colonne_possible, liste_ligne_possible):
    """

    :param plateau: passe la table de jeu en parametre
    :type plateau: objet de class Plateau
    :param piece:
    :type piece:
    :param liste_colonne_possible:
    :type liste_colonne_possible:
    :param liste_ligne_possible:
    :type liste_ligne_possible:
    :return:
    :rtype:
    """
    return (c.COORD[plateau.cases.index(piece)][0] in liste_colonne_possible) \
           and int(c.COORD[plateau.cases.index(piece)][1:3]) in liste_ligne_possible


def is_drapeau_prenable(plateau):
    """
    Determine si le drapeau est prenable par n'importe quel piece (pour les regles de fin)
    :param plateau: passe la table de jeu en parametre
    :type plateau: objet de class Plateau
    :return:si quelqu'un a encore la possibilité de prendre le drapeau
    :rtype: boolean
    """
    equipe_drapeau = plateau.cases[c.COORD.index("h08")].equipe
    for piece in plateau.cases:
        if piece.equipe != equipe_drapeau:
            # on regarde les pièces restantes ennemies
            if piece.nom == "DAME" or piece.nom == "TOUR" or piece.nom == "CAVALIER" or piece.nom == "FOU":
                return True

            # pour les pions, regarder où ils sont
            elif piece.equipe == "green":
                if verif_pion_vertical_peut_prendre_drapeau(plateau, piece, ["g", "i"], range(1, 8)):
                    return True
            elif piece.equipe == "blue":
                if verif_pion_vertical_peut_prendre_drapeau(plateau, piece, ["g", "i"], range(1, 10)):
                    # dans la bonne colonne et pas au-dessus du drapeau
                    return True
            elif piece.equipe == "red":
                if verif_pion_horizontal_peut_prendre_drapeau(plateau, piece, ["b", "c", "d", "e", "f", "g"],
                                                              ["07", "09"]):
                    # dans la bonne colonne et pas au-dessus du drapeau
                    return True
            elif piece.equipe == "yellow":
                if verif_pion_horizontal_peut_prendre_drapeau(plateau, piece, ["i", "j", "k", "l", "m", "n"],
                                                              ["07", "09"]):
                    # dans la bonne colonne et pas au-dessus du drapeau
                    return True

    return False
