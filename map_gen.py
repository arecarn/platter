import settings
import game_objects

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
        # TODO mode map into separate files
        self.width  = len(self.level[0])*settings.BLK_SIZE
        self.height = len(self.level)*settings.BLK_SIZE

    def draw(self, screen, background):
        for self.y in range(settings.WIN_HEIGHT//settings.BLK_SIZE):
            for self.x in range(settings.WIN_WIDTH//settings.BLK_SIZE):
                screen.blit(background, (self.x * settings.BLK_SIZE, self.y * settings.BLK_SIZE))

    def build(self, entities):
        # build the level
        for row in self.level:
            for col in row:
                if col == "P":
                    p = game_objects.Platform(self.x, self.y)
                    self.platforms.append(p)
                    entities.add(p)
                if col == "E":
                    e = game_objects.ExitBlock(self.x, self.y)
                    self.platforms.append(e)
                    entities.add(e)
                self.x += settings.BLK_SIZE
            self.y += settings.BLK_SIZE
            self.x = 0
