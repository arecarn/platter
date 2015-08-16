import pygame

import entity
import settings

##############################################################################
# Platform
# surfaces that make up the games terrain
##############################################################################
class Platform(entity.Entity):
    def __init__(self, x, y):
        entity.Entity.__init__(self)
        self.image = pygame.Surface((settings.BLK_SIZE, settings.BLK_SIZE))
        self.image.convert()
        self.image.fill(pygame.Color("#DDDDDD"))
        self.rect = pygame.Rect(x, y, settings.BLK_SIZE, settings.BLK_SIZE)
        self.rect = pygame.Rect(x, y, settings.BLK_SIZE, settings.BLK_SIZE)
    def update(self):
        pass

##############################################################################
# Exitblock
# surface when touched ends the game
##############################################################################
class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(pygame.Color("#C0C0C0"))

##############################################################################
# Background
##############################################################################
class Background(pygame.Surface):
    def __init__(self, color, width, height):
       pygame.Surface.__init__(self, (width, height))
       self.convert()
       self.fill(pygame.Color(color))
