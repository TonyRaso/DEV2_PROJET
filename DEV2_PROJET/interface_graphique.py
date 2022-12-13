import pygame as p
import board
import engine
import sys
from main import Jeu, argument_argparse
import constante as c

IMAGES = {}


def charge_images():
    """
    initialise un repertoire d'image qui sera appelé une seul fois
    :return: /
    :rtype: /   
    """
    for piece in c.NOM_IMAGES:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (c.TAILLE_CASE, c.TAILLE_CASE))


def selection_equipe(plateau, equipe_en_jeu, ecran):
    """
    Souligne en jaune la totalité des pieces du joueur dont c'est le tour
    :param ecran: la fenetre du gui renvoyé par py.game
    :type ecran: Objet de type Surface
    :param plateau: la table dans l état actuelle
    :type plateau: un objet de type Plateau
    :param equipe_en_jeu: équipe dont c'est le tour
    :type equipe_en_jeu: string
    :return: /
    :rtype: /
    """
    for case in range(len(plateau)):
        if plateau[case].equipe == equipe_en_jeu:
            row = int(case / 15)
            col = case % 15
            s = p.Surface((c.TAILLE_CASE, c.TAILLE_CASE))
            s.set_alpha(40)  # transparency value 0 -> transparent, 255 -> opaque
            s.fill(p.Color('yellow'))
            ecran.blit(s, (col * c.TAILLE_CASE, row * c.TAILLE_CASE))


def selection_case(case_cliquee, ecran):
    """
    Souligne en bleu la case sur laquel on a clické
    :param case_cliquee:
    :param ecran: la fenetre du gui renvoyé par py.game
    :type ecran: Objet de type Surface
    :return: /
    :rtype: /
    """
    if case_cliquee != 0:
        row = int(case_cliquee / 15)
        col = case_cliquee % 15
        # highlight selected square
        s = p.Surface((c.TAILLE_CASE, c.TAILLE_CASE))
        s.set_alpha(90)  # transparency value 0 -> transparent, 255 -> opaque
        s.fill(p.Color('blue'))
        ecran.blit(s, (col * c.TAILLE_CASE, row * c.TAILLE_CASE))


def draw_game_state(plateau, case_cliquee, equipe_en_jeu, ecran):
    """
    Responsable de tout les graphismes dans le jeux (utilise selection equipe et selection case)
    :param ecran: la fenetre du gui renvoyé par py.game
    :type ecran: Objet de type Surface
    :param plateau: la table dans l état actuelle
    :type plateau: un objet de type Plateau
    :param  case_cliquee: la case cliquée
    :type  case_cliquee: int
    :param equipe_en_jeu: équipe dont c'est le tour
    :type equipe_en_jeu: string
    :return: /
    :rtype: /
    """

    afficher_plateau(ecran)  # draw squares on the board
    draw_pieces(plateau, ecran)  # draw pieces on top of those squares
    selection_case(case_cliquee, ecran)  # highlight case choisie
    selection_equipe(plateau, equipe_en_jeu, ecran)  # highlight equipe en jeu


def afficher_plateau(ecran):
    """
    Dessine les cases blanches et noir
    :return: /
    :rtype: /
    """
    taille = c.TAILLE_CASE
    global colors
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(c.DIMENSION):
        for column in range(c.DIMENSION):
            color = colors[((row + column) % 2)]
            p.draw.rect(ecran, color, p.Rect(column * taille, row * taille, taille, taille))


def draw_pieces(plateau, ecran):
    """
    Affiche les pieces par dessus les cases
    :param ecran: la fenetre du gui renvoyé par py.game
    :type ecran: Objet de type Surface
    :param plateau: la table dans l état actuelle
    :type plateau: un objet de type Plateau
    :return: /
    :rtype: /
    """
    taille = c.TAILLE_CASE
    count = 0
    for row in range(c.DIMENSION):
        for col in range(c.DIMENSION):
            piece = str(plateau[count])
            if piece != "." and piece != " ":
                ecran.blit(IMAGES[piece + plateau[count].equipe], p.Rect(col * taille, row * taille, taille, taille))

            elif piece == " ":
                ecran.blit(IMAGES[plateau[count].equipe],
                           p.Rect(col * taille, row * taille, taille, taille))
            count += 1

    ecran.blit(IMAGES["Xwhite"], p.Rect(7 * taille, 7 * taille, taille, taille))


class GuiJeu(Jeu):
    def __init__(self, plateau=board.Plateau(), joueurs=c.JOUEURS_POSSIBLE, nombre_tour=0, nmbr_tour_plateau=0):
        """
        Classe enfant de jeu,ajoute l'interface graphique
        :param plateau: recoit la table de jeux a l'état de démarrage
        :type plateau: un objet de classe Plateau
        :param joueurs: liste des joueurs en jeu
        :type joueurs: list de string
        :param nombre_tour: compteur de tour en int
        :type nombre_tour: int
        :param nmbr_tour_plateau:differencie le tour d'un joueur et le tour de table
        :type nmbr_tour_plateau: int
        """
        self.clique_joueur = []
        self.case_cliquee = 0
        super().__init__(plateau, joueurs, nombre_tour, nmbr_tour_plateau)

    @staticmethod
    def recuperer_index_clique():
        """

        :return:
        :rtype:
        """
        location = p.mouse.get_pos()  # (x, y) location of the mouse
        col = location[0] // c.TAILLE_CASE
        row = location[1] // c.TAILLE_CASE
        return col + row * 15

    def reinitilaise_le_coup(self):
        """

        :return:
        :rtype:
        """
        self.clique_joueur = []
        self.case_cliquee = 0

    def clique_vers_coup(self):
        """

        :return:
        :rtype:
        """
        return str(self.plateau.cases[self.clique_joueur[0]]).lower() + c.COORD[self.clique_joueur[0]] + c.COORD[
            self.clique_joueur[1]]

    def rafraichissement_gui(self, clock, equipe, ecran):
        """

        :param clock:
        :type clock:
        :param equipe:
        :type equipe:
        :param ecran:
        :type ecran:
        :return:
        :rtype:
        """
        clock.tick(15)
        p.display.flip()
        draw_game_state(self.plateau.cases, self.case_cliquee, equipe, ecran)

    def gestion_clique(self, k):
        """

        :param k:
        :type k:
        :return:
        :rtype:
        """
        if k.type == p.QUIT:
            p.quit()
            sys.exit()
        # mouse handler
        elif k.type == p.MOUSEBUTTONDOWN:
            index = self.recuperer_index_clique()
            if self.case_cliquee == index:  # user clicked the same square twice
                self.reinitilaise_le_coup()
            else:
                self.case_cliquee = index
                self.clique_joueur.append(self.case_cliquee)  # append for both 1st and 2nd click
            if len(self.clique_joueur) == 2:
                return True
        return False

    def jeu_visuel(self):
        """
        Joue la partie du programme en GUI et prend les inputs
        :return: /
        :rtype: /
        """
        self.plateau.init_plateau(self.joueurs)
        clock = p.time.Clock()
        ecran = p.display.set_mode((c.LARGEUR, c.HAUTEUR))
        ecran.fill(p.Color("white"))
        p.init()

        equipe_en_jeu = self.joueur_prochain(c.JOUEURS_POSSIBLE[0])
        charge_images()
        while self.Is_jeu_en_cours:
            for e in p.event.get():
                if self.gestion_clique(e):  # after 2nd click on joue
                    move = self.clique_vers_coup()
                    print(move)
                    if self.validation_coup(move, equipe_en_jeu):
                        # vérifie si format correct et place libre et case pas interdite
                        if self.is_pas_bonne_equipe(equipe_en_jeu, move):
                            # vérifie si le pion déplacé est le bon
                            self.reinitilaise_le_coup()
                            continue
                        else:  # on peut jouer le coup
                            equipe_drapeau = self.couleur_drapeau()
                            if self.is_prise_de_drapeau(equipe_drapeau, move):
                                # si le drapeau est pris, on devra lancer une contre-attaque
                                self.plateau.deplacement(self.plateau, move, equipe_en_jeu)
                                contre_attaque_finie = False
                                self.reinitilaise_le_coup()
                                if engine.is_contre_attaque_sur_flag_possible(self.plateau, equipe_drapeau):
                                    print(" coup possible :",
                                          engine.is_contre_attaque_sur_flag_possible(self.plateau, equipe_drapeau))
                                    while not contre_attaque_finie:  # contre-attaque
                                        for i in p.event.get():
                                            if self.gestion_clique(i):  # after 2nd click on joue
                                                move = self.clique_vers_coup()
                                                print(move)
                                                if self.is_pas_bonne_equipe(equipe_drapeau, move):
                                                    # vérifie si le pion rdt de la bonne équipe
                                                    self.reinitilaise_le_coup()
                                                    continue
                                                if move in engine.is_contre_attaque_sur_flag_possible(
                                                        self.plateau, equipe_drapeau):
                                                    # vérifie si on peut jouer le coup
                                                    self.plateau.deplacement(self.plateau, move, equipe_drapeau)
                                                    contre_attaque_finie = True
                                                    self.reinitilaise_le_coup()
                                        self.rafraichissement_gui(clock, equipe_drapeau, ecran)
                                        # fin contre attaque

                            elif not self.is_prise_de_drapeau(equipe_drapeau, move):
                                # on joue le coup normal
                                if self.validation_coup(move, equipe_en_jeu):
                                    if equipe_en_jeu != self.plateau.cases[c.COORD.index(move[1:4])].equipe:
                                        # vérifie si le pion déplacé est le bon
                                        self.reinitilaise_le_coup()
                                        continue
                                    else:  # on peut jouer le coup
                                        self.plateau.deplacement(self.plateau, move, equipe_en_jeu)

                            equipe_en_jeu = self.actualiser_plateau_fin_de_tour(equipe_en_jeu)
                            # actualisation des paramètres de la partie

                        self.reinitilaise_le_coup()
                        # vérifie les règles
                        self.verif_regle_fin_tour()
                    else:
                        print("Coup impossible")
                        self.reinitilaise_le_coup()

            self.rafraichissement_gui(clock, equipe_en_jeu, ecran)


if __name__ == "__main__":

    args = argument_argparse()

    nmbr_joueurs = args.nombre_joueur if args.nombre_joueur else 4
    cokoteurs = c.JOUEURS_POSSIBLE[0:int(nmbr_joueurs)]

    afficher_score = args.score

    echiquier = board.Plateau()
    Game = GuiJeu(echiquier, cokoteurs)
    Game.jeu_visuel()

    if afficher_score.lower() == "oui":
        Game.afficher_score()
    elif afficher_score.lower() == "non":
        Game.ajout_score()
    else:
        print("input incorrect")
