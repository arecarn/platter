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

    the_game = game.Game()
    the_game.build(level._1)

    timer = pygame.time.Clock()

    while 1:
        timer.tick(60)
        the_game.update()
        pygame.display.update()

if __name__ == "__main__":
    main()
