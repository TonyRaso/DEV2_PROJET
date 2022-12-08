import argparse
import board
import engine
import json
#import constante

parser = argparse.ArgumentParser()
parser.add_argument("--nombre-joueur", type=int, help="nombre de joueur, entre 2 et 4")
parser.add_argument("--score", help="si vous voulez afficher les scores et le réinitialiser sinon "
                                    "garder en mémoire pour la prochaine fois [oui/non]")

args = parser.parse_args()


class Jeu:
    def __init__(self, plateau=board.Plateau(), joueurs=None, nombre_tour=0,
                 nmbr_tour_plateau=0):
        """
        Methode qui initialise la partie et qui la stop selon les regles
        Elle compte les point et determine le tour des joueurs et gere les regles de fin de partie
        :param plateau: recoit la table de jeux a l'état de démarrage
        :type plateau: un objet de classe Plateau
        :param joueurs: liste des joueurs en jeu
        :type joueurs: list de string
        :param nombre_tour: compteur de tour en int
        :type nombre_tour: int
        :param nmbr_tour_plateau:differencie le tour d'un joueur et le tour de table
        :type nmbr_tour_plateau: int
        """

        if joueurs is None:
            joueurs = ["yellow", "blue", "red", "green"]
        self.Is_jeu_en_cours = True
        self.plateau = plateau
        self.joueurs = joueurs
        self.nombre_tour = nombre_tour
        self.nmbr_tour_plateau = nmbr_tour_plateau
        self.points_joueur = {}
        self.Is_drapeu_neutre = True
        self.count_tour_drapeau_neutre = 0

    def ajout_score(self):
        """
        Ajoute le score au fichier txt
        :return: /
        :rtype: /
        """
        data = json.dumps(self.points_joueur)
        with open('data.txt', "a") as file:
            file.write(data + "\n")

    def afficher_score(self):
        """
        affiche le score en cours du fichier txt dans le terminal
        :return: /
        :rtype: /
        """
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
        """
        Determine le prochain joueur
        :param equipe_en_cours: le joueur  qui a fini de jouer
        :type equipe_en_cours: string
        :return: le prochain joueur dont c est le tour
        :rtype: string
        """
        joueur = self.joueurs[self.joueurs.index(equipe_en_cours) - 1]
        return joueur

    def init_point_joueur(self):
        """
        Initialise les points des joueurs a 0
        :return: /
        :rtype: /
        """
        for joueur in self.joueurs:
            self.points_joueur[joueur] = 0

    def joueur_max_point(self):
        """
        Methode qui renvoi le joueur qui eu le plus de points
        :return: renvoi la couleur du joueur
        :rtype: string
        """
        max_points = -1
        joueur_gagnant = ""
        for joueur in self.joueurs:
            if self.points_joueur[joueur] >= max_points:
                max_points = self.points_joueur[joueur]
                joueur_gagnant = joueur
        return joueur_gagnant

    def fin_partie(self, joueur_gagnant):
        """
        Met fin a la partie en changeant le boolean is_jeu_en_cours et donne les point bonus (cfr regles)
        :param joueur_gagnant: le joueurs qui a le plus de points
        :type joueur_gagnant: string
        :return: /
        :rtype: /
        """
        self.points_joueur[joueur_gagnant] += 20
        print(self.points_joueur)
        print("Féliciation au joueur " + joueur_gagnant + " !!!")
        self.Is_jeu_en_cours = False

    def actualiser_plateau_fin_de_tour(self, equipe_en_jeu):
        if self.plateau.cases[board.COORD.index("h08")].equipe != "white":  # drapeau pris par une équipe
            self.points_joueur[self.plateau.cases[board.COORD.index("h08")].equipe] += 5
            self.Is_drapeu_neutre = False
            # si le drapeau est pris, compteur de tour de drapeau neutre = 0
            self.count_tour_drapeau_neutre = 0
            print(self.points_joueur)

        equipe_en_jeu = self.joueur_prochain(equipe_en_jeu)

        self.nombre_tour += 1
        if self.nombre_tour % len(self.joueurs) == 0:  # compte le nmbr de tour de plateau
            self.nmbr_tour_plateau += 1

        return equipe_en_jeu

    def verif_regle_fin_tour(self):
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

        if not engine.is_drapeau_prenable(self.plateau) and \
                self.plateau.cases[board.COORD.index("h08")].equipe != "white":
            # si drapeau n'est pas prenable et que quelqu'un est dessus
            self.fin_partie(self.plateau.cases[board.COORD.index("h08")].equipe)

        if self.nombre_tour == 100:
            self.Is_jeu_en_cours = False

    def validation_coup(self, coup, equipe_en_jeu):
        return (engine.verif_format_coup(coup) and engine.is_place_occupee(self.plateau, coup, equipe_en_jeu)
                and engine.is_case_interdit(self.plateau, coup) and
                engine.verif_deplacment(coup, self.plateau, equipe_en_jeu))

    def jeu(self):
        """
        Joue la partie du programme en console et prend les inputs
        :return: /
        :rtype: /
        """

        self.plateau.init_plateau(self.joueurs)
        self.plateau.afficher_plateau()
        equipe_en_jeu = self.joueur_prochain("yellow")
        self.init_point_joueur()
        # force la première équipe à jouer à être après le yellow ( donc green -> red -> blue )

        while self.Is_jeu_en_cours:
            print("tour du joueur", equipe_en_jeu)
            move = input("Quel pièce voulez vous déplacer vers quel case ? (Format, pf02f03 = pion en f02 vers f03) : ")

            # ce if est remplaçable par self.validation_coup(move, equipe_en_jeu)
            if engine.verif_format_coup(move) \
                    and engine.is_place_occupee(self.plateau, move, equipe_en_jeu) and engine.is_case_interdit(
                self.plateau, move):
                # vérifie si format correct et place libre et case pas interdite

                if equipe_en_jeu != self.plateau.cases[board.COORD.index(move[1:4])].equipe:
                    # vérifie si le pion déplacé est le bon
                    print("Vous ne possédez pas de pion sur cette case!")
                    continue

                if engine.verif_deplacment(move, self.plateau, equipe_en_jeu): # on peut jouer le coup r.validation_coup
                    equipe_drapeau = self.plateau.cases[board.COORD.index("h08")].equipe
                    if equipe_drapeau != "white" and move[4:7] == "h08":
                        # si le drapeau est pris, on devra lancer une contre-attaque
                        self.plateau.deplacement(self.plateau, move, equipe_en_jeu)
                        contre_attaque_finie = False
                        if engine.is_contre_attaque_sur_flag_possible(self.plateau, equipe_drapeau):
                            while not contre_attaque_finie:
                                print("tour du joueur", equipe_drapeau)
                                move = input(
                                    "Quel pièce voulez vous déplacer vers quel case ? "
                                    "(Format, pf02f03 = pion en f02 vers f03) : ")
                                # ce if est remplaçable par self.validation_coup(move, equipe_en_jeu)
                                if engine.verif_format_coup(move) \
                                        and engine.is_place_occupee(self.plateau, move,
                                                                    equipe_drapeau) and engine.is_case_interdit(
                                    self.plateau, move):
                                    self.plateau.deplacement(self.plateau, move, equipe_drapeau)
                                    contre_attaque_finie = True

                    elif move[4:7] != "h08" or equipe_drapeau == "white" and move[4:7] == "h08":
                        # on joue le coup normal
                        # ce if est remplaçable par self.validation_coup(move, equipe_en_jeu)
                        if engine.verif_format_coup(move) and engine.is_place_occupee(self.plateau, move,
                                                                                      equipe_en_jeu) and \
                                engine.is_case_interdit(self.plateau, move):
                            if engine.verif_deplacment(move, self.plateau, equipe_en_jeu):  # on peut jouer le coup
                                self.plateau.deplacement(self.plateau, move, equipe_en_jeu)

                    # remplaçable par equipe_en_jeu = self.actualiser_plateau_fin_de_tour(equipe_en_jeu)
                    if self.plateau.cases[board.COORD.index("h08")].equipe != "white":  # drapeau pris par une équipe
                        self.points_joueur[self.plateau.cases[board.COORD.index("h08")].equipe] += 5
                        self.Is_drapeu_neutre = False
                        # si le drapeau est pris, compteur de tour de drapeau neutre = 0
                        self.count_tour_drapeau_neutre = 0
                        print(self.points_joueur)

                    equipe_en_jeu = self.joueur_prochain(equipe_en_jeu)

                    self.nombre_tour += 1
                    if self.nombre_tour % len(self.joueurs) == 0:  # compte le nmbr de tour de plateau
                        self.nmbr_tour_plateau += 1
                    # fin de self.fin_de_tour()

            # peut être remplacé par self.actualiser_plateau_fin_de_tour()
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

            if not engine.is_drapeau_prenable(self.plateau) and \
                    self.plateau.cases[board.COORD.index("h08")].equipe != "white":
                # si drapeau n'est pas prenable et que quelqu'un est dessus
                self.fin_partie(self.plateau.cases[board.COORD.index("h08")].equipe)

            if self.nombre_tour == 100:
                self.Is_jeu_en_cours = False
            # fin de self.verif_regle_fin_tour()


if __name__ == "__main__":
    joueurs1 = ["yellow", "blue", "red", "green"]

    nmbr_joueurs = args.nombre_joueur
    if not nmbr_joueurs:
        nmbr_joueurs = 4
    joueurs1 = joueurs1[0:int(nmbr_joueurs)]

    afficher_score = args.score

    plateau1 = board.Plateau()
    Game1 = Jeu(plateau1, joueurs1)
    Game1.jeu()

    if afficher_score == "oui":
        Game1.afficher_score()
    elif afficher_score == "non":
        Game1.ajout_score()
    else:
        print("input incorrect")
