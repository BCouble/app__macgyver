
import os
import random
import csv
import pygame
from constant import *

class Maze:
    def __init__(self):
        """ creation of labyrinth from a csv file """
        self.structure = MAZE
        self.area = []

    def creation_area(self):
        """ create a list to represent the structure """
        structure_area = []
        with open(self.structure, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                structure_area.append(row)
        self.area = structure_area

    def generate_area(self, window):
        """ we will apply an image to each sprite of the structure """
        texture = pygame.image.load(TEXTURE).convert()
        WALL = texture.subsurface(0, 0, 20, 20)
        WALL = pygame.transform.scale(WALL, (SIZE_SPRITE, SIZE_SPRITE))
        PATH = texture.subsurface(20, 20, 20, 20)
        PATH = pygame.transform.scale(PATH, (SIZE_SPRITE, SIZE_SPRITE))
        START = texture.subsurface(160, 20, 20, 20)
        START = pygame.transform.scale(START, (SIZE_SPRITE, SIZE_SPRITE))
        num_line = 0
        for line in self.area:
            num_sprite = 0
            for sprite in line:
                x = num_sprite * SIZE_SPRITE
                y = num_line * SIZE_SPRITE
                if sprite == 'M':
                    window.blit(WALL, (x, y))
                elif sprite == 'D':
                    window.blit(START, (x, y))
                elif sprite == 'G':
                    window.blit(START, (x, y))
                else:
                    window.blit(PATH, (x, y))
                num_sprite += 1
            num_line += 1

class Macgyver:
    """ Class Hero """
    def __init__(self, spx, spy, mac, matrice):
        # position/sprite
        # image
        MAC_G = MAC
        self.sprite_x = spx
        self.sprite_y = spy
        self.x = self.sprite_x * SIZE_SPRITE
        self.y = self.sprite_y * SIZE_SPRITE
        self.mac = MAC_G
        # This matrice is the maze
        self.matrice = matrice
        #self.Maze = Maze

    def image_hero(self, mac):
        MAC_G = pygame.image.load(MAC).convert_alpha()
        MAC_G = MAC_G.subsurface(0, 0, 32, 32)
        MAC_G = pygame.transform.scale(MAC_G, (SIZE_SPRITE, SIZE_SPRITE))
        self.mac = MAC_G

    def position(self, compass):
        """ Method to move the hero """
        if compass == 'down':
            if self.sprite_y < NB_SPRITE - 1:
                #letter = self.matrice.area[self.sprite_y+1][self.sprite_x]
                if self.matrice.area[self.sprite_y+1][self.sprite_x] != "M":
                    # + 1 sur l'axe y
                    self.sprite_y += 1
                    self.y = self.sprite_y * SIZE_SPRITE
        if compass == 'up':
            # if the value of the y-axis is greater than the minimum y-axis value of the labyrinth
            if self.y > 0:
                if self.matrice.area[self.sprite_y-1][self.sprite_x] != "M":
                    # - 1 sur l'axe y 
                    self.sprite_y -= 1
                    # On recalcule l'emplacement graphique par rapport à la taille d'une sprite
                    self.y = self.sprite_y * SIZE_SPRITE
        if compass == 'left':
            if self.x > 0:
                if self.matrice.area[self.sprite_y][self.sprite_x-1] != "M":
                    self.sprite_x -= 1
                    self.x = self.sprite_x * SIZE_SPRITE
        if compass == 'right':
            if self.sprite_x < NB_SPRITE - 1:
                if self.matrice.area[self.sprite_y][self.sprite_x+1] != "M":
                    self.sprite_x += 1
                    self.x = self.sprite_x * SIZE_SPRITE

class item:
    """ create list of item """
    def __init__(self):
        self.item = ITEM
        self.obj = []

    def create_item(self, matrice):
        self.matrice = matrice
        # create position of items
        item = []
        exist_x = []
        for opu in self.item:
            #if sprite_x in exist_x == False:
                #exist_x.append(sprite_x)
            sprite_x = random.randint(0, 14)
            sprite_y = random.randint(0, 14)
            # if maze != #:
            while self.matrice.area[sprite_y][sprite_x] != "#":
                sprite_x = random.randint(0, 14)
                sprite_y = random.randint(0, 14)
            opu.append(sprite_x)
            opu.append(sprite_y)
            item.append(opu)
        # check position different
        """for opu in item:
            if item[i][2] and item[i][3] == item[n][2] and item[n][3]:
                if item[i][2] and item[i][3] == item[nu][2] and item[nu][3]:
                    sprite_x = random.randint(0, 14)
                    sprite_y = random.randint(0, 14)"""
        print(item)
        self.obj = item

    def generate_item(self, window):
        num_line = 0
        for line in self.obj:
            x = self.obj[num_line][2] * SIZE_SPRITE
            y = self.obj[num_line][3] * SIZE_SPRITE
            # layer alpha
            if num_line == 0:# NEEDLE
                img = pygame.image.load(self.obj[num_line][0]).convert_alpha()
                img = pygame.transform.scale(img, (SIZE_SPRITE, SIZE_SPRITE))
            if num_line == 1:# ETHER
                img = pygame.image.load(self.obj[num_line][0])
                img = pygame.transform.scale(img, (SIZE_SPRITE, SIZE_SPRITE))
                img.set_colorkey(BLACK)
            if num_line == 2:# PIPE
                img = pygame.image.load(self.obj[num_line][0])
                img.set_colorkey(WHITE)
                img = pygame.transform.scale(img, (SIZE_SPRITE, SIZE_SPRITE))
            window.blit(img, (x, y))
            num_line += 1

class interaction_sprite():
    """ Gestion des mouvements and objets """
    def __init__(self):
        pass

    def find_gardian(self):
        # maze letter G
        # if mac à la serynge il win 
        # else il loose
        pass

    def loot_item(self):
        # Item for 3 loot
        # tresor is serynge
        pass

























