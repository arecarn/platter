import pygame
import entity
import settings
import game_objects
import actions


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
        self.collision = CollisionComponent(self)

    def update(self, entities):
        new_entities = []
        new_entities[:] = entities.sprites()
        new_entities.remove(self)


        self.rect.left += self.x_velocity
        self.collision.collide_x(new_entities)

        self.rect.top += self.y_velocity
        self.collision.collide_y(new_entities)
        self.do_behavior()

    def do_behavior(self):
        pass


    def go_up(self):
        self.y_velocity = self.speed * -settings.CHARACTER_WALK_SPEED

    def go_down(self) :
        self.y_velocity = self.speed * settings.CHARACTER_WALK_SPEED

    def stop_y(self):
        self.y_velocity = 0

    def go_left(self):
        self.x_velocity = self.speed * -settings.CHARACTER_WALK_SPEED

    def go_right(self):
        self.x_velocity = self.speed * settings.CHARACTER_WALK_SPEED

    def stop_x(self):
        self.x_velocity = 0


class CollisionComponent(object):
    def __init__(self, entity):
        self.entity = entity

    def collide_x(self, entities):
        entity = pygame.sprite.spritecollideany(self.entity, entities)
        while entity != None:
            if self.entity.x_velocity > 0:
                self.entity.rect.right = entity.rect.left

            if self.entity.x_velocity < 0:
                self.entity.rect.left = entity.rect.right
            entity = pygame.sprite.spritecollideany(self.entity, entities)

    def collide_y(self, entities):
        entity = pygame.sprite.spritecollideany(self.entity, entities)
        while entity != None:
            if self.entity.y_velocity > 0:
                self.entity.rect.bottom = entity.rect.top

            if self.entity.y_velocity < 0:
                self.entity.rect.top = entity.rect.bottom
            entity = pygame.sprite.spritecollideany(self.entity, entities)


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

    def do_behavior(self):
        self.follow(player)

    # TODO make this a "Behavior" and mode it to that class
    def follow(self, target):

        target_x , target_y = target.rect.center
        x , y = self.rect.center

        if target_x < x: #t   n tpos < npos to the left of npc
            actions.GoLeft(self).execute()

        if target_x > x : #n   t tpos > npos: to the right of npc
            actions.GoRight(self).execute()

        if target_y < y: #above
            actions.GoUp(self).execute()

        if target_y > y: #bellow
            actions.GoDown(self).execute()


player = Player(0 , 0 , settings.CHARACTER_COLOR)
npcs = []
