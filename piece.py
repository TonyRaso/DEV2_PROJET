from termcolor import colored



class Piece:

    def __init__(self, nom="", equipe="white", Is_flag = False):
        self.nom = nom
        self.equipe = equipe
        self.Is_flag = Is_flag

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
            res = "X"
        elif self.nom == "INTERDIT":
            res = " "
        return colored(res, self.equipe)

    def nom(self):
        return self.nom
