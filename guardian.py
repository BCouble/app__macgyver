
import pygame
from constant import *

class Guardian:
    """Create Guardian"""
    def __init__(self, guard, matrix):
        GUARD = GUARDIAN
        self.matrix = matrix

    def generate_guardian(self, window):
        GUARD = pygame.image.load(GUARDIAN).convert_alpha()
        GUARD = pygame.transform.scale(GUARD, (SIZE_SPRITE, SIZE_SPRITE))
        window.blit(GUARD, (POS_GUARD, POS_GUARD))