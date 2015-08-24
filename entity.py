import pygame
import settings

##############################################################################
# Entity
# create a sprite
##############################################################################
class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((settings.BLK_SIZE, settings.BLK_SIZE))
        self.image.fill(pygame.Color(color))
        self.rect = pygame.Rect(x, y, settings.BLK_SIZE, settings.BLK_SIZE)

    def set_pos(self, x, y):
        self.rect.top = y
        self.rect.right = x

    def set_color(self, color):
        self.image.fill(pygame.Color(color))

