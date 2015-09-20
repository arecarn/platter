import pygame

import level
import characters
import game_objects
import settings
import camera
import map_gen
import actions


def main():
    pygame.init()
    pygame.display.set_caption("Use arrows to move!")

    map = map_gen.Map(level._1)
    map.build()
    game_camera = camera.Camera(map.width, map.height)

    action = actions.Action()
    action.set_player(characters.player)

    timer = pygame.time.Clock()

    while 1:
        timer.tick(60)

        action.check()
        characters.player.update(map.entities)

        for npc in characters.npcs:
            npc.update(map.entities)

        game_camera.update(characters.player)
        map.draw(offset=game_camera.apply)
        pygame.display.update()

if __name__ == "__main__":
    main()
