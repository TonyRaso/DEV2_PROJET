import engine
from piece import Piece

JOUEURS_POSSIBLE = ["yellow", "blue", "red", "green"]

INPUT_VERS_PIECE = {"p": "PION", "f": "FOU", "d": "DAME", "t": "TOUR", "c": "CAVALIER"}

COORD_INTERDIT = ['a15', 'b15', 'c15', 'd15', 'l15', 'm15', 'n15', 'o15',
                  'a14', 'b14', 'c14', 'd14', 'l14', 'm14', 'n14', 'o14',
                  'a13', 'b13', 'c13', 'd13', 'l13', 'm13', 'n13', 'o13',
                  'a12', 'b12', 'c12', 'd12', 'l12', 'm12', 'n12', 'o12',
                  'a04', 'b04', 'c04', 'd04', 'l04', 'm04', 'n04', 'o04',
                  'a03', 'b03', 'c03', 'd03', 'l03', 'm03', 'n03', 'o03',
                  'a02', 'b02', 'c02', 'd02', 'l02', 'm02', 'n02', 'o02',
                  'a01', 'b01', 'c01', 'd01', 'l01', 'm01', 'n01', 'o01',
                  ]
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


class Plateau:
    def __init__(self):
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
        self.is_contre_attaque = False

    def init_plateau(self, joueurs=""):
        if joueurs != "":  # c'est qu'on appelle la fonction avec un argument
            piece_a_retirer = []
            for joueur in JOUEURS_POSSIBLE:
                if joueur not in joueurs:
                    piece_a_retirer.append(joueur)
            for case in self.cases:
                if case.equipe in piece_a_retirer:
                    if case.equipe == "green":
                        self.cases[self.cases.index(case) - 30] = Piece("INTERDIT")
                    elif case.equipe == "blue":
                        self.cases[self.cases.index(case) + 30] = Piece("INTERDIT")
                    elif case.equipe == "red":
                        self.cases[self.cases.index(case) + 2] = Piece("INTERDIT")
                    elif case.equipe == "yellow":
                        self.cases[self.cases.index(case) - 2] = Piece("INTERDIT")
                    # on a retirer les 2 collonnes/rangées devant les équipes qui ne jouent pas

                    self.cases[self.cases.index(case)] = Piece("INTERDIT")  # on retire les pièces qui ne jouent pas

    def afficher_plateau(self):
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

    def deplacement(self, plateau, coup, equipe, contre_attaque=False):
        nom_piece = INPUT_VERS_PIECE[coup[0]]
        depart = coup[1:4]
        arrive = coup[4:7]

        if self.cases[COORD.index(depart)].nom == nom_piece:  # Vérifie que la pièce appellée est la bonne
            if self.cases[COORD.index(arrive)].Is_drapeau:
                # si on arrive sur le flag
                self.cases[COORD.index(arrive)] = Piece(nom_piece, equipe, True)
                self.cases[COORD.index(depart)] = Piece()

            else:
                # coup normal
                if self.cases[COORD.index(depart)].Is_premier_coup :
                    # si on joue la première fois un pion, on indique déjà joué pour la suite
                    self.cases[COORD.index(arrive)] = Piece(nom_piece, equipe, Is_premier_coup=False)
                    self.cases[COORD.index(depart)] = Piece()

                else:
                    self.cases[COORD.index(arrive)] = Piece(nom_piece, equipe)
                    self.cases[COORD.index(depart)] = Piece()

        else:
            print("Coup invalide")

        plateau.afficher_plateau()
