#! /usr/bin/env python3
# coding: utf-8

"""
Project 3
Maze game Mac Gyver 
"""
import pygame
import constant
from classe import *

def main():

	pygame.init()
	window = pygame.display.set_mode(c_window)
	maze = Maze()
	maze.generate_area(window)
	hero = Macgyver()
	hero.image()
	#position_hero = hero.get_rect()
	#window.blit(hero, init_hero)
	pygame.display.flip()
    
if __name__ == "__main__":
    main()
