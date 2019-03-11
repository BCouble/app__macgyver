    game = True

    while game:
        for event in pygame.event.get():
            if event.type == QUIT:
                game = False
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                if event.key == K_UP:
                if event.key == K_LEFT:
                if event.key == K_RIGHT:

class Macgyver:
    """ Class Hero """
    def __init__(self):
        # position/sprite 
        self.macgyver = ()
        #self.Macgyver = (MAC(X, Y))

    def image_hero(self):
        MAC_G = pygame.image.load(MAC).convert_alpha()
        self.macgyver.append(MAC_G)

    def position(self):
        x = 3
        y = 40
        position = (x, y)
        return self.macgyver.append(position)

    def lire(self):
        print(self.macgyver)

            # Update image
            hero.image_hero(MAC)
            window.blit(hero.mac, (hero.sprite_x, hero.sprite_y))
            # appel des attributs
            #window.blit(hero.mac, (hero.x, hero.y))
            #pygame.display.flip()


def main():
    """ running the game """
    pygame.init()
    # Init windows
    window = pygame.display.set_mode(AREA)

    game = True

    while game:
        player_ready = True
        continue_game = True
        print("While game")
        while player_ready:
            # Load screen start
            START = "assets/image/tile-crusader-logo.png"
            START = pygame.image.load(START).convert()
            window.blit(START, (0, 0))
            pygame.display.flip()
            print("player_ready")
            # loop event player ready
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    player_ready = 0
                    continue_game = False
                    game = False
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        continue_game = True
                        player_ready = 0

            if player_ready == 0:
                # Creation of the Maze and display it
                maze = Maze()
                maze.creation_area()
                maze.generate_area(window)
                # Creation of MacGyver
                hero = Macgyver(c_macx, c_macy, MAC, maze)
            
            # Loop Game
            while continue_game:
                print("continue_game")
                pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    continue_game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        hero.position('down')
                    if event.key == pygame.K_UP:
                        hero.position('up')
                    if event.key == pygame.K_LEFT:
                        hero.position('left')
                    if event.key == pygame.K_RIGHT:
                        hero.position('right')

            # Rebuild
            if continue_game:
                maze.generate_area(window)
                window.blit(hero.position, (hero.sprite_x, hero.sprite_y))
            #hero.position()
            #position_mac = hero.get_rect() 
            #window.blit(hero.position, (hero.sprite_x, hero.sprite_y))
            pygame.display.flip()
    
if __name__ == "__main__":
    main()





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
    # Init windows
    window = pygame.display.set_mode(AREA)

    game = True

    while game:
        player_ready = True
        continue_game = True
        print("While game")
        while player_ready:
            # Load screen start
            START = "assets/image/tile-crusader-logo.png"
            START = pygame.image.load(START).convert()
            window.blit(START, (0, 0))
            pygame.display.flip()
            print("player_ready")
            # loop event player ready
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    player_ready = False
                    continue_game = False
                    game = False
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        continue_game = True
                        player_ready = True

            if player_ready == True:
                # Creation of the Maze and display it
                maze = Maze()
                maze.creation_area()
                maze.generate_area(window)
                # Creation of MacGyver
                hero = Macgyver(c_macx, c_macy, MAC, maze)
            
            # Loop Game
            while continue_game:
                print("continue_game")
                pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    continue_game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        hero.position('down')
                    if event.key == pygame.K_UP:
                        hero.position('up')
                    if event.key == pygame.K_LEFT:
                        hero.position('left')
                    if event.key == pygame.K_RIGHT:
                        hero.position('right')

            # Rebuild
            if continue_game:
                maze.generate_area(window)
                window.blit(hero.position, (hero.sprite_x, hero.sprite_y))
            #hero.position()
            #position_mac = hero.get_rect() 
            #window.blit(hero.position, (hero.sprite_x, hero.sprite_y))
            pygame.display.flip()
    
if __name__ == "__main__":
    main()

