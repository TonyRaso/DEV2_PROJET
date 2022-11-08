import board
import piece
import engine


class Game:
    def __init__(self, table, joueurs, nombre_tour=0):
        self.IsGameON = True
        self.table = table
        self.joueurs = joueurs
        self.nombre_tour = nombre_tour
        self.points_joueur = {}

    def joueur_prochain(self, equipe_en_cours):
        joueur = self.joueurs[self.joueurs.index(equipe_en_cours) - 1]
        return joueur

    def init_point_joueur(self):
        for joueur in self.joueurs:
            self.points_joueur[joueur] = 0

    def play(self):
        self.table.format_board(self.joueurs)
        equipe_en_jeu = self.joueur_prochain("yellow")
        self.init_point_joueur()
        # force la première équipe à jouer à être après le yellow ( donc green -> red -> blue )

        while self.IsGameON:
            print("tour du joueur", equipe_en_jeu)
            move = input("Quel pièce voulez vous déplacer vers quel case ? (Format, pf02f03 = pion en f02 vers f03) : ")

            if engine.verif_format_move(move) \
                    and engine.is_place_occupee(table, move, equipe_en_jeu) and engine.is_case_interdit(table, move):
                # vérifie si format correct et place libre et case pas interdite

                if equipe_en_jeu != self.table.cases[board.COORD.index(move[1:4])].equipe:
                    # vérifie si le pion déplacé est le bon
                    print("Vous ne possédez pas de pion sur cette case!")
                    continue

                if engine.verif_deplacment(move, self.table, equipe_en_jeu):  # on peut jouer le coup
                    table.moveto(table, move, equipe_en_jeu)

                    if self.table.cases[board.COORD.index("h08")].equipe != "white":  # drapeau pris par une équipe
                        self.points_joueur[self.table.cases[board.COORD.index("h08")].equipe] += 5
                        print(self.points_joueur)
                    equipe_en_jeu = self.joueur_prochain(equipe_en_jeu)
                    self.nombre_tour += 1
            if self.nombre_tour == 100:
                self.IsGameON = False


if __name__ == "__main__":
    nmbr_joueurs = 0
    nmbr_joueurs_possible = ["2", "3", "4"]
    nmbr_player_OK = True

    while nmbr_player_OK:
        nmbr_joueurs = input("Combien de joueurs êtes vous ? (entre 2 et 4)")
        if nmbr_joueurs not in nmbr_joueurs_possible:
            print("input impossible, recommencez")
        elif nmbr_joueurs in nmbr_joueurs_possible:
            nmbr_player_OK = False

    joueurs = ["yellow", "blue", "red", "green"]
    joueurs = joueurs[0:int(nmbr_joueurs)]

    table = board.Board()
    Game1 = Game(table, joueurs)
    Game1.play()
