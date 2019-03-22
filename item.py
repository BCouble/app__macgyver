
import random
import pygame
from constant import *

class item:
    """ create list of item """
    def __init__(self):
        sprite_x = 0 
        sprite_y = 0
        self.item = ITEM
        self.obj = item
        self.opu = []
        self.sprite_x = sprite_x
        self.sprite_y = sprite_y
        inventory = 0
        self.inventory = inventory
        exist = []
        self.exist = exist
        image = ''
        self.image = image

    def create_item(self, matrix):
        """ create random position of items """
        self.matrix = matrix
        #del self.obj[:]
        exist = []
        item = []
        for self.opu in self.item:
            self.create_position(self.sprite_x, self.sprite_y)
            item.append(self.fill_item_list(self.opu, self.sprite_x, self.sprite_y))
            exist.append(item)
            self.exist = item
        self.obj = item

    def random_xy(self, sprite_x, sprite_y):
        self.sprite_x = random.randint(0, 14)
        self.sprite_y = random.randint(0, 14)
        return sprite_x, sprite_y

    def create_position(self, sprite_x, sprite_y):
        """ avoid overlay """
        while True:
            self.random_xy(self.sprite_x, self.sprite_y)
            while self.matrix.area[self.sprite_y][self.sprite_x] != "#":
                self.random_xy(self.sprite_x, self.sprite_y)
            self.duplicate_check(self.fill_item_list, self.obj)
            break
        return sprite_x, sprite_y

    def duplicate_check(self, init_item_list, exist):
        check = self.fill_item_list(self.opu, self.sprite_x, self.sprite_y)
        print(self.exist)
        num_line = 0
        if self.exist != []:
            for line in self.exist:
                if check[2] == self.exist[num_line][2] and check[3] == self.exist[num_line][3]:
                    print("égalité")
                    self.create_position(self.sprite_x, self.sprite_y)
                num_line += 1
        else:
            pass

    def fill_item_list(self, opu, sprite_x, sprite_y):
        init_item_list = []
        init_item_list = self.opu.copy()
        init_item_list.append(sprite_x)
        init_item_list.append(sprite_y)
        init_item_list.append(0)
        return init_item_list

    def generate_item(self, window):
        self.window = window
        num_line = 0
        inventory = 0
        for line in self.obj:
            if self.obj[num_line][4] == 0:
                obj_x = self.obj[num_line][2] * SIZE_SPRITE
                obj_y = self.obj[num_line][3] * SIZE_SPRITE
            if self.obj[num_line][4] == 1:
                obj_x = OBJ_X_INVENTORY
                obj_y = num_line * SIZE_SPRITE
                inventory += 1
            self.image = self.obj[num_line][0]
            self.img_load_scale_blit(obj_x, obj_y, self.image, self.window)
            self.inventory = inventory
            num_line += 1

    def display_serynge(self, window):
        if self.inventory == 3:
            self.image = SYRINGE
            obj_x = OBJ_X_INVENTORY
            obj_y = OBJ_Y_SERYNGE
            self.img_load_scale_blit(obj_x, obj_y, self.image, self.window)

    def img_load_scale_blit(self, obj_x, obj_y, image, window):
        img = pygame.image.load(self.image).convert_alpha()
        img = pygame.transform.scale(img, (SIZE_SPRITE, SIZE_SPRITE))
        self.window.blit(img, (obj_x, obj_y))