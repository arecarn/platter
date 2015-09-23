import pygame
import settings
import game_objects

import camera
import characters
import level

Player = None

##############################################################################
# Map
# contains text map
# method to build the map out of platforms
# method to redraw map
##############################################################################
class Game(object):
    def __init__(self):
        self.entities = pygame.sprite.Group()
        self.npcs = pygame.sprite.Group()



        self.width = 0
        self.height = 0
        self.camera = None

    def update(self):
        self.camera.update(self.player)
        settings.BACKGROUND.update()

        for entity in self.entities:
            entity.update(self.entities, self.camera.apply)

    def build(self, level):
        self.width  = len(level[0])*settings.BLK_SIZE
        self.height = len(level)*settings.BLK_SIZE
        self.camera = camera.Camera(self.width, self.height)

        x = 0
        y = 0

        for row_number, row in enumerate(level):
            for col_number, col in enumerate(row):

                if col == "P":
                    platform = game_objects.Platform(
                        x,
                        y,
                        settings.PLATFORM_COLOR
                    )
                    self.entities.add(platform)

                if col == "E":
                    exit_block = game_objects.ExitBlock(
                        x,
                        y,
                        settings.EXIT_BLOCK_COLOR
                    )
                    self.entities.add(exit_block)

                if col == "C":
                    self.player = characters.Player(x, y, settings.CHARACTER_COLOR)
                    Player = self.player
                    self.entities.add(self.player)

                if col == "N":
                    npc = characters.NonPlayer(
                        x,
                        y,
                        settings.NPC_COLOR
                    )
                    self.entities.add(npc)
                    self.npcs.add(npc)

                x += settings.BLK_SIZE
            y += settings.BLK_SIZE
            x = 0

            for entity in self.entities:
                entity.image.convert()



game = Game()
game.build(level._1)

def getActiveGamer():
    return game
