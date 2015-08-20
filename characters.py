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
        super().__init__()
        self.x_velocity = 0
        self.y_velocity = 0
        self.onGround = False
        self.speed = speed
        self.jump = jump

        dimension = size * settings.BLK_SIZE

        self.image = pygame.Surface((dimension, dimension))
        self.image.fill(pygame.Color(color))
        self.image.convert()
        self.rect = pygame.Rect(x, y, dimension, dimension)

        self.status = {
                'up'      : False,
                'down'    : False,
                'right'   : False,
                'left'    : False,
                'running' : False
        }

    def updateLocation(self, platforms):
        if self.status['up']:
            if self.onGround: 
                self.y_velocity -= self.jump * 10

        if self.status['down']:
            pass

        if self.status['running']:
            self.x_velocity = self.speed * settings.BLK_SIZE/2.66

        if self.status['left']:
            self.x_velocity = self.speed * -settings.BLK_SIZE/4

        if self.status['right']:
            self.x_velocity = self.speed * settings.BLK_SIZE/4

        if not self.onGround:                 # accelerate w/ gravity if in air
            self.y_velocity += settings.BLK_SIZE/106.66      # max falling speed
            if self.y_velocity > settings.BLK_SIZE*3: self.y_velocity = settings.BLK_SIZE*3

        if not(self.status['left'] or self.status['right']):
            self.x_velocity = 0

        self.rect.left += self.x_velocity           # increment in x direction
        self.collide(self.x_velocity, 0, platforms) # do x-axis collisions

        self.rect.top += self.y_velocity            # increment in y direction
        self.onGround = False;                      # assuming we're in the air
        self.collide(0, self.y_velocity, platforms) # do y-axis collisions

    def collide(self, x_velocity, y_velocity, platforms):
        for platform in platforms:
            if pygame.sprite.collide_rect(self, platform):

                if isinstance(platform, game_objects.ExitBlock):
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

                if x_velocity > 0:
                    self.rect.right = platform.rect.left # print "collide right"

                if x_velocity < 0:
                    self.rect.left = platform.rect.right # print "collide left"

                if y_velocity > 0:
                    self.rect.bottom = platform.rect.top
                    self.onGround = True
                    self.y_velocity = 0

                if y_velocity < 0:
                    self.rect.top = platform.rect.bottom

##############################################################################
# Player
##############################################################################
class Player(_Character):
    def __init__(self, x, y, color):
        super().__init__(
            x,
            y,
            size = 1,
            color = color,
            speed = 1,
            jump = 1
        )

##############################################################################
# NonPlayer
##############################################################################
class NonPlayer(_Character):
    def __init__(self, x, y, color):
        super().__init__(
            x,
            y,
            size = 2,
            color = color,
            speed = 0.25,
            jump = 0.8
        )

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
