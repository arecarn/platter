import pygame
import entity
import settings
import game_objects

class Character(entity.Entity):
    def __init__(self, x, y, size, color, speed, jump):
        entity.Entity.__init__(self, x, y, color)

        self.x_velocity = 0
        self.y_velocity = 0
        self.onGround = False
        self.speed = speed
        self.jump = jump

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
                self.y_velocity -= self.jump * settings.CHARACTER_JUMP_SPEED

        if self.status['down']:
            pass

        if self.status['left']:
            self.x_velocity = self.speed * -settings.CHARACTER_WALK_SPEED

        if self.status['right']:
            self.x_velocity = self.speed * settings.CHARACTER_WALK_SPEED

        if self.status['running']:
            self.x_velocity = self.x_velocity * 3

        if not self.onGround:
            self.y_velocity += settings.FALLING_ACCELERATION
            if self.y_velocity > settings.TERMINAL_VELOCITY:
                self.y_velocity = settings.TERMINAL_VELOCITY

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
                    self.y_velocity = 0

class Player(Character):
    def __init__(self, x, y, color):
        Character.__init__(
            self,
            x,
            y,
            size = 1,
            color = color,
            speed = 1,
            jump = 1
        )

    def go_up(self):
        self.status['up'] = True

    def stop_go_up(self):
        self.status['up'] = False

    def go_down(self) :
        self.status['down'] = True

    def stop_go_down(self) :
        self.status['down'] = False

    def go_left(self):
        self.status['left'] = True

    def stop_go_left(self):
        self.status['left'] = False

    def go_right(self):
        self.status['right'] = True

    def stop_go_right(self):
        self.status['right'] = False

    def run(self):
        self.status['running'] = True

    def stop_run(self):
        player.status['running'] = False


player = Player(0 , 0 , settings.CHARACTER_COLOR)

class NonPlayer(Character):
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

