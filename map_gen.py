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
        self.platforms = []
        self.x = 0
        self.y = 0

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
            "#000000",
            settings.BLK_SIZE,
            settings.BLK_SIZE
        )

    def draw(self, offset):

        for self.y in range(settings.WIN_HEIGHT // settings.BLK_SIZE):
            for self.x in range(settings.WIN_WIDTH // settings.BLK_SIZE):
                self.screen.blit(
                        self.background,
                        (self.x * settings.BLK_SIZE, self.y * settings.BLK_SIZE)
                    )
        for entity in self.entities:
            self.screen.blit(entity.image, offset(entity))



    def build(self, players, npcs):
        # build the level

        for row_number, row in enumerate(self.level):
            for col_number, col in enumerate(row):
                if col == "P":
                    p = game_objects.Platform(self.x, self.y)
                    self.platforms.append(p)
                    self.entities.add(p)

                if col == "E":
                    e = game_objects.ExitBlock(self.x, self.y)
                    self.platforms.append(e)
                    self.entities.add(e)

                if col == "C":
                    player = characters.Player(self.x, self.y)
                    self.entities.add(player)
                    players.append(player)

                if col == "N":
                    npc = characters.NonPlayer(self.x, self.y)
                    self.entities.add(npc)
                    npcs.append(npc)

                self.x += settings.BLK_SIZE
            self.y += settings.BLK_SIZE
            self.x = 0
