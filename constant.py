
import pygame

# maze file
MAZE = "assets/map/maze.csv"

# structure area
NB_SPRITE = 15
SIZE_SPRITE = 30
XY_WINDOW = NB_SPRITE * SIZE_SPRITE
AREA = (XY_WINDOW, XY_WINDOW)

# initialyze hero
INIT_MAC_X = 7
INIT_MAC_Y = 0

# images
MAC = "assets/image/MacGyver.png"
ETHER = "assets/image/ether.png"
NEEDLE = "assets/image/aiguille.png"
PIPE = "assets/image/tube_plastique.png"
SYRINGE = "assets/image/seringue.png"
TEXTURE = "assets/image/floor-tiles-20x20.png"

# Object
ITEM = [
	[NEEDLE, 1],
	[ETHER, 1],
	[PIPE, 1],
]
# [SYRINGE, 2]

# COLOR
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)