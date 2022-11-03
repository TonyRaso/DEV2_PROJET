import board
import piece
import engine


class Game:
    def __init__(self, table):
        self.IsGameON = True
        self.table = table

    def play(self):
        nombre_tour = 0

        while self.IsGameON:
            move = input("Quel pièce voulez vous déplacer vers quel case ? (Format, pf01f04 = pion en f02 vers f03) : ")
            if engine.verif_format_move(move) and engine.verif_deplacment(move, table):
                table.moveto(table, move)
                nombre_tour += 1

            if nombre_tour == 3:
                self.IsGameON = False


if __name__ == "__main__":
    table = board.Board()
    Game1 = Game(table)
    Game1.play()
