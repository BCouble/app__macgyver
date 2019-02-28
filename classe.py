
import os
import csv
import pygame
from constant import *

class Maze:
    def __init__(self):
        """creation of labyrinth from a csv file"""
        self.structure = c_maze
        self.area = self.creation_area()

    def creation_area(self):
        """ create a list to represent the structure """
        structure_area = []
        with open(self.structure, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                structure_area.append(row)
        return structure_area

    def generate_area(self, window):
        """ nous allons appliquer une image à chaque sprite de la structure """
        wall = pygame.image.load(c_texture).convert_alpha()
        wall = wall.subsurface(0, 0, 20, 20)
        wall = pygame.transform.scale(wall, (size_sprite, size_sprite))
        path = pygame.image.load(c_texture).convert()
        path = path.subsurface(20, 20, 20, 20)
        path = pygame.transform.scale(path, (size_sprite, size_sprite))
        start = pygame.image.load(c_texture).convert()
        start = start.subsurface(160, 20, 20, 20)
        start = pygame.transform.scale(start, (size_sprite, size_sprite))
        num_line = 0
        for line in self.area:
            num_sprite = 0
            for sprite in line:
                x = num_sprite * size_sprite
                y = num_line * size_sprite
                if sprite == 'M':
                    window.blit(wall, (x, y))
                elif sprite == 'D':
                    init_hero = (x, y)
                    window.blit(start, (x, y))
                elif sprite == 'G':
                    window.blit(start, (x, y))
                else:
                    window.blit(path, (x, y))
                num_sprite += 1
            num_line += 1

class Macgyver:

    def __init__(self):
        # position/sprite
        # image
        self.icon = self.image()
        self.sprite = self.position()

    def image(self):
        mac = pygame.image.load(c_mac).convert_alpha()
        mac = pygame.transform.scale(mac, (size_sprite, size_sprite))

    def position(self, x, y):
        pass