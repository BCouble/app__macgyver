    game = True

    while game:
        for event in pygame.event.get():
            if event.type == QUIT:
                game = False
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                if event.key == K_UP:
                if event.key == K_LEFT:
                if event.key == K_RIGHT:

class Macgyver:
    """ Class Hero """
    def __init__(self):
        # position/sprite 
        self.macgyver = ()
        #self.Macgyver = (MAC(X, Y))

    def image_hero(self):
        MAC_G = pygame.image.load(MAC).convert_alpha()
        self.macgyver.append(MAC_G)

    def position(self):
        x = 3
        y = 40
        position = (x, y)
        return self.macgyver.append(position)

    def lire(self):
        print(self.macgyver)
