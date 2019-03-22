
import os
import csv
import pygame
from constant import *

class Maze:
    def __init__(self):
        """ creation of labyrinth from a csv file """
        self.structure = MAZE
        self.area = []

    def create_area(self):
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