""" 
	We will put here the classes of the game
"""
# agent	
class Sprite:
	""" class that generates the boxes 
	according to its symbol and its position """
	def __init__(self, symbol, position):
		self.symbol = symbol
		self.position = position

# position
class Position:
	""" class that retrieves positions 
	according to the maze list """
	def __init__(self, x, y):
		self.x = x
		self.y = y

# zone
class Area:
	""" Grid of the game board 
	x-axe = lines y-axe = column """

	AREA = []
	MIN_X_PIXEL = 0
	MAX_X_PIXEL = 450
	MIN_Y_PIXEL = 0
	MAX_Y_PIXEL = 450
	WIDTH_PIXEL = 30
	HEIGHT_PIXEL = 30

	def __init__(self, corner1, corner2):
		self.corner1 = corner1
		self.corner2 = corner2
		self.insprites = []

	def add_insprite(self, insprite):
		self.insprites.append(insprite)

	def contains(self, position):
		return position.x >= min(self.corner1.x, self.corner2.x) and \
            position.x < max(self.corner1.x, self.corner2.x) and \
            position.y >= min(self.corner1.y, self.corner2.y) and \
            position.y < max(self.corner1.y, self.corner2.y)

	@classmethod
	def find_sprite_that_area(cls, position):
		x_index = int((position.x - cls.MIN_X_PIXEL)/ cls.WIDTH_PIXEL)
		y_index = int((position.y - cls.MIN_Y_PIXEL)/ cls.HEIGHT_PIXEL)
		x_bins = int((cls.MAX_X_PIXEL - cls.MIN_X_PIXEL)/ cls.WIDTH_PIXEL)
		area_index = y_index * x_bins + x_index

		area = cls.AREA[area_index]
		assert area.contains(position)

		print(cls.area)

	@classmethod
	def initialize_area(cls):
		for y in range(cls.MIN_Y_PIXEL, cls.MAX_Y_PIXEL, cls.HEIGHT_PIXEL):
			for x in range(cls.MIN_X_PIXEL, cls.MAX_X_PIXEL, cls.WIDTH_PIXEL):
				top_left_corner = Position(x, y)
				bottom_right_corner = Position(x + cls.WIDTH_PIXEL, y + cls.HEIGHT_PIXEL)
				area = Area(top_left_corner, bottom_right_corner)
				cls.AREA.append(area)
		#print(len(cls.AREA))
		#for y in range(self.MIN_Y_PIXEL, self.MAX_Y_PIXEL, self.HEIGHT_PIXEL):
			#for x in range(self.MIN_X_PIXEL, self.MAX_X_PIXEL, self.WIDTH_PIXEL):


class Macgyver():

	def __init__(self, name):
		self.name = name

	def name(self):
		name = 'Macgyver'


def main():
	# appel class methode
	Area.initialize_area()
		# Loop Game Menu
			# end menu
		# Loop Game
			# end game

if __name__ == "__main__":
    main()
