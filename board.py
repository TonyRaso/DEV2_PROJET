from piece import Piece


class Board:
    def __init__(self):
        self.cases = [
            Piece('PION'), Piece('PION'), Piece('PION'), Piece('PION'), Piece('PION'), Piece('PION'), Piece('PION'),
            Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(),
            Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(),
            Piece(), Piece(), Piece(), Piece("FLAG"), Piece(), Piece(), Piece(),
            Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(),
            Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(),
            Piece('PION'), Piece('PION'), Piece('PION'), Piece('PION'), Piece('PION'), Piece('PION'), Piece('PION'),
        ]

        self.coord = [
            'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7',
            'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6',
            'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5',
            'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4',
            'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3',
            'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2',
            'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1',
        ]

    def format_board(self):
        i = 0
        toscreen = ""
        for j in self.cases:
            if (str(j) == "PION"):
                toscreen += "|" + " " * 4 + str(j) + " " * 4 + "|"
            else:
                toscreen += "| " + str(j) + " |"
            if i % 7 == 6:
                print(''.join('{0:^32s}').format(toscreen))
                print('\t')
                toscreen = ""
            i += 1

    def moveto(self, depart, arrive):
        print(self.cases[self.coord.index(depart)].nom)

        if str(self.cases[self.coord.index(depart)]) == "PION": #Un pion peu bouger
            self.cases[self.coord.index(arrive)] = Piece("Pion")
            self.cases[self.coord.index(depart)] = Piece()



table = Board()

table.format_board()

depart = input("move depuis:")
sortie = input("move to :")

table.moveto(depart, sortie)
table.format_board()