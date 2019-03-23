
import pygame
from constant import *

class interaction():
    """ Movement and object management """
    def __init__(self, matrix, window):
        screen = ''
        self.matrix = matrix
        self.window = window
        self.screen = screen

    def meet_gardian(self, hero, item):
        self.hero = hero
        self.item = item
        if hero.x == POS_GUARD and hero.y == POS_GUARD:
            if self.item.inventory == 3:
                screen = WINNER
            else:
                screen = LOOSER
            return screen

    def meet_item(self, hero, obj):
        inventory = []
        self.hero = hero
        self.obj = obj
        num_item = 0
        for line in self.obj.obj:
            if hero.sprite_x == self.obj.obj[num_item][2]:
                if hero.sprite_y == self.obj.obj[num_item][3]:
                    self.obj.obj[num_item][4] = 1
            num_item += 1

    def game_over(self, screen):
        self.screen = screen
        window = pygame.display.set_mode(AREA)
        gameover = pygame.image.load(screen)
        gameover = pygame.transform.scale(gameover, (X_WINDOW, Y_WINDOW))
        window.blit(gameover, (0, 0))