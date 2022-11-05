from termcolor import colored

LIST_PIECE = ["p"]


class Piece:

    def __init__(self, nom="", couleur="white"):
        self.nom = nom
        self.couleur = couleur

    def __str__(self):
        res = f"."
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
            res = "."
        elif self.nom == "INTERDIT":
            res = " "
        return colored(res, self.couleur)

    def nom(self):
        return self.nom
