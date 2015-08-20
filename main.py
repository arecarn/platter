import pygame

import level
import characters
import game_objects
import settings
import camera
import map_gen
import actions


##############################################################################
# Main
# Includes initialization, and the main game loop
##############################################################################
def main():
    pygame.init()
    pygame.display.set_caption("Use arrows to move!")

    players = []
    npcs = []
    map = map_gen.Map(level._1)
    map.build(players, npcs)
    player = players[0]
    game_camera = camera.Camera(map.width, map.height)

    action = actions.Action()

    timer = pygame.time.Clock()

    while 1:
        timer.tick(60)

        action.check(player.status)
        player.updateLocation(map.platforms)

        for npc in npcs:
            npc.updateLocation(map.platforms)
            npc.follow(player)

        game_camera.update(player)
        map.draw(offset=game_camera.apply)
        pygame.display.update()

##############################################################################
# This runs main once every other function is defined
# this must last.
##############################################################################
if __name__ == "__main__":
    main()
