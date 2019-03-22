
import pygame
from constant import *


class Macgyver:
    """ Class Hero """
    def __init__(self, spx, spy, mac, matrix):
        MAC_G = MAC
        self.sprite_x = spx
        self.sprite_y = spy
        self.x = self.sprite_x * SIZE_SPRITE
        self.y = self.sprite_y * SIZE_SPRITE
        self.mac = MAC_G
        self.matrix = matrix

    def image_hero(self, mac):
        MAC_G = pygame.image.load(MAC).convert_alpha()
        MAC_G = MAC_G.subsurface(0, 0, 32, 32)
        MAC_G = pygame.transform.scale(MAC_G, (SIZE_SPRITE, SIZE_SPRITE))
        self.mac = MAC_G

    def position(self, compass):
        """ Function to move the hero """
        if compass == 'down':
            if self.sprite_y < NB_SP_H - 1:
                if self.matrix.area[self.sprite_y+1][self.sprite_x] != "M":
                    self.sprite_y += 1
                    self.y = self.sprite_y * SIZE_SPRITE
        if compass == 'up':
            if self.y > 0:
                if self.matrix.area[self.sprite_y-1][self.sprite_x] != "M":
                    self.sprite_y -= 1
                    self.y = self.sprite_y * SIZE_SPRITE
        if compass == 'left':
            if self.x > 0:
                if self.matrix.area[self.sprite_y][self.sprite_x-1] != "M":
                    self.sprite_x -= 1
                    self.x = self.sprite_x * SIZE_SPRITE
        if compass == 'right':
            if self.sprite_x < NB_SP_H - 1:
                if self.matrix.area[self.sprite_y][self.sprite_x+1] != "M":
                    self.sprite_x += 1
                    self.x = self.sprite_x * SIZE_SPRITE