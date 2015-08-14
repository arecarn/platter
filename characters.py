import pygame
import entity
import settings
import game_objects

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
class _Character(entity.Entity):
    def __init__(self, x, y, size, color, speed, jump):
        entity.Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.speed = speed
        self.jump = jump

        dimension = size * settings.BLK_SIZE

        self.image = pygame.Surface((dimension,dimension))
        self.image.fill(pygame.Color(color))
        self.image.convert()
        self.rect = pygame.Rect(x, y, dimension, dimension)

        self.status = {
                'up' : False,
                'down' : False,
                'right' : False,
                'left' : False,
                'running' : False
                }

    def updateLocation(self, platforms):
        if self.status['up']: # only jump if on the ground
            if self.onGround: self.yvel -= self.jump * 10
        if self.status['down']:
            pass
        if self.status['running']:
            self.xvel = self.speed * settings.BLK_SIZE/2.66
        if self.status['left']:
            self.xvel = self.speed * -settings.BLK_SIZE/4
        if self.status['right']:
            self.xvel = self.speed * settings.BLK_SIZE/4
        if not self.onGround:                 # accelerate w/ gravity if in air
            self.yvel += settings.BLK_SIZE/106.66      # max falling speed
            if self.yvel > settings.BLK_SIZE*3: self.yvel = settings.BLK_SIZE*3
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
                if isinstance(p, game_objects.ExitBlock):
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
# Player
##############################################################################
class Player(_Character):
    def __init__(self, x, y):
        super().__init__(x, y, 1,  "#0000FF", 1 , 1)

##############################################################################
# NonPlayer
##############################################################################
class NonPlayer(_Character):
    def __init__(self, x, y):
        speed = 0.25
        jump = 1
        size = 3
        color = "#FF0000"
        super().__init__(x, y, size,  color, speed , jump)

    def follow(self, target):

        target_x , target_y = target.rect.center
        x , y = self.rect.center

        if target_x < x: #t   n tpos < npos to the left of npc
            self.status["right"] = False
            self.status["left"] = True

        if target_x > x : #n   t tpos > npos: to the right of npc
            self.status["right"] = True
            self.status["left"] = False

        if  target_x == x:  # don't move when x is inline x_targ
            self.status["right"] = False
            self.status["left"] = False

        if target_y < y: #above
            self.status["up"] = True

        if target_y > y: #bellow
            self.status["up"] = False

        if target_y == y: # same level
            self.status["up"] = False
