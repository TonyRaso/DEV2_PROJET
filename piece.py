LIST_PIECE = ["p"]


class Piece:
    def __init__(self, nom=""):
        self._nom = nom

    def __str__(self):
        res = f" "
        if self._nom == "PION":
            res = "X"
        elif self._nom == "FLAG":
            res = "O"
        elif self._nom == "INTERDIT":
            res = "_"
        return res

    def nom(self):
        return self._nom
