from termcolor import colored

LIST_PIECE = ["p"]


class Piece:


    def __init__(self, nom="", couleur="white"):
        """
        methode qui sert a initialiser une piece avec son nom complet et sa couleur de joueur
        :param nom:le nome de la piece (PION,FOU,TOUR,DAME,CAVALIER)
        :type nom:string
        :param couleur: la couleur du joueur a qui on initialise la piece
        :type couleur:string
        """
        self.nom = nom
        self.couleur = couleur

    def __str__(self):
        """
        Methode qui sert a récuperer le type et la couleur de la piece
        :return: le nom abrégé et sa couleur
        :rtype: string
        """
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

