import argparse
import board
import engine
import json
import constante as c 


def argument_argparse():
    """
    Methode qui renvoi les arguments passés en commande sous la forme d'une liste
    :return: Une liste qui contient les arguments
    :rtype: Liste
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--nombre-joueur", type=int, help="nombre de joueur, entre 2 et 4")
    parser.add_argument("--score", help="si vous voulez afficher les scores et le réinitialiser sinon "
                                        "garder en mémoire pour la prochaine fois [oui/non]")

    return parser.parse_args()


class Jeu:
    def __init__(self, plateau=board.Plateau(), joueurs=c.JOUEURS_POSSIBLE, nombre_tour=0,
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

        self.Is_jeu_en_cours = True
        self.plateau = plateau
        self.joueurs = joueurs
        self.nombre_tour = nombre_tour
        self.nmbr_tour_plateau = nmbr_tour_plateau
        self.points_joueur = c.SCORES_VIDE
        self.Is_drapeu_neutre = True
        self.count_tour_drapeau_neutre = 0

    def ajout_score(self):
        """
        Ajoute le score au fichier txt
        :return: /
        :rtype: /
        """
        total_scores = json.dumps(self.points_joueur)
        with open(c.FICHIER_POINTS, "a") as file:
            file.write(total_scores + "\n")

    def afficher_score(self):
        """
        affiche le score en cours du fichier txt dans le terminal et vide le fichier
        :return: /
        :rtype: /
        """
        global data_locale

        self.ajout_score()
        try:
            data_locale = open(c.FICHIER_POINTS)
        except FileNotFoundError:
            print('Fichier introuvable.')
        scores_equipes = c.SCORES_VIDE
        for line in data_locale:
            score_d_une_partie = json.loads(line)
            for equipe in score_d_une_partie:
                scores_equipes[equipe] += score_d_une_partie[equipe]

        joueur_perdant = min(scores_equipes, key=scores_equipes.get)

        print("le joueur qui a perdu est " + joueur_perdant + "\nVoici les scores exact :" + str(scores_equipes))
        print("les score ont été réinitialisé")
        with open(c.FICHIER_POINTS, "w") as fichier_a_vider:
            fichier_a_vider.write("")

    def joueur_prochain(self, equipe_en_cours):
        """
        Determine le prochain joueur
        :param equipe_en_cours: le joueur  qui a fini de jouer
        :type equipe_en_cours: string
        :return: le prochain joueur dont c est le tour
        :rtype: string
        """
        try:
            return self.joueurs[self.joueurs.index(equipe_en_cours) - 1]
        except IndexError:
            print("Une erreur inattendue est arrivée, la partie prend fin")
            self.Is_jeu_en_cours = False

    def joueur_max_point(self):
        """
        Methode qui renvoi le joueur qui eu le plus de points
        :return: renvoi la couleur du joueur
        :rtype: string
        """
        return max(self.points_joueur, key=self.points_joueur.get)

    def fin_partie(self, joueur_gagnant):
        """
        Met fin a la partie en changeant le boolean is_jeu_en_cours et donne les point bonus (cfr regles)
        :param joueur_gagnant: le joueurs qui a le plus de points ou qui est resté sur la case en dernier
        :type joueur_gagnant: string
        :return: /
        :rtype: /
        """
        self.points_joueur[joueur_gagnant] += c.PTS_BONUS_VAINQEUR
        print(self.points_joueur)
        print("Féliciation au joueur " + joueur_gagnant + " !!!")
        self.Is_jeu_en_cours = False

    def actualiser_plateau_fin_de_tour(self, equipe_en_jeu):
        """
        Methode qui set a actualiser le plateau en fin de tour
        :param equipe_en_jeu: Une liste qui contient les joueurs de la partie
        :type equipe_en_jeu: Liste de string
        :return:
        :rtype:
        """
         if self.couleur_drapeau() != "white":  # drapeau pris par une équipe
            self.points_joueur[self.couleur_drapeau()] += c.PTS_PAR_TOUR
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
        """
        Méthode qui vérifie les conditions des regles a la fin de chaque tour
        :param self: ?
        :type self: ?
        :return: /
        :rtype: /
        """
        if self.nmbr_tour_plateau == c.NMBR_MAX_TOUR_VIDE and self.Is_drapeu_neutre:
            # drapeau pas pris avant le 10ème tour de plateau
            for i in range(len(self.joueurs)):  # on met des malus
                self.points_joueur[self.joueurs[-i]] -= (c.PTS_BONUS_VAINQEUR - c.PTS_PAR_TOUR * i)
            self.Is_jeu_en_cours = False

        if not self.Is_drapeu_neutre and self.couleur_drapeau() == "white":
            # drapeau a déjà été pris MAIS il n'est plus occupé
            self.count_tour_drapeau_neutre += 1
            if self.count_tour_drapeau_neutre >= c.NMBR_MAX_TOUR_SANS_REPRISER:
                joueur_pts_bonus = self.joueur_max_point()
                self.fin_partie(joueur_pts_bonus)

        for equipe in self.joueurs:
            if self.points_joueur[equipe] >= c.MAX_PTS:
                # partie finie si on joueur gagne 100pts
                joueur_pts_bonus = self.joueur_max_point()
                self.fin_partie(joueur_pts_bonus)

        if not engine.is_drapeau_prenable(self.plateau) and self.couleur_drapeau() != "white":
            # si drapeau n'est pas prenable et que quelqu'un est dessus
            self.fin_partie(self.couleur_drapeau())

    def validation_coup(self, coup, equipe_en_jeu):
        """
        Méthode qui valide le coup
        :param coup: le déplacement mémorisé via l input main
        :type coup: string
        :param equipe_en_jeu: Une liste qui contient les joueurs de la partie
        :type equipe_en_jeu: Liste de string
        :return: ?
        :rtype: ?
        """
        return (engine.verif_format_coup(coup) and engine.is_place_occupee(self.plateau, coup, equipe_en_jeu)
                and engine.is_case_interdit(self.plateau, coup) and
                engine.verif_deplacement(coup, self.plateau, equipe_en_jeu))

    def is_pas_bonne_equipe(self, equipe_en_jeu, move):
        """

        :param self:
        :type self:
        :param equipe_en_jeu: Une liste qui contient les joueurs de la partie
        :type equipe_en_jeu: Liste de string
        :param move:
        :type move:
        :return:
        :rtype:
        """
        return equipe_en_jeu != self.plateau.cases[c.COORD.index(move[1:4])].equipe

    @staticmethod
    def is_prise_de_drapeau(equipe_drapeau, move):
        """

        :param equipe_drapeau:
        :type equipe_drapeau:
        :param move:
        :type move:
        :return:
        :rtype:
        """
        return equipe_drapeau != "white" and move[4:7] == "h08"

    def couleur_drapeau(self):
        """

        :param self:
        :type self:
        :return:
        :rtype:
        """
        return self.plateau.cases[c.COORD.index("h08")].equipe

    def jeu(self):
        """
        Joue la partie du programme en console et prend les inputs
        :return: /
        :rtype: /
        """

        self.plateau.init_plateau(self.joueurs)
        self.plateau.afficher_plateau()
        equipe_en_jeu = self.joueur_prochain(c.EQUIPE_QUI_COMMENCE)
        # force la première équipe à jouer à être après le yellow ( donc green -> red -> blue )

        while self.Is_jeu_en_cours:
            print("tour du joueur", equipe_en_jeu)
            move = input("Quel pièce voulez vous déplacer vers quel case ? (Format, pf02f03 = pion en f02 vers f03) : ")

            if self.validation_coup(move, equipe_en_jeu):
                # vérifie si format correct et place libre et case pas interdite

                if self.is_pas_bonne_equipe(equipe_en_jeu, move):
                    # vérifie si le pion déplacé est le bon
                    print("Vous ne possédez pas de pion sur cette case!")
                    continue
                else:
                    equipe_drapeau = self.couleur_drapeau()
                    if self.is_prise_de_drapeau(equipe_drapeau, move):
                        # si le drapeau est pris, on devra lancer une contre-attaque
                        self.plateau.deplacement(self.plateau, move, equipe_en_jeu)
                        contre_attaque_finie = False
                        if engine.is_contre_attaque_sur_flag_possible(self.plateau, equipe_drapeau):
                            print(" coup possible :",
                                  engine.is_contre_attaque_sur_flag_possible(self.plateau, equipe_drapeau))
                            while not contre_attaque_finie:
                                print("tour du joueur", equipe_drapeau)
                                move = input("Quel pièce voulez vous déplacer vers quel case ? "
                                             "(Format, pf02f03 = pion en f02 vers f03) : ")

                                if self.validation_coup(move, equipe_en_jeu):
                                    self.plateau.deplacement(self.plateau, move, equipe_drapeau)
                                    contre_attaque_finie = True

                    elif not self.is_prise_de_drapeau(equipe_drapeau, move):
                        # on joue le coup normal
                        if self.validation_coup(move, equipe_en_jeu):  # on peut jouer le coup
                            self.plateau.deplacement(self.plateau, move, equipe_en_jeu)

                    equipe_en_jeu = self.actualiser_plateau_fin_de_tour(equipe_en_jeu)
                    # actualisation des paramètres de la partie

                self.verif_regle_fin_tour()
            else:
                print("Coup impossible")


if __name__ == "__main__":

    args = argument_argparse()
    nmbr_joueurs = args.nombre_joueur if args.nombre_joueur else 4
    cokoteurs = c.JOUEURS_POSSIBLE[0:int(nmbr_joueurs)]

    afficher_score = args.score

    echiquier = board.Plateau()
    Game = Jeu(echiquier, cokoteurs)
    Game.jeu()

    if afficher_score.lower() == "oui":
        Game.afficher_score()
    elif afficher_score.lower() == "non":
        Game.ajout_score()
    else:
        print("paramètre incorrect de l'arugment --score")
