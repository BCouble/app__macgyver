class item:
    """ create list of item """
    def __init__(self):
        sprite_x = 0 
        sprite_y = 0
        self.item = ITEM
        self.obj = []
        self.sprite_x = sprite_x
        self.sprite_y = sprite_y
        self.inventory = ""

    def create_item(self, matrix):
        """ create random position of items """
        self.matrix = matrix
        del self.obj[:]
        item = []
        for opu in self.item:
            self.create_position(self.sprite_x, self.sprite_y)
            item.append(self.fill_item_list(opu, self.sprite_x, self.sprite_y))
            print(item)
        self.obj = item

    def random_xy(self, sprite_x, sprite_y):
        self.sprite_x = random.randint(0, 14)
        self.sprite_y = random.randint(0, 14)
        #print(sprite_x, sprite_y)
        return sprite_x, sprite_y

    def create_position(self, sprite_x, sprite_y):
        """ avoid overlay """
        while True:
            print("Premier random")
            self.random_xy(self.sprite_x, self.sprite_y)
            print(self.matrix.area[self.sprite_y][self.sprite_x])
            print(self.sprite_x, self.sprite_y)
            while self.matrix.area[self.sprite_y][self.sprite_x] != "#":
                print("Boucle random")
                self.random_xy(self.sprite_x, self.sprite_y)
                print(self.matrix.area[self.sprite_y][self.sprite_x])
                print(self.sprite_x, self.sprite_y)
            break
        return sprite_x, sprite_y

    def fill_item_list(self, opu, sprite_x, sprite_y):
        init_item_list = []
        init_item_list = opu.copy()
        init_item_list.append(sprite_x)
        init_item_list.append(sprite_y)
        init_item_list.append(0)
        return init_item_list

    def generate_item(self, window):
        inventory = 0
        num_line = 0
        for line in self.obj:
            # creation of objects on the labyrinth
            if self.obj[num_line][4] == 0:
                obj_x = self.obj[num_line][2] * SIZE_SPRITE
                obj_y = self.obj[num_line][3] * SIZE_SPRITE
            # creation of the objects in the inventory
            if self.obj[num_line][4] == 1:
                obj_x = 15 * SIZE_SPRITE
                obj_y = num_line * SIZE_SPRITE
                inventory += 1
                # creation of the syringe
                if inventory == 3:
                    obj_x = 15 * SIZE_SPRITE
                    obj_y = 5 * SIZE_SPRITE
                    imga = pygame.image.load(SYRINGE).convert_alpha()
                    imga = pygame.transform.scale(imga, (SIZE_SPRITE, SIZE_SPRITE))
                    window.blit(imga, (obj_x, obj_y))
                    self.inventory = inventory
            # display
            img = pygame.image.load(self.obj[num_line][0]).convert_alpha()
            img = pygame.transform.scale(img, (SIZE_SPRITE, SIZE_SPRITE))
            window.blit(img, (obj_x, obj_y))
            num_line += 1