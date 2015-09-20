import settings
import characters
import game_objects
import pygame

##############################################################################
# Map
# contains text map
# method to build the map out of platforms
# method to redraw map
##############################################################################
class Map(object):
    def __init__(self, level):
        self.level = level

        self.entities = pygame.sprite.Group()

        # TODO mode map into separate files
        self.width  = len(self.level[0])*settings.BLK_SIZE
        self.height = len(self.level)*settings.BLK_SIZE
        self.screen = pygame.display.set_mode(
            settings.DISPLAY,
            settings.FLAGS,
            settings.DEPTH
        )
        self.background = game_objects.Background(
            settings.BACKGROUND_COLOR,
            settings.BLK_SIZE,
            settings.BLK_SIZE
        )


    def draw(self, offset):
        for y in range(settings.WIN_HEIGHT // settings.BLK_SIZE):
            for x in range(settings.WIN_WIDTH // settings.BLK_SIZE):
                self.screen.blit(
                        self.background,
                        (x * settings.BLK_SIZE, y * settings.BLK_SIZE)
                    )
        for entity in self.entities:
            self.screen.blit(entity.image, offset(entity))



    def build(self):
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
                    characters.player.set_pos(x, y)
                    characters.player.set_color(settings.CHARACTER_COLOR)
                    self.entities.add(characters.player)

                if col == "N":
                    npc = characters.NonPlayer(
                        x,
                        y,
                        settings.NPC_COLOR
                    )
                    self.entities.add(npc)
                    characters.npcs.append(npc)

                x += settings.BLK_SIZE
            y += settings.BLK_SIZE
            x = 0

            for entity in self.entities:
                entity.image.convert()
