import pygame as p
import board
import engine
import sys
from piece import Piece

from main import Game

LARGEUR = HAUTEUR = 512
DIMENSION = 15
TAILLE_CASE = HAUTEUR // DIMENSION
IMAGES = {}
p.init()

board = [
    Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),
    Piece('TOUR', "blue"), Piece('CAVALIER', "blue"), Piece('FOU', "blue"), Piece('DAME', "blue"),
    Piece('FOU', "blue"), Piece('CAVALIER', "blue"), Piece('TOUR', "blue"),
    Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),  # ligne 15

    Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),
    Piece('PION', "blue"), Piece('PION', "blue"), Piece('PION', "blue"), Piece('PION', "blue"),
    Piece('PION', "blue"), Piece('PION', "blue"), Piece('PION', "blue"),
    Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),  # ligne 14

    Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),
    Piece(''), Piece(''), Piece(''), Piece(''), Piece(''), Piece(''), Piece(''),
    Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),  # ligne 13

    Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),
    Piece(''), Piece(''), Piece(''), Piece(''), Piece(''), Piece(''), Piece(''),
    Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),  # ligne 12

    Piece('TOUR', "red"), Piece('PION', "red"),
    Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(),
    Piece('PION', "yellow"), Piece('TOUR', "yellow"),  # ligne 11

    Piece('CAVALIER', "red"), Piece('PION', "red"),
    Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(),
    Piece('PION', "yellow"), Piece('CAVALIER', "yellow"),  # ligne 10

    Piece('FOU', "red"), Piece('PION', "red"),
    Piece(), Piece(), Piece(), Piece(), Piece(), Piece('DAME', "red"), Piece(), Piece(), Piece(), Piece(),
    Piece(),
    Piece('PION', "yellow"), Piece('FOU', "yellow"),  # ligne 09

    Piece('DAME', "red"), Piece('PION', "red"),
    Piece(), Piece(), Piece(), Piece(), Piece('DAME', "blue"), Piece("FLAG", "white", True),
    Piece('DAME', "yellow"), Piece(), Piece(),
    Piece(), Piece(),
    Piece('PION', "yellow"), Piece('PION', "yellow"),  # ligne 08

    Piece('FOU', "red"), Piece('PION', "red"),
    Piece(), Piece(), Piece(), Piece(), Piece(), Piece("DAME", "green"), Piece("PION", "yellow"), Piece(),
    Piece(), Piece(),
    Piece(),
    Piece('PION', "yellow"), Piece('FOU', "yellow"),  # ligne 07

    Piece('CAVALIER', "red"), Piece('PION', "red"),
    Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(),
    Piece(),
    Piece('PION', "yellow"), Piece('CAVALIER', "yellow"),  # ligne 06

    Piece('TOUR', "red"), Piece('PION', "red"),
    Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(),
    Piece('PION', "yellow"), Piece('TOUR', "yellow"),  # ligne 05

    Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),
    Piece(''), Piece(''), Piece(''), Piece(''), Piece(''), Piece(''), Piece(''),
    Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),  # ligne 04

    Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),
    Piece(''), Piece(''), Piece(''), Piece(''), Piece(''), Piece(''), Piece(''),
    Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),  # ligne 03

    Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),
    Piece('PION', "green"), Piece('PION', "green"), Piece('PION', "green"), Piece('PION', "green"),
    Piece('PION', "green"), Piece('PION', "green"), Piece('PION', "green"),
    Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),  # ligne 02

    Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),
    Piece('TOUR', "green"), Piece('CAVALIER', "green"), Piece('FOU', "green"), Piece('DAME', "green"),
    Piece('FOU', "green"), Piece('CAVALIER', "green"), Piece('TOUR', "green"),
    Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'), Piece('INTERDIT'),  # ligne 01
]

ecran = p.display.set_mode((LARGEUR, HAUTEUR))


def charge_images():
    """
    Initialize a global directory of images.
    This will be called exactly once in the main.
    """
    pieces = ["P", "C", "F", "T", "D", "X"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (TAILLE_CASE, TAILLE_CASE))


def jeu_visuel():
    clock = p.time.Clock()
    ecran.fill(p.Color("white"))
    case_cliquee = ()
    clique_joueur = []
    ecran.fill(p.Color("white"))
    equipe = "green"

    charge_images()
    while True:
        for e in p.event.get():
            if e.type == p.QUIT:
                p.quit()
                sys.exit()
            clock.tick(15)
            p.display.flip()
            drawGameState(ecran)

            # mouse handler
            # elif e.type == p.MOUSEBUTTONDOWN:
            #   if not Is_jeu_en_cours:
            #      location = p.mouse.get_pos()  # (x, y) location of the mouse
            #     col = location[0] // TAILLE_CASE
            #    row = location[1] // TAILLE_CASE
            #   if case_cliquee == (row, col) or col >= 8:  # user clicked the same square twice
            #      square_selected = ()  # deselect
            #     clique_joueur = []  # clear clicks
            # else:
            #   square_selected = (row, col)
            #  clique_joueur.append(square_selected)  # append for both 1st and 2nd click
            # if len(clique_joueur) == 2:  # after 2nd click
            #   move = (clique_joueur[0], clique_joueur[1], board)

            #  if engine.verif_deplacment(move, plateau, equipe):
            #     plateau.deplacement(move)
            #    move_made = True
            #   animate = True
            #  square_selected = ()  # reset user clicks
            # clique_joueur = []


def afficher_plateau():
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


def drawGameState(ecran):
    """
    Responsible for all the graphics within current game state.
    """
    drawBoard(ecran)  # draw squares on the board
    drawPieces(ecran)  # draw pieces on top of those squares


def drawBoard(screen):
    """
    Draw the squares on the board.
    The top left square is always light.
    """
    global colors
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[((row + column) % 2)]
            p.draw.rect(screen, color, p.Rect(column * TAILLE_CASE, row * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))


def drawPieces(screen):
    """
    Draw the pieces on the board using the current game_state.board
    """
    count = 0
    for row in range(15):
        for col in range(15):
            piece = str(board[count])
            if piece != "." and piece != " ":
                screen.blit(IMAGES[piece], p.Rect(col * TAILLE_CASE, row * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))
            count += 1



jeu_visuel()
