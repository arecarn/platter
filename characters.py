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
    ):
        entity.Entity.__init__(
                self,
                x,
                y,
                color
            )

        self.x_velocity = 0
        self.y_velocity = 0
        self.speed = speed

        self.going_up = False
        self.going_down = False
        self.going_right = False
        self.going_left  =  False

    def update(self, entities):
        self.rect.left += self.x_velocity
        self.collide_x(entities)
        self.rect.top += self.y_velocity
        self.collide_y(entities)
        self.do_behavior()

    def handleActions(self):
        pass

    def collide_x(self, entities):
        for entity in entities:
            if isinstance(entity, game_objects.Platform):
                if pygame.sprite.collide_rect(self, entity):

                    if self.x_velocity > 0:
                        self.rect.right = entity.rect.left

                    if self.x_velocity < 0:
                        self.rect.left = entity.rect.right

    def collide_y(self, entities):
        for entity in entities:
            if isinstance(entity, game_objects.Platform):
                if pygame.sprite.collide_rect(self, entity):

                    if self.y_velocity > 0:
                        self.rect.bottom = entity.rect.top
                        self.y_velocity = 0

                    if self.y_velocity < 0:
                        self.rect.top = entity.rect.bottom
                        self.y_velocity = 0

    def go_up(self):
        self.y_velocity = self.speed * -settings.CHARACTER_WALK_SPEED

    def go_down(self) :
        self.y_velocity = self.speed * settings.CHARACTER_WALK_SPEED

    def go_left(self):
        self.x_velocity = self.speed * -settings.CHARACTER_WALK_SPEED

    def go_right(self):
        self.x_velocity = self.speed * settings.CHARACTER_WALK_SPEED

    def stop_x(self):
        self.x_velocity = 0

    def stop_y(self):
        self.y_velocity = 0

class Player(Character):
    def __init__(self, x, y, color):
        super().__init__(
            x,
            y,
            size = 1,
            color = color,
            speed = 1,
        )


class NonPlayer(Character):
    def __init__(self, x, y, color):
        super().__init__(
            x,
            y,
            size = 2,
            color = color,
            speed = 0.25,
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
