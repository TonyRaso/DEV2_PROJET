from piece import Piece
import constante as c


class Plateau:
    def __init__(self):
        """
        Comprend la position initiale des pieces de chaque joueur ainsi que les cases interdites
        :param /
        :return /
        """
        self.cases = [
            Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),
            Piece('TOUR', "blue"), Piece('CAVALIER', "blue"), Piece('FOU', "blue"), Piece('DAME', "blue"),
            Piece('FOU', "blue"), Piece('CAVALIER', "blue"), Piece('TOUR', "blue"),
            Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),  # ligne 15

            Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),
            Piece('PION', "blue"), Piece('PION', "blue"), Piece('PION', "blue"), Piece('PION', "blue"),
            Piece('PION', "blue"), Piece('PION', "blue"), Piece('PION', "blue"),
            Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),  # ligne 14

            Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),
            Piece(''), Piece(''), Piece(''), Piece(''), Piece(''), Piece(''), Piece(''),
            Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),  # ligne 13

            Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),
            Piece(''), Piece(''), Piece(''), Piece(''), Piece(''), Piece(''), Piece(''),
            Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),  # ligne 12

            Piece('TOUR', "red"), Piece('PION', "red"),
            Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(),
            Piece('PION', "yellow"), Piece('TOUR', "yellow"),  # ligne 11

            Piece('CAVALIER', "red"), Piece('PION', "red"),
            Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(),
            Piece('PION', "yellow"), Piece('CAVALIER', "yellow"),  # ligne 10

            Piece('FOU', "red"), Piece('PION', "red"),
            Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(),
            Piece(),
            Piece('PION', "yellow"), Piece('FOU', "yellow"),  # ligne 09

            Piece('DAME', "red"), Piece('PION', "red"),
            Piece(), Piece(), Piece(), Piece(), Piece(), Piece("FLAG", "white", True),
            Piece(), Piece(), Piece(),
            Piece(), Piece(),
            Piece('PION', "yellow"), Piece('DAME', "yellow"),  # ligne 08

            Piece('FOU', "red"), Piece('PION', "red"),
            Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(),
            Piece(), Piece(),
            Piece(),
            Piece('PION', "yellow"), Piece('FOU', "yellow"),  # ligne 07

            Piece('CAVALIER', "red"), Piece('PION', "red"),
            Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(),
            Piece(),
            Piece('PION', "yellow"), Piece('CAVALIER', "yellow"),  # ligne 06

            Piece('TOUR', "red"), Piece('PION', "red"),
            Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(),
            Piece('PION', "yellow"), Piece('TOUR', "yellow"),  # ligne 05

            Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),
            Piece(''), Piece(''), Piece(''), Piece(''), Piece(''), Piece(''), Piece(''),
            Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),  # ligne 04

            Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),
            Piece(''), Piece(''), Piece(''), Piece(''), Piece(''), Piece(''), Piece(''),
            Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),  # ligne 03

            Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),
            Piece('PION', "green"), Piece('PION', "green"), Piece('PION', "green"), Piece('PION', "green"),
            Piece('PION', "green"), Piece('PION', "green"), Piece('PION', "green"),
            Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),  # ligne 02

            Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),
            Piece('TOUR', "green"), Piece('CAVALIER', "green"), Piece('FOU', "green"), Piece('DAME', "green"),
            Piece('FOU', "green"), Piece('CAVALIER', "green"), Piece('TOUR', "green"),
            Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),  # ligne 01
        ]

    def init_plateau(self, joueurs=""):
        """
        Adapte le plateau au nombre de joueur
        :param joueurs: liste de string représentant les joueurs
        :type joueurs: liste de string
        :return: /
        :rtype: /
        """
        if joueurs != "":  # c'est qu'on appelle la fonction avec un argument
            equipe_a_retirer = []
            for joueur in c.JOUEURS_POSSIBLE:
                if joueur not in joueurs:
                    equipe_a_retirer.append(joueur)
            for case in self.cases:
                if case.equipe in equipe_a_retirer:
                    if case.equipe == "green":
                        self.cases[self.cases.index(case) - 30] = Piece("INTERDIT")
                    elif case.equipe == "blue":
                        self.cases[self.cases.index(case) + 30] = Piece("INTERDIT")
                    elif case.equipe == "red":
                        self.cases[self.cases.index(case) + 2] = Piece("INTERDIT")
                    elif case.equipe == "yellow":
                        self.cases[self.cases.index(case) - 2] = Piece("INTERDIT")
                    # on a retirer les 2 collonnes/lignes devant les équipes qui ne jouent pas

                    self.cases[self.cases.index(case)] = Piece("INTERDIT")  # on retire les pièces qui ne jouent pas

    def afficher_plateau(self):
        """
        Methode qui permet la representation en console de l'échiquier
        :return:/
        :rtype:/
        """
        print("_" * 46 + "\t")
        i = 0
        affiche = ""
        compteur_linge = 15
        for j in self.cases:
            affiche += " " + str(j) + " "
            if i % 15 == 14:
                print(affiche, compteur_linge, end=' \n')
                compteur_linge -= 1
                affiche = ""
            i += 1
        print(" A  B  C  D  E  F  G  H  I  J  K  L  M  N  O")

    def deplacement(self, plateau, coup, equipe):
        """
        Methode qui éffectue le déplacement de la piece lors du tours (apres les differentes verification de engine)
        et qui vérifie les cas de mouvements impossible
        :param plateau: la table dans l état actuelle
        :type plateau: un objet de type Plateau
        :param coup: déplacement encodé par l'utilisateur
        :type coup: string
        :param equipe: la couleur du joueur qui effectue le coup
        :type equipe: string
        :return: /
        :rtype: /
        """

        nom_piece = c.INPUT_VERS_PIECE[coup[0]]
        depart = coup[1:4]
        arrive = coup[4:7]

        if self.cases[c.COORD.index(depart)].nom == nom_piece:  # Vérifie que la pièce appellée est la bonne
            if self.cases[c.COORD.index(arrive)].Is_drapeau:
                # si on arrive sur le flag
                self.cases[c.COORD.index(arrive)] = Piece(nom_piece, equipe, True)
                self.cases[c.COORD.index(depart)] = Piece()

            else:
                # coup normal
                if self.cases[c.COORD.index(depart)].Is_premier_coup:
                    # si on joue la première fois un pion, on indique déjà joué pour la suite
                    self.cases[c.COORD.index(arrive)] = Piece(nom_piece, equipe, is_premier_coup=False)
                    self.cases[c.COORD.index(depart)] = Piece()

                else:
                    self.cases[c.COORD.index(arrive)] = Piece(nom_piece, equipe)
                    self.cases[c.COORD.index(depart)] = Piece()

        plateau.afficher_plateau()
