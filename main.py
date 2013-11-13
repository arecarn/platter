import pygame
from pygame import *

WIN_WIDTH = 800
WIN_HEIGHT = int(WIN_WIDTH / 1.25)
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)
BLK_SIZE = 32

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0
CAMERA_SLACK = 30

class Debug(object):
    enable = False 
    def printHeader(self, txt):
        if self.enable:
            print '=' * 80
            print txt
            print '-' * 80
    def printMsg(self, txt):
        if self.enable:
            print txt
debug = Debug()
debug.enable = True


##############################################################################
# Main 
# Includes initialization, and the main game loop
##############################################################################
def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Use arrows to move!")
    timer = pygame.time.Clock()
    entities = pygame.sprite.Group()
    map = Map()
    map.build(entities)
    action = Action()

    # TODO: move this to it's own class?
    bg = Background("#000000", BLK_SIZE, BLK_SIZE)

    player = Player(BLK_SIZE, BLK_SIZE)
    camera = Camera(map.width, map.height)
    entities.add(player)
    while 1:
        timer.tick(60)

        action.check(player.status) # check for events

        map.draw(screen, bg)

        camera.update(player) # update player camera TODO needs better discription
        player.updateLocation(map.platforms) 

        # draw everything with offset
        for e in entities:
            screen.blit(e.image, camera.apply(e)) # update entities with of set Camera
        pygame.display.update()

##############################################################################
# Camera
# keep scroll on the map following a target sprite
##############################################################################
class Camera(object):
    def __init__(self, width, height):
        self.state = Rect(0, 0, width, height)
    # provide the offset for each block
    def apply(self, target):
        return target.rect.move(self.state.topleft)
    def update(self, target):
        self.state = self.complex_camera(self.state, target.rect)

    #TODO: integrate into class
    def simple_camera(self, camera, target_rect):
        l, t, _, _ = target_rect # left , top position
        # _, _, w, h = camera # width, height of camera
        w = WIN_WIDTH
        h = WIN_HEIGHT
        # center the camera on the target 
        return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)

    #TODO: integrate into class
    def complex_camera(self, camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera
        l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h

        l = min(0, l)                           # stop scrolling at the left edge
        l = max(-(camera.width-WIN_WIDTH), l)   # stop scrolling at the right edge
        t = max(-(camera.height-WIN_HEIGHT), t) # stop scrolling at the bottom
        t = min(0, t)                           # stop scrolling at the top
        return Rect(l, t, w, h)

##############################################################################
# Map
# contains text map 
# method to build the map out of platforms
# method to redraw map
##############################################################################
class Map(object):
    def __init__(self):
        self.platforms = []
        self.x = 0
        self.y = 0
        # TODO mode map into separate files
        self.level = [
                "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
                "P                                                                                    P",
                "P                                                                                    P",
                "P                           E                                        E               P",
                "P                     PPPPPPPPPPP                              PPPPPPPPPPP           P",
                "P                                                                                    P",
                "P                                                                                    P",
                "P                                                                                    P",
                "P     PPPPPPPP                                 PPPPPPPP                              P",
                "P                                                                                    P",
                "P                           PPPPPPP                                  PPPPPPP         P",
                "P                  PPPPPP                                   PPPPPP                   P",
                "P                                                                                    P",
                "P          PPPPPPP                                  PPPPPPP                          P",
                "P                                                                                    P",
                "P                      PPPPPP                                   PPPPPP               P",
                "P                                                                                    P",
                "P    PPPPPPPPPPP                              PPPPPPPPPPP                            P",
                "P                                                                                    P",
                "P                     PPPPPPP                                  PPPPPPP               P",
                "P                                                                                    P",
                "P                  PPPPPPPPPPP                              PPPPPPPPPPP              P",
                "P                                                                                    P",
                "P                                                                                    P",
                "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
                ]
        self.width  = len(self.level[0])*BLK_SIZE
        self.height = len(self.level)*BLK_SIZE

    def draw(self, screen, background):
        for self.y in range(WIN_HEIGHT/BLK_SIZE):
            for self.x in range(WIN_WIDTH/BLK_SIZE):
                screen.blit(background, (self.x * BLK_SIZE, self.y * BLK_SIZE))

    def build(self, entities):
        # build the level
        for row in self.level:
            for col in row:
                if col == "P":
                    p = Platform(self.x, self.y)
                    self.platforms.append(p)
                    entities.add(p)
                if col == "E":
                    e = ExitBlock(self.x, self.y)
                    self.platforms.append(e)
                    entities.add(e)
                self.x += BLK_SIZE
            self.y += BLK_SIZE
            self.x = 0

##############################################################################
# Action
# Handles keyboard events/ especially movment
##############################################################################
class Action(object):


    def check(self, status):
            # check for keys and handle movement
        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit, "QUIT"

            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit, "ESCAPE"
            if e.type == KEYDOWN and (e.key == K_UP or e.key == K_j):
                status['up'] = True
                debug.printMsg('action is up')
            if e.type == KEYDOWN and e.key == K_DOWN:
                status['down'] = True
                debug.printMsg('action is down')
            if e.type == KEYDOWN and e.key == K_LEFT:
                status['left'] = True
                debug.printMsg('action is left')
            if e.type == KEYDOWN and e.key == K_RIGHT:
                status['right'] = True
                debug.printMsg('action is right')
            if e.type == KEYDOWN and e.key == K_SPACE:
                status['running'] = True
                debug.printMsg('action is running')
            if e.type == KEYUP and e.key == K_UP:
                status['up'] = False
            if e.type == KEYUP and e.key == K_DOWN:
                status['down'] = False
            if e.type == KEYUP and e.key == K_RIGHT:
                status['right'] = False
            if e.type == KEYUP and e.key == K_LEFT:
                status['left'] = False
            if e.type == KEYUP and e.key == K_RIGHT:
                status['right'] = False

##############################################################################
# Entity
# create a sprite
##############################################################################
class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

##############################################################################
# Character
# TODO 
# Variables:
# size
# health

# color
# image
#
# speed
# jump 
##############################################################################
class Character(Entity):
    def __init__(self, x, y, size, color, speed, jump):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.speed = speed
        self.jump = jump

        dimension = size * BLK_SIZE

        self.image = Surface((dimension,dimension))
        self.image.fill(Color(color))
        self.image.convert()
        self.rect = Rect(x, y, dimension, dimension)

        self.status = {
                'up' : False,
                'down' : False,
                'right' : False,
                'left' : False,
                'running' : False
                }

    def updateLocation(self, platforms):
        if self.status['up']:                     # only jump if on the ground
            if self.onGround: self.yvel -= self.jump * 10
        if self.status['down']:
            pass
        if self.status['running']:
            self.xvel = self.speed * BLK_SIZE/2.66
        if self.status['left']:
            self.xvel = self.speed * -BLK_SIZE/4
        if self.status['right']:
            self.xvel = self.speed * BLK_SIZE/4
        if not self.onGround:                 # accelerate w/ gravity if in air
            self.yvel += BLK_SIZE/106.66      # max falling speed
            if self.yvel > BLK_SIZE*3: self.yvel = BLK_SIZE*3
        if not(self.status['left'] or self.status['right']):
            self.xvel = 0
        self.rect.left += self.xvel           # increment in x direction
        self.collide(self.xvel, 0, platforms) # do x-axis collisions
        self.rect.top += self.yvel            # increment in y direction
        self.onGround = False;                # assuming we're in the air
        self.collide(0, self.yvel, platforms) # do y-axis collisions

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left # print "collide right"
                if xvel < 0:
                    self.rect.left = p.rect.right # print "collide left"
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom

##############################################################################
# NonPlayer
# TODO create AI
# a
##############################################################################
class NonPlayer(Character):
    def __init__(self, x, y):
        Character.__init__(self, x, y, 1,  "#FF0000", 1 , 1)
        

##############################################################################
# Player
##############################################################################
class Player(Character):
    def __init__(self, x, y):
        Character.__init__(self, x, y, 1,  "#0000FF", 1 , 1)
        

##############################################################################
# Platform 
# surfaces that make up the games terrain
##############################################################################
class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((BLK_SIZE, BLK_SIZE))
        self.image.convert()
        self.image.fill(Color("#DDDDDD"))
        self.rect = Rect(x, y, BLK_SIZE, BLK_SIZE)
    def update(self):
        pass

##############################################################################
# Exitblock 
# surface when touched ends the game
##############################################################################
class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#C0C0C0"))

##############################################################################
# Background
##############################################################################
class Background(Surface):
    def __init__(self, color, width, height):
       Surface.__init__(self, (width, height)) 
       self.convert()
       self.fill(Color(color))

##############################################################################
# This runs main once every other function is defined
# this must last.
##############################################################################
if __name__ == "__main__":
    main()
