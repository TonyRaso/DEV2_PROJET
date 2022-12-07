

class Piece:

    def __init__(self, nom="", equipe="white", is_drapeau=False, is_premier_coup=True):
        """
        methode qui sert a initialiser une piece avec son nom complet et sa couleur de joueur(c'est à dire son equipe)
        :param nom: le nome de la piece (PION,FOU,TOUR,DAME,CAVALIER)
        :type nom: string
        :param equipe: la couleur du joueur a qui on initialise la piece
        :type equipe: string
        :param is_drapeau: boolean qui decrit une piece est sur un drapeau
        :type is_drapeau: boolean
        :param is_premier_coup: determine si c est le premier coup de la piece (pour les pions)
        :type is_premier_coup: boolean
        """

        self.nom = nom
        self.equipe = equipe
        self.Is_drapeau = is_drapeau
        self.Is_premier_coup = is_premier_coup

    def __str__(self):
        """
        Methode qui sert a récuperer le type de la piece
        :return: le nom abrégé
        :rtype: string
        """
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
