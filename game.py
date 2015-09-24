import pygame
import settings
import game_objects

import camera
import characters
import level

class Game(object):
    def __init__(self, level):
        self.level = level

        self.entities = pygame.sprite.Group()
        self.npcs = pygame.sprite.Group()
        self.player = None

        self.width  = len(self.level[0])*settings.BLK_SIZE
        self.height = len(self.level)*settings.BLK_SIZE

        self.camera = camera.Camera(self.width, self.height)

        self.build_level()

    def build_level(self):
        x = 0
        y = 0

        for row_number, row in enumerate(self.level):
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

    def update_camera(self):
        self.camera.update(self.player)
