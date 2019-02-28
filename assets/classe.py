
import os
import csv
import pygame
from constant import *

class Maze:
    def __init__(self):
        """creation of labyrinth from a csv file"""
        self.area = self.creation_area()

    def creation_area(data_file):
        """ create a list to represent the structure """
        directory = os.path.dirname(__file__)
        path_to_file = os.path.join(directory, "map", data_file)
        structure_area = []
        with open(path_to_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                structure_area.append(row)
        return structure_area

    def generate_area(self, windows):
        """ nous allons appliquer une image à chaque sprite de la structure """
        wall = pygame.image.load(c_wall).convert_alpha()
        flor = pygame.image.load(c_flor).convert()
        line = 0
        for line in self.area:
            num_sprite = 0
            for sprite in line:
                x = num_case * size_sprite
                y = num_line * size_sprite
                if sprite == 'M':
                    window.blit(wall, (x, y))
                else:
                    window.blit(flor, (x, y))
                num_sprite += 1
            line += 1






def main():
    pass

if __name__ == "__main__":
    main()
