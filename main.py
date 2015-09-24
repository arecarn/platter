import pygame

import level
import characters
import game_objects
import settings
import game
import actions


def main():
    pygame.init()
    pygame.display.set_caption("Use arrows to move!")

    world = game.Game(level._1)

    timer = pygame.time.Clock()

    while 1:
        timer.tick(60)

        settings.BACKGROUND.update()
        world.update_camera()
        world.entities.update(world) #could each entity have an instance of the game
        pygame.display.update()

if __name__ == "__main__":
    main()
