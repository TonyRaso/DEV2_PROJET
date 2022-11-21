import board
import piece
import engine
import json


class Game:
    def __init__(self, plateau, joueurs, nombre_tour=0, nmbr_tour_plateau=0):
        self.Is_jeu_en_cours = True
        self.plateau = plateau
        self.joueurs = joueurs
        self.nombre_tour = nombre_tour
        self.nmbr_tour_plateau = nmbr_tour_plateau
        self.points_joueur = {}
        self.Is_drapeu_neutre = True
        self.count_tour_drapeau_neutre = 0

    def ajout_score(self):
        data = json.dumps(self.points_joueur)
        with open('data.txt', "a") as file:
            file.write(data + "\n")

    def afficher_score(self):
        self.ajout_score()
        try:
            file = open('data.txt')
        except FileNotFoundError:
            print('Fichier introuvable.')
        equipes = {"green": 0, "red": 0, "blue": 0, "yellow": 0, }
        for line in file:
            dic = json.loads(line)
            for equipe in dic:
                equipes[equipe] += dic[equipe]
        min_pts = 999
        for joueur in equipes:
            if equipes[joueur] <= min_pts:
                min_pts = equipes[joueur]
                joueur_perdant = joueur

        print("le joueur qui a perdu est " + joueur_perdant + "\nvoici les scores exact :" + str(equipes))
        print("les score ont été réinitialisé")
        with open('data.txt', "w") as file:
            file.write("")

    def joueur_prochain(self, equipe_en_cours):
        joueur = self.joueurs[self.joueurs.index(equipe_en_cours) - 1]
        return joueur

    def init_point_joueur(self):
        for joueur in self.joueurs:
            self.points_joueur[joueur] = 0

    def joueur_max_point(self):
        max_points = -1
        joueur_gagnant = ""
        for joueur in self.joueurs:
            if self.points_joueur[joueur] >= max_points:
                max_points = self.points_joueur[joueur]
                joueur_gagnant = joueur
        return joueur_gagnant

    def fin_partie(self, joueur_gagnant):
        self.points_joueur[joueur_gagnant] += 20
        print(self.points_joueur)
        print("Féliciation au joueur " + joueur_gagnant + " !!!")
        self.Is_jeu_en_cours = False

    def gestionscore(self):
        print("\n La partie est Finie !")
        Is_input_ok = False
        while not Is_input_ok:
            afficher_score = input(
                "Voulez-vous réinitialiser les scores et afficher les scores depuis la dernière fois ? ('oui'/'non')")
            if afficher_score == "oui":
                self.afficher_score()
                Is_input_ok = True

            elif afficher_score == "non":
                self.ajout_score()
                Is_input_ok = True
            else:
                print("input incorrect")

    def jeu(self):
        self.plateau.afficher_plateau(self.joueurs)
        equipe_en_jeu = self.joueur_prochain("yellow")
        self.init_point_joueur()
        # force la première équipe à jouer à être après le yellow ( donc green -> red -> blue )

        while self.Is_jeu_en_cours:
            print("tour du joueur", equipe_en_jeu)
            move = input("Quel pièce voulez vous déplacer vers quel case ? (Format, pf02f03 = pion en f02 vers f03) : ")

            if engine.verif_format_coup(move) \
                    and engine.is_place_occupee(self.plateau, move, equipe_en_jeu) and engine.is_case_interdit(
                self.plateau, move):
                # vérifie si format correct et place libre et case pas interdite

                if equipe_en_jeu != self.plateau.cases[board.COORD.index(move[1:4])].equipe:
                    # vérifie si le pion déplacé est le bon
                    print("Vous ne possédez pas de pion sur cette case!")
                    continue

                if engine.verif_deplacment(move, self.plateau, equipe_en_jeu):  # on peut jouer le coup
                    self.plateau.deplacement(self.plateau, move, equipe_en_jeu)

                    if self.plateau.cases[board.COORD.index("h08")].equipe != "white":  # drapeau pris par une équipe
                        self.points_joueur[self.plateau.cases[board.COORD.index("h08")].equipe] += 5
                        self.Is_drapeu_neutre = False
                        # si le drapeau est pris, compteur de tour de drapeau neutre = 0
                        self.count_tour_drapeau_neutre = 0
                        print(self.points_joueur)

                    equipe_en_jeu = self.joueur_prochain(equipe_en_jeu)

                    self.nombre_tour += 1
                    if self.nombre_tour % len(self.joueurs):  # compte le nmbr de tour de plateau
                        self.nmbr_tour_plateau += 1

            if self.nmbr_tour_plateau == 10 and self.Is_drapeu_neutre:
                # drapeau pas pris avant le 10ème tour de plateau
                for i in range(len(self.joueurs)):  # on met des malus
                    self.points_joueur[self.joueurs[-i]] -= (20 - 5 * i)
                self.Is_jeu_en_cours = False

            if not self.Is_drapeu_neutre and self.plateau.cases[board.COORD.index("h08")].equipe == "white":
                # drapeau a déjà été pris MAIS il n'est plus occupé
                self.count_tour_drapeau_neutre += 1
                if self.count_tour_drapeau_neutre >= 5:
                    joueur_pts_bonus = self.joueur_max_point()
                    self.fin_partie(joueur_pts_bonus)

            for equipe in self.joueurs:
                if self.points_joueur[equipe] >= 100:
                    # partie finie si on joueur gagne 100pts
                    joueur_pts_bonus = self.joueur_max_point()
                    self.fin_partie(joueur_pts_bonus)

            if not engine.Is_drapeau_prenable(self.plateau) and \
                    self.plateau.cases[board.COORD.index("h08")].equipe != "white":
                # si drapeau n'est pas prenable et que quelqu'un est dessus
                self.fin_partie(self.plateau.cases[board.COORD.index("h08")].equipe)

            if self.nombre_tour == 100:
                self.Is_jeu_en_cours = False

        if not self.Is_jeu_en_cours:
            # jeu fini
            self.gestionscore()


if __name__ == "__main__":
    nmbr_joueurs = 0
    nmbr_joueurs_possible = ["2", "3", "4"]
    nmbr_player_ok = True

    while nmbr_player_ok:
        nmbr_joueurs = input("Combien de joueurs êtes vous ? (entre 2 et 4)")
        if nmbr_joueurs not in nmbr_joueurs_possible:
            print("input impossible, recommencez")
        elif nmbr_joueurs in nmbr_joueurs_possible:
            nmbr_player_ok = False

    joueurs = ["yellow", "blue", "red", "green"]
    joueurs = joueurs[0:int(nmbr_joueurs)]

    plateau1 = board.Plateau()
    Game1 = Game(plateau1, joueurs)
    Game1.jeu()
