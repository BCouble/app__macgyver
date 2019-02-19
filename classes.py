""" 
	We will put here the classes of the game
"""
# Import constants


# Sprite
class Sprite:
	pass

# the area
class Area:
	""" Grid of the game board """
	#Attribut de la class :
	SPRITES = []
	SPRITES_ABSSISSE_MIN : 0
	SPRITES_ABSSISSE_MAX : 14
	SPRITES_ORDONNE_MIN : 0
	SPRITES_ORDONNE_MAX : 14
	
	def __init(self, corner1, corner2):
		self.corner1 = corner1
		self.corner2 = corner2
		self.elements = 0

# oblects

# guardian

