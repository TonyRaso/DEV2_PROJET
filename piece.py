from termcolor import colored


class Piece:

    def __init__(self, nom="", equipe="white", Is_drapeau = False, Is_premier_coup = True):
        self.nom = nom
        self.equipe = equipe
        self.Is_drapeau = Is_drapeau
        self.Is_premier_coup = Is_premier_coup

    def __str__(self):
        res = "."
        if self.nom == "PION":
            res = "P"
        elif self.nom == "CAVALIER":
            res = "C"
        elif self.nom == "FOU":
            res = "F"
        elif self.nom == "TOUR":
            res = "T"
        elif self.nom == "DAME":
            res = "D"
        elif self.nom == "FLAG":
            res = "X"
        elif self.nom == "INTERDIT":
            res = " "
        return res
