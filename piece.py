class Piece:
    def __init__(self, nom=""):
        self._nom = nom

    def __str__(self):
        res = f"{self._nom}"
        if self._nom == "":
            res = "Case Libre"
        return res

    def nom(self):
        return self._nom
