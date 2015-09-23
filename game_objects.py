import pygame
import entity

class Platform(entity.Entity):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

class ExitBlock(Platform):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)


