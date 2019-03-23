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
    window = pygame.display.set_mode(AREA)
    maze = Maze()
    maze.create_area()
    maze.generate_area(window)
    items = item()
    items.create_item(maze)
    items.generate_item(window)
    hero = Macgyver(INIT_MAC_X, INIT_MAC_Y, MAC, maze)
    hero.image_hero(MAC)
    guard = Guardian(GUARDIAN, maze)
    guard.generate_guardian(window)

    return window, maze, items, hero, guard

def move_player(hero):
	for event in pygame.event.get():
		if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
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

def rebuild_windows(maze, guard, items, window):
	maze.generate_area(window)
	guard.generate_guardian(window)
	items.generate_item(window)
	items.display_serynge(window)

def management_interaction(maze, window, meet, hero, items, meetGuard):
	meet.meet_item(hero, items)
	window.blit(hero.mac, (hero.x, hero.y))
	meet.meet_gardian(hero, items)

def main():
	""" running the game """
	pygame.init()
	init_window()
	""" pygame initialyse loop home """ 
	game = True
	player_ready = False
	while game:
		pygame.display.flip()
		""" speed management loop """
		pygame.time.Clock().tick(30)
		for event in pygame.event.get():
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				game = False
			elif event.type == KEYDOWN:
				if event.key == K_s:
					player_ready = True
					(window, maze, items, hero, guard) = init_game()

		""" Game loop """
		while player_ready:
			""" Move player """
			move_player(hero)
			""" Rebuild windows after move """
			rebuild_windows(maze, guard, items, window)
			""" Interaction """
			meet = interaction(maze, window)
			meetGuard = meet.meet_gardian(hero, items)
			management_interaction(maze, window, meet, hero, items, meetGuard)
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
			
			pygame.display.flip()

if __name__ == "__main__":
    main()