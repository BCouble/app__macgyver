
import os
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

class Image:
    """ Ajustement des images """
    def __init__(self):
        pass

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
            #if self.y < SIZE_SPRITE:
                # + 1 sur l'axe y
            self.sprite_y += 1
            self.y = self.sprite_y * SIZE_SPRITE
            print("down")
            print(self.sprite_y)
            print(self.y)
        if compass == 'up':
            # if the value of the y-axis is greater than the minimum y-axis value of the labyrinth
            #if self.y > 0:
                # - 1 sur l'axe y 
            self.sprite_y -= 1
                # On recalcule l'emplacement graphique par rapport à la taille d'une sprite
            self.y = self.sprite_y * SIZE_SPRITE
            print("up")
            print(self.sprite_y)
            print(self.y)
        if compass == 'left':
            self.sprite_x -= 1
            self.x = self.sprite_x * SIZE_SPRITE
            print("left")
            print(self.x)
            print(self.sprite_x)
        if compass == 'right':
            self.sprite_x += 1
            self.x = self.sprite_x * SIZE_SPRITE
            print("right")
            print(self.x)
            print(self.sprite_x)