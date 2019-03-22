#! /usr/bin/env python3
# coding: utf-8

"""
Project 3
Maze game Mac Gyver 
"""
import pygame
import constant
from item import *
from maze import *
from interaction import *
from macgyver import *
from guardian import *
from pygame.locals import *

def init_window():
    window = pygame.display.set_mode(AREA)
    start = pygame.image.load(START).convert_alpha()
    start = pygame.transform.scale(start, (X_WINDOW, Y_WINDOW))
    window.blit(start, (0, 0))

def init_game():
    # Init windows
    window = pygame.display.set_mode(AREA)
    # Creation of Maze
    maze = Maze()
    maze.create_area()
    maze.generate_area(window)
    # Items
    items = item()
    items.create_item(maze)
    #items.inventory()
    items.generate_item(window)
    # Creation of MacGyver
    hero = Macgyver(INIT_MAC_X, INIT_MAC_Y, MAC, maze)
    # Update image
    hero.image_hero(MAC)
    # Creation Guard
    guard = Guardian(GUARDIAN, maze)
    guard.generate_guardian(window)

    return window, maze, items, hero, guard

def main():
	""" running the game """
	pygame.init()
	# 1 on lance le jeu
	init_window()
	# pygame loop home 
	game = True
	player_ready = False
	while game:
		pygame.display.flip()
		# speed management loop
		pygame.time.Clock().tick(30)
		for event in pygame.event.get():
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				game = False
			elif event.type == KEYDOWN:
				if event.key == K_s:
					player_ready = True
					(window, maze, items, hero, guard) = init_game()

		# 2 La partie démarre
		while player_ready:
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
			# Rebuild windows
			maze.generate_area(window)
			# Guard
			guard.generate_guardian(window)
			# update loot avec invmac
			items.generate_item(window)
			items.display_serynge(window)
			# interaction
			meet = interaction(maze, window)
			meet.meet_item(hero, items)
			meet.meet_gardian(hero, items)
			meetGuard = meet.meet_gardian(hero, items)
			if meetGuard != None:
				meet.game_over(meetGuard)
				for event in pygame.event.get():
					if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
						game = False
					elif event.type == KEYDOWN:
						if event.key == K_s:
							game = True
							player_ready = False
							init_window()
			window.blit(hero.mac, (hero.x, hero.y))
			pygame.display.flip()
if __name__ == "__main__":
    main()