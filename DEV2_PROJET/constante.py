# On définit toutes les constantes qu'on utilisera dans les différents fichiers

COORD = [
    'a15', 'b15', 'c15', 'd15', 'e15', 'f15', 'g15', 'h15', 'i15', 'j15', 'k15', 'l15', 'm15', 'n15', 'o15',
    'a14', 'b14', 'c14', 'd14', 'e14', 'f14', 'g14', 'h14', 'i14', 'j14', 'k14', 'l14', 'm14', 'n14', 'o14',
    'a13', 'b13', 'c13', 'd13', 'e13', 'f13', 'g13', 'h13', 'i13', 'j13', 'k13', 'l13', 'm13', 'n13', 'o13',
    'a12', 'b12', 'c12', 'd12', 'e12', 'f12', 'g12', 'h12', 'i12', 'j12', 'k12', 'l12', 'm12', 'n12', 'o12',
    'a11', 'b11', 'c11', 'd11', 'e11', 'f11', 'g11', 'h11', 'i11', 'j11', 'k11', 'l11', 'm11', 'n11', 'o11',
    'a10', 'b10', 'c10', 'd10', 'e10', 'f10', 'g10', 'h10', 'i10', 'j10', 'k10', 'l10', 'm10', 'n10', 'o10',
    'a09', 'b09', 'c09', 'd09', 'e09', 'f09', 'g09', 'h09', 'i09', 'j09', 'k09', 'l09', 'm09', 'n09', 'o09',
    'a08', 'b08', 'c08', 'd08', 'e08', 'f08', 'g08', 'h08', 'i08', 'j08', 'k08', 'l08', 'm08', 'n08', 'o08',
    'a07', 'b07', 'c07', 'd07', 'e07', 'f07', 'g07', 'h07', 'i07', 'j07', 'k07', 'l07', 'm07', 'n07', 'o07',
    'a06', 'b06', 'c06', 'd06', 'e06', 'f06', 'g06', 'h06', 'i06', 'j06', 'k06', 'l06', 'm06', 'n06', 'o06',
    'a05', 'b05', 'c05', 'd05', 'e05', 'f05', 'g05', 'h05', 'i05', 'j05', 'k05', 'l05', 'm05', 'n05', 'o05',
    'a04', 'b04', 'c04', 'd04', 'e04', 'f04', 'g04', 'h04', 'i04', 'j04', 'k04', 'l04', 'm04', 'n04', 'o04',
    'a03', 'b03', 'c03', 'd03', 'e03', 'f03', 'g03', 'h03', 'i03', 'j03', 'k03', 'l03', 'm03', 'n03', 'o03',
    'a02', 'b02', 'c02', 'd02', 'e02', 'f02', 'g02', 'h02', 'i02', 'j02', 'k02', 'l02', 'm02', 'n02', 'o02',
    'a01', 'b01', 'c01', 'd01', 'e01', 'f01', 'g01', 'h01', 'i01', 'j01', 'k01', 'l01', 'm01', 'n01', 'o01',
]

JOUEURS_POSSIBLE = ["yellow", "blue", "red", "green"]
INPUT_VERS_PIECE = {"p": "PION", "f": "FOU", "d": "DAME", "t": "TOUR", "c": "CAVALIER"}
LIST_PIECE = ["p", "c", "f", "t", "d"]
vecteur_tour = [-15, 15]
vecteur_fou = [16, -16, 14, -14]
vecteur_dame = [-15, 15, -16, 16, -14, 14]
coup_cavalier = [29, 31, 13, 17, -17, -13, -31, -29]
LARGEUR = HAUTEUR = 600
DIMENSION = 15
TAILLE_CASE = HAUTEUR // DIMENSION
SCORES_VIDE = {"green": 0, "red": 0, "blue": 0, "yellow": 0, }
PTS_BONUS_VAINQEUR = 20
PTS_PAR_TOUR = 5
NMBR_MAX_TOUR_VIDE = 10
NMBR_MAX_TOUR_SANS_REPRISER = 5
MAX_PTS = 100
NOM_IMAGES = ["Pred", "Cred", "Fred", "Tred", "Dred", "Pblue", "Cblue", "Fblue", "Tblue", "Dblue", "Pyellow", "Cyellow",
              "Fyellow", "Tyellow", "Dyellow", "Pgreen", "Cgreen", "Fgreen", "Tgreen", "Dgreen", "Xwhite", "white"]
FICHIER_POINTS = 'data.txt'
CASE_DRAPEAU = "h08"
EQUIPE_QUI_COMMENCE = "yellow"
TRANSPARENCE_SELECTION_GUI =90
TRANSPARENCE_SELECTION_EQUIPE_GUI =40