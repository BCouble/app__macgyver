#! /usr/bin/env python3
# coding: utf-8

"""
Project 3
Maze game Mac Gyver 
"""
import pygame
import constant
from classe import *
from pygame.locals import *

def main():
	""" running the game """
	pygame.init()
	

	game = True

	while game:
                # Init windows
		window = pygame.display.set_mode(AREA)
		# Creation of Maze
		maze = Maze()
		maze.creation_area()
		maze.generate_area(window)
		# Creation of MacGyver
		hero = Macgyver(c_macx, c_macy, MAC, maze)
		# Update image
		hero.image_hero(MAC)
		window.blit(hero.mac, (hero.sprite_x, hero.sprite_y))
		# appel des attributs
		#window.blit(hero.mac, (hero.x, hero.y))
		#pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					hero.position('down')
				if event.key == pygame.K_UP:
					hero.position('up')
				if event.key == pygame.K_LEFT:
					hero.position('left')
				if event.key == pygame.K_RIGHT:
					hero.position('right')
		#hero.position()
		#position_mac = hero.get_rect() 
		#window.blit(hero.position, (hero.sprite_x, hero.sprite_y))
		pygame.display.flip()
    
if __name__ == "__main__":
    main()

