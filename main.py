import board
import piece
import engine


class Game:
    def __init__(self, table):
        self.IsGameON = True
        self.table = table

    def play(self):
        nombre_tour = 0
        self.table.format_board()
        while self.IsGameON:
            move = input("Quel pièce voulez vous déplacer vers quel case ? (Format, pf02f03 = pion en f02 vers f03) : ")
            if engine.verif_format_move(move):
                equipe = self.table.cases[board.COORD.index(move[1:4])].couleur

                if engine.verif_deplacment(move, self.table, equipe):
                    table.moveto(table, move, equipe)
                    nombre_tour += 1

            if nombre_tour == 10:
                self.IsGameON = False


if __name__ == "__main__":
    table = board.Board()
    Game1 = Game(table)
    Game1.play()
