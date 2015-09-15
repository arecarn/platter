import pygame
import entity

class Platform(entity.Entity):
    def __init__(self, x, y, color):
        entity.Entity.__init__(self, x, y, color)

class ExitBlock(Platform):
    def __init__(self, x, y, color):
        Platform.__init__(self, x, y, color)

class Background(pygame.Surface):
    def __init__(self, color, width, height):
       pygame.Surface.__init__(self, (width, height))
       self.convert()
       self.fill(pygame.Color(color))

