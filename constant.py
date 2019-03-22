# maze file
MAZE = "assets/map/maze.csv"

# structure area window
NB_SPRITE_L = 16
NB_SP_H = 15
SIZE_SPRITE = 30
X_WINDOW = NB_SPRITE_L * SIZE_SPRITE
Y_WINDOW = NB_SP_H * SIZE_SPRITE
AREA = (X_WINDOW, Y_WINDOW)

# init position hero
INIT_MAC_X = 7
INIT_MAC_Y = 0

# init guard
G_XY = 14
POS_GUARD = G_XY * SIZE_SPRITE

# images
MAC = "assets/image/MacGyver.png"
ETHER = "assets/image/ether.png"
NEEDLE = "assets/image/aiguille.png"
PIPE = "assets/image/tube_plastique.png"
SYRINGE = "assets/image/seringue.png"
TEXTURE = "assets/image/floor-tiles-20x20.png"
GUARDIAN = "assets/image/Gardien.png"
START = "assets/image/MacGyver_home_master.jpg"
WINNER = "assets/image/winner.jpg"
LOOSER = "assets/image/looser.jpg"

# items
ITEM = [
	[NEEDLE, 1],
	[ETHER, 1],
	[PIPE, 1],
]

# inventory
OBJ_X_INVENTORY = NB_SP_H * SIZE_SPRITE
OBJ_Y_SERYNGE = 5 * SIZE_SPRITE