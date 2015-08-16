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
    timer = pygame.time.Clock()
    entities = pygame.sprite.Group()
    players = []
    npcs = []

    screen = pygame.display.set_mode(settings.DISPLAY, settings.FLAGS, settings.DEPTH)
    background = game_objects.Background("#000000", settings.BLK_SIZE, settings.BLK_SIZE)

    map = map_gen.Map(level._1)
    map.build(entities, players, npcs)
    game_camera = camera.Camera(map.width, map.height)

    action = actions.Action()

    player = players[0]


    while 1:
        timer.tick(60)

        action.check(player.status)

        player.updateLocation(map.platforms)
        for npc in npcs:
            npc.updateLocation(map.platforms)
            npc.follow(player)

        game_camera.update(player)
        map.draw(screen, background)

        # draw everything with offset
        for e in entities:
            screen.blit(e.image, game_camera.apply(e))

        pygame.display.update()


##############################################################################
# This runs main once every other function is defined
# this must last.
##############################################################################
if __name__ == "__main__":
    main()
