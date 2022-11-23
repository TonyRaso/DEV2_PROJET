import board
import engine


class Jeu:
    def __init__(self, table):
        self.est_en_jeu = True
        self.table = table

    def jouer(self):
        self.table.afficher_plateau()
        while self.est_en_jeu:
            coup = input("Quel pièce voulez vous déplacer vers quel case ? (Format, pf02f03 = pion en f02 vers f03) : ")

            if engine.verif_format_coup(coup):  # vérifie si format correct
                equipe = self.table.cases[board.COORD.index(coup[1:4])].equipe

                if engine.verif_deplacment(coup, self.table, equipe):  # on peut jouer le coup
                    self.table.deplacement(self.table, coup, equipe)


if __name__ == "__main__":
    print("Changement mineur juste pour tester le push Github \N{grinning face}")
    table1 = board.Plateau()
    Game1 = Jeu(table1)
    Game1.jouer()

