import pygame as p
import board
import engine
import sys
from main import Jeu

LARGEUR = HAUTEUR = 600
DIMENSION = 15
TAILLE_CASE = HAUTEUR // DIMENSION
IMAGES = {}
p.init()

ecran = p.display.set_mode((LARGEUR, HAUTEUR))


def charge_images():
    """
    Initialize a global directory of images.
    This will be called exactly once in the main.
    """
    pieces = ["Pred", "Cred", "Fred", "Tred", "Dred", "Pblue", "Cblue", "Fblue", "Tblue", "Dblue", "Pyellow", "Cyellow",
              "Fyellow", "Tyellow", "Dyellow", "Pgreen", "Cgreen", "Fgreen", "Tgreen", "Dgreen", "Xwhite", "white"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (TAILLE_CASE, TAILLE_CASE))


def selection_equipe(ecran, plateau, equipe_en_jeu):
    for case in range(len(plateau)):
        if plateau[case].equipe == equipe_en_jeu:
            row = int(case / 15)
            col = case % 15
            s = p.Surface((TAILLE_CASE, TAILLE_CASE))
            s.set_alpha(40)  # transparency value 0 -> transparent, 255 -> opaque
            s.fill(p.Color('yellow'))
            ecran.blit(s, (col * TAILLE_CASE, row * TAILLE_CASE))


def selection_case(ecran, case_cliquee):
    if case_cliquee != 0:
        row = int(case_cliquee / 15)
        col = case_cliquee % 15
        # highlight selected square
        s = p.Surface((TAILLE_CASE, TAILLE_CASE))
        s.set_alpha(90)  # transparency value 0 -> transparent, 255 -> opaque
        s.fill(p.Color('blue'))
        ecran.blit(s, (col * TAILLE_CASE, row * TAILLE_CASE))


def drawGameState(ecran, plateau, case_cliquee, equipe_en_jeu):
    """
    Responsible for all the graphics within current game state.
    """
    afficher_plateau(ecran)  # draw squares on the board
    drawPieces(ecran, plateau)  # draw pieces on top of those squares
    selection_case(ecran, case_cliquee)  # highlight case choisie
    selection_equipe(ecran, plateau, equipe_en_jeu)  # highlight equipe en jeu


def afficher_plateau(ecran):
    """
    Draw the squares on the board.
    The top left square is always light.
    """
    global colors
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[((row + column) % 2)]
            p.draw.rect(ecran, color,
                        p.Rect(column * TAILLE_CASE, row * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))


def drawPieces(screen, plateau):
    """
    Draw the pieces on the board using the current game_state.board
    """
    count = 0
    for row in range(15):
        for col in range(15):
            piece = str(plateau[count])
            if piece != "." and piece != " ":
                screen.blit(IMAGES[piece + plateau[count].equipe],
                            p.Rect(col * TAILLE_CASE, row * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))

            elif piece == " ":
                screen.blit(IMAGES[plateau[count].equipe],
                            p.Rect(col * TAILLE_CASE, row * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))

            count += 1


def mousclicker(plateau):
    move = ""
    case_cliquee = 0
    clique_joueur = []
    for e in p.event.get():
        if e.type == p.QUIT:
            p.quit()
            sys.exit()

        # mouse handler
        elif e.type == p.MOUSEBUTTONDOWN:
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
            print(clique_joueur)
            if len(clique_joueur) == 2:  # after 2nd click on joue
                equipe_piece = plateau.cases[clique_joueur[0]].equipe
                move = str(plateau.cases[clique_joueur[0]]).lower() + board.COORD[clique_joueur[0]] + \
                       board.COORD[clique_joueur[1]]
                print(move)
    return move


class GUI_jeu(Jeu):
    def __init__(self, plateau=board.Plateau(), joueurs=None, nombre_tour=0, nmbr_tour_plateau=0):
        super().__init__(plateau, joueurs, nombre_tour, nmbr_tour_plateau)

    def jeu_visuel(self):
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
                                        while not contre_attaque_finie:
                                            for i in p.event.get():
                                                if i.type == p.QUIT:
                                                    p.quit()
                                                    sys.exit()
                                                # mouse handler
                                                elif i.type == p.MOUSEBUTTONDOWN:
                                                    if self.Is_jeu_en_cours:
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
                                                            print(move, engine.Is_contre_attaque_sur_flag_possible(self.plateau, equipe_drapeau))
                                                            if move in engine.Is_contre_attaque_sur_flag_possible(
                                                                    self.plateau, equipe_drapeau):
                                                                # vérifie si format correct et place libre
                                                                # et case pas interdite
                                                                # et coup dans les coups autorisé en contre-attaque
                                                                # on peut jouer le coup
                                                                self.plateau.deplacement(self.plateau, move, equipe_drapeau)
                                                                contre_attaque_finie = True
                                            clock.tick(15)
                                            p.display.flip()
                                            drawGameState(ecran, self.plateau.cases, case_cliquee, equipe_drapeau)
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

                            if not engine.Is_drapeau_prenable(self.plateau) and \
                                    self.plateau.cases[board.COORD.index("h08")].equipe != "white":
                                # si drapeau n'est pas prenable et que quelqu'un est dessus
                                self.fin_partie(self.plateau.cases[board.COORD.index("h08")].equipe)

                            if self.nombre_tour == 100:
                                self.Is_jeu_en_cours = False

            clock.tick(15)
            p.display.flip()
            drawGameState(ecran, self.plateau.cases, case_cliquee, equipe_en_jeu)


plateau1 = board.Plateau()
a = GUI_jeu()
a.jeu_visuel()
