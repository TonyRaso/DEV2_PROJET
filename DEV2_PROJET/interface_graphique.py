import pygame as p
import board
import engine
import sys
import argparse
from main import Jeu

LARGEUR = HAUTEUR = 600
DIMENSION = 15
TAILLE_CASE = HAUTEUR // DIMENSION
IMAGES = {}
p.init()

ecran = p.display.set_mode((LARGEUR, HAUTEUR))

parser = argparse.ArgumentParser()
parser.add_argument("--nombre-joueur", type=int, help="nombre de joueur, entre 2 et 4")
parser.add_argument("--score", help="si vous voulez afficher les scores et le réinitialiser sinon "
                                    "garder en mémoire pour la prochaine fois [oui/non]")

args = parser.parse_args()


def charge_images():
    """
    initialise un repertoire d'image qui sera appelé une seul fois
    :return: /
    :rtype: /
    """

    pieces = ["Pred", "Cred", "Fred", "Tred", "Dred", "Pblue", "Cblue", "Fblue", "Tblue", "Dblue", "Pyellow", "Cyellow",
              "Fyellow", "Tyellow", "Dyellow", "Pgreen", "Cgreen", "Fgreen", "Tgreen", "Dgreen", "Xwhite", "white"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (TAILLE_CASE, TAILLE_CASE))


def selection_equipe(ecran, plateau, equipe_en_jeu):
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
            s = p.Surface((TAILLE_CASE, TAILLE_CASE))
            s.set_alpha(40)  # transparency value 0 -> transparent, 255 -> opaque
            s.fill(p.Color('yellow'))
            ecran.blit(s, (col * TAILLE_CASE, row * TAILLE_CASE))


def selection_case(ecran, case_cliquee):
    """
    Souligne en bleu la case sur laquel on a clické
    :param ecran: la fenetre du gui renvoyé par py.game
    :type ecran: Objet de type Surface
    :param case_cliquee: la case cliquée
    :type case_cliquee: int
    :return: /
    :rtype: /
    """
    if case_cliquee != 0:
        row = int(case_cliquee / 15)
        col = case_cliquee % 15
        # highlight selected square
        s = p.Surface((TAILLE_CASE, TAILLE_CASE))
        s.set_alpha(90)  # transparency value 0 -> transparent, 255 -> opaque
        s.fill(p.Color('blue'))
        ecran.blit(s, (col * TAILLE_CASE, row * TAILLE_CASE))


def draw_game_state(ecran, plateau, case_cliquee, equipe_en_jeu):
    """
    Responsable de tout les graphismes dans le jeux (utilise selection equipe et selection case)
    :param ecran: la fenetre du gui renvoyé par py.game
    :type ecran: Objet de type Surface
    :param plateau: la table dans l état actuelle
    :type plateau: un objet de type Plateau
    :param case_cliquee: la case cliquée
    :type case_cliquee: int
    :param equipe_en_jeu: équipe dont c'est le tour
    :type equipe_en_jeu: string
    :return: /
    :rtype: /
    """

    afficher_plateau(ecran)  # draw squares on the board
    draw_pieces(ecran, plateau)  # draw pieces on top of those squares
    selection_case(ecran, case_cliquee)  # highlight case choisie
    selection_equipe(ecran, plateau, equipe_en_jeu)  # highlight equipe en jeu


def afficher_plateau(ecran):
    """
    Dessine les cases blanches et noir
    :param ecran: la fenetre du gui renvoyé par py.game
    :type ecran: Objet de type Surface
    :return: /
    :rtype: /
    """

    global colors
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[((row + column) % 2)]
            p.draw.rect(ecran, color,
                        p.Rect(column * TAILLE_CASE, row * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))


def draw_pieces(screen, plateau):
    """
    Affiche les pieces par dessus les cases
    :param screen:la fenetre du gui renvoyé par py.game
    :type screen:Objet de type Surface
    :param plateau: la table dans l état actuelle
    :type plateau: un objet de type Plateau
    :return: /
    :rtype: /
    """

    count = 0
    for row in range(15):
        for col in range(15):
            piece = str(plateau[count])
            if piece != "." and piece != " ":
                screen.blit(IMAGES[piece + plateau[count].equipe], p.Rect(col * TAILLE_CASE, row * TAILLE_CASE,
                                                                         TAILLE_CASE, TAILLE_CASE))

            elif piece == " ":
                screen.blit(IMAGES[plateau[count].equipe],
                            p.Rect(col * TAILLE_CASE, row * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))
            count += 1

    screen.blit(IMAGES["Xwhite"], p.Rect(7 * TAILLE_CASE, 7 * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))


class GuiJeu(Jeu):
    def __init__(self, plateau=board.Plateau(), joueurs=None, nombre_tour=0, nmbr_tour_plateau=0):
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
        super().__init__(plateau, joueurs, nombre_tour, nmbr_tour_plateau)

    def jeu_visuel(self):
        """
        Joue la partie du programme en GUI et prend les inputs
        :return: /
        :rtype: /
        """
        self.plateau.init_plateau(self.joueurs)
        clock = p.time.Clock()
        ecran.fill(p.Color("white"))
        case_cliquee = 0
        clique_joueur = []
        ecran.fill(p.Color("white"))

        equipe_en_jeu = self.joueur_prochain("yellow")
        self.init_point_joueur()
        charge_images()
        while self.Is_jeu_en_cours:
            for e in p.event.get():
                if e.type == p.QUIT:
                    p.quit()
                    sys.exit()

                # mouse handler
                elif e.type == p.MOUSEBUTTONDOWN:
                    if self.Is_jeu_en_cours:
                        location = p.mouse.get_pos()  # (x, y) location of the mouse
                        col = location[0] // TAILLE_CASE
                        row = location[1] // TAILLE_CASE
                        index = (col + row * 15)
                        if case_cliquee == index or col >= DIMENSION:  # user clicked the same square twice
                            case_cliquee = 0  # deselect
                            clique_joueur = []  # clear clicks
                        else:
                            case_cliquee = index
                            clique_joueur.append(case_cliquee)  # append for both 1st and 2nd click
                        if len(clique_joueur) == 2:  # after 2nd click on joue
                            move = str(self.plateau.cases[clique_joueur[0]]).lower() + board.COORD[clique_joueur[0]] + \
                                   board.COORD[clique_joueur[1]]
                            print(move)
                            arrivee = move[4:7]
                            if engine.verif_format_coup(move) \
                                    and engine.is_place_occupee(self.plateau, move,
                                                                equipe_en_jeu) and engine.is_case_interdit(self.plateau,
                                                                                                           move):
                                # vérifie si format correct et place libre et case pas interdite
                                if equipe_en_jeu != self.plateau.cases[board.COORD.index(move[1:4])].equipe:
                                    # vérifie si le pion déplacé est le bon
                                    case_cliquee = 0  # reset user clicks
                                    clique_joueur = []
                                    continue

                                if engine.verif_deplacment(move, self.plateau, equipe_en_jeu):  # on peut jouer le coup
                                    equipe_drapeau = self.plateau.cases[board.COORD.index("h08")].equipe
                                    if equipe_drapeau != "white" and arrivee == "h08":
                                        # si le drapeau est pris, on devra lancer une contre-attaque
                                        self.plateau.deplacement(self.plateau, move, equipe_en_jeu)
                                        contre_attaque_finie = False
                                        case_cliquee = 0  # deselect
                                        clique_joueur = []  # clear clicks
                                        print(engine.is_contre_attaque_sur_flag_possible(self.plateau, equipe_drapeau))
                                        if engine.is_contre_attaque_sur_flag_possible(self.plateau, equipe_drapeau):
                                            while not contre_attaque_finie:  # contre-attaque
                                                for i in p.event.get():
                                                    if i.type == p.QUIT:
                                                        p.quit()
                                                        sys.exit()
                                                    # mouse handler
                                                    elif i.type == p.MOUSEBUTTONDOWN:
                                                        location = p.mouse.get_pos()  # (x, y) location of the mouse
                                                        col = location[0] // TAILLE_CASE
                                                        row = location[1] // TAILLE_CASE
                                                        index = (col + row * 15)
                                                        if case_cliquee == index or col >= DIMENSION:
                                                            # user clicked the same square twice
                                                            case_cliquee = 0  # deselect
                                                            clique_joueur = []  # clear clicks
                                                        else:
                                                            case_cliquee = index
                                                            clique_joueur.append(
                                                                case_cliquee)  # append for both 1st and 2nd click
                                                        if len(clique_joueur) == 2:  # after 2nd click on joue
                                                            move = str(self.plateau.cases[clique_joueur[0]]).lower() + \
                                                                   board.COORD[clique_joueur[0]] + \
                                                                   board.COORD[clique_joueur[1]]
                                                            print(move)
                                                            if equipe_drapeau != self.plateau.cases[
                                                                board.COORD.index(move[1:4])].equipe:
                                                                # vérifie si le pion déplacé est le bon
                                                                case_cliquee = 0  # reset user clicks
                                                                clique_joueur = []
                                                                continue

                                                            if move in engine.is_contre_attaque_sur_flag_possible(
                                                                    self.plateau, equipe_drapeau):
                                                                # vérifie si format correct et place libre
                                                                # et case pas interdite
                                                                # et coup dans les coups autorisé en contre-attaque
                                                                # on peut jouer le coup
                                                                self.plateau.deplacement(self.plateau, move,
                                                                                         equipe_drapeau)
                                                                contre_attaque_finie = True
                                                                case_cliquee = 0  # reset user clicks
                                                                clique_joueur = []

                                                clock.tick(15)
                                                p.display.flip()
                                                draw_game_state(ecran, self.plateau.cases, case_cliquee, equipe_drapeau)
                                                # fin contre attaque
                                    elif arrivee != "h08" or equipe_drapeau == "white" and arrivee == "h08":
                                        # on joue le coup normal
                                        if engine.verif_format_coup(move) \
                                                and engine.is_place_occupee(self.plateau, move,
                                                                            equipe_en_jeu) and engine.is_case_interdit(
                                            self.plateau, move):

                                            # vérifie si format correct et place libre et case pas interdite
                                            if equipe_en_jeu != self.plateau.cases[board.COORD.index(move[1:4])].equipe:
                                                # vérifie si le pion déplacé est le bon
                                                case_cliquee = 0  # reset user clicks
                                                clique_joueur = []
                                                continue

                                            if engine.verif_deplacment(move, self.plateau,
                                                                       equipe_en_jeu):  # on peut jouer le coup
                                                self.plateau.deplacement(self.plateau, move, equipe_en_jeu)

                                    if self.plateau.cases[
                                        board.COORD.index("h08")].equipe != "white":  # drapeau pris par une équipe
                                        self.points_joueur[self.plateau.cases[board.COORD.index("h08")].equipe] += 5
                                        self.Is_drapeu_neutre = False
                                        # si le drapeau est pris, compteur de tour de drapeau neutre = 0
                                        self.count_tour_drapeau_neutre = 0
                                        print(self.points_joueur)

                                    equipe_en_jeu = self.joueur_prochain(equipe_en_jeu)

                                    self.nombre_tour += 1
                                    if self.nombre_tour % len(self.joueurs) == 0:  # compte le nmbr de tour de plateau
                                        self.nmbr_tour_plateau += 1

                                case_cliquee = 0  # reset user clicks
                                clique_joueur = []
                            else:
                                case_cliquee = 0  # reset user clicks
                                clique_joueur = []

                            # vérifie les règles

                            if self.nmbr_tour_plateau == 10 and self.Is_drapeu_neutre:
                                # drapeau pas pris avant le 10ème tour de plateau
                                for i in range(len(self.joueurs)):  # on met des malus
                                    self.points_joueur[self.joueurs[-i]] -= (20 - 5 * i)
                                self.Is_jeu_en_cours = False

                            if not self.Is_drapeu_neutre and self.plateau.cases[
                                board.COORD.index("h08")].equipe == "white":
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

            clock.tick(15)
            p.display.flip()
            draw_game_state(ecran, self.plateau.cases, case_cliquee, equipe_en_jeu)


if __name__ == "__main__":

    joueur1 = ["yellow", "blue", "red", "green"]

    nmbr_joueurs = args.nombre_joueur
    if not nmbr_joueurs:
        nmbr_joueurs = 4

    joueur1 = joueur1[0:int(nmbr_joueurs)]

    afficher_score = args.score

    plateau1 = board.Plateau()
    Game2 = GuiJeu(plateau1, joueur1)
    Game2.jeu_visuel()

    if afficher_score == "oui":
        Game2.afficher_score()
    elif afficher_score == "non":
        Game2.ajout_score()
    else:
        print("input incorrect")
