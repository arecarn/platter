import pygame
import entity
import settings
import game_objects


class Character(entity.Entity):
    def __init__(
        self,
        x,
        y,
        size,
        color,
        speed,
        jump
    ):
        entity.Entity.__init__(
                self,
                x,
                y,
                color
            )

        self.x_velocity = 0
        self.y_velocity = 0
        self.onGround = False
        self.speed = speed
        self.jump = jump

        self.going_up = False
        self.going_down = False
        self.going_right = False
        self.going_left  =  False
        self.running = False

    def update_location(self, entities):
        if self.going_up:
            if self.onGround:
                self.y_velocity -= self.jump * settings.CHARACTER_JUMP_SPEED

        if self.going_down:
            pass

        if self.going_left:
            self.x_velocity = self.speed * -settings.CHARACTER_WALK_SPEED

        if self.going_right:
            self.x_velocity = self.speed * settings.CHARACTER_WALK_SPEED

        if self.running:
            self.x_velocity = self.x_velocity * 3

        if not self.onGround:
            self.y_velocity += settings.FALLING_ACCELERATION
            if self.y_velocity > settings.TERMINAL_VELOCITY:
                self.y_velocity = settings.TERMINAL_VELOCITY

        if not(self.going_left or self.going_right):
            self.x_velocity = 0

        self.onGround = False;                      # assuming we're in the air
        self.collide(self.x_velocity, self.y_velocity, entities) # do x-axis collisions


    def collide(self, x_velocity, y_velocity, entities):
        self.rect.left += self.x_velocity           # increment in x direction
        for entity in entities:
            if isinstance(entity, game_objects.Platform):
                if pygame.sprite.collide_rect(self, entity):

                    if x_velocity > 0:
                        self.rect.right = entity.rect.left

                    if x_velocity < 0:
                        self.rect.left = entity.rect.right

        self.rect.top += self.y_velocity            # increment in y direction
        for entity in entities:
            if isinstance(entity, game_objects.Platform):
                if pygame.sprite.collide_rect(self, entity):

                    if y_velocity > 0:
                        self.rect.bottom = entity.rect.top
                        self.onGround = True
                        self.y_velocity = 0

                    if y_velocity < 0:
                        self.rect.top = entity.rect.bottom
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
        self.going_up = True

    def stop_go_up(self):
        self.going_up = False

    def go_down(self) :
        self.going_down = True

    def stop_go_down(self) :
        self.going_down = False

    def go_left(self):
        self.going_left = True

    def stop_go_left(self):
        self.going_left = False

    def go_right(self):
        self.going_right = True

    def stop_go_right(self):
        self.going_right = False

    def run(self):
        self.running = True

    def stop_run(self):
        player.running = False



class NonPlayer(Character):
    def __init__(self, x, y, color):
        Character.__init__(
            self,
            x,
            y,
            size = 2,
            color = color,
            speed = 0.25,
            jump = 0.8
        )

    # TODO make this a "Behavior" and mode it to that class
    def follow(self, target):

        target_x , target_y = target.rect.center
        x , y = self.rect.center

        if target_x < x: #t   n tpos < npos to the left of npc
            self.going_right = False
            self.going_left = True

        if target_x > x : #n   t tpos > npos: to the right of npc
            self.going_right = True
            self.going_left = False

        if  target_x == x:  # don't move when x is inline x_targ
            self.going_right = False
            self.going_left = False

        if target_y < y: #above
            self.going_up = True

        if target_y > y: #bellow
            self.going_up = False

        if target_y == y: # same level
            self.going_up = False


player = Player(0 , 0 , settings.CHARACTER_COLOR)
npcs = []
