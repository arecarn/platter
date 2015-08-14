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
    screen = pygame.display.set_mode(settings.DISPLAY, settings.FLAGS, settings.DEPTH)
    pygame.display.set_caption("Use arrows to move!")
    timer = pygame.time.Clock()
    entities = pygame.sprite.Group()

    map = map_gen.Map(level._1)
    map.build(entities)

    action = actions.Action()

    # TODO: move this to it's own class?
    bg = game_objects.Background("#000000", settings.BLK_SIZE, settings.BLK_SIZE)

    cam = camera.Camera(map.width, map.height)

    player = characters.Player(settings.BLK_SIZE, settings.BLK_SIZE)
    characters.Player(settings.BLK_SIZE, settings.BLK_SIZE)
    entities.add(player)

    npc = characters.NonPlayer(settings.BLK_SIZE + 20 ,settings.BLK_SIZE + 20 )
    entities.add(npc)

    while 1:
        timer.tick(60)

        action.check(player.status) # check for events

        map.draw(screen, bg)

        cam.update(player) # update player camera TODO needs better discription
        player.updateLocation(map.platforms)
        npc.updateLocation(map.platforms)
        npc.follow(player)

        # draw everything with offset
        for e in entities:
            screen.blit(e.image, cam.apply(e)) # update entities with of set Camera
        pygame.display.update()




##############################################################################
# This runs main once every other function is defined
# this must last.
##############################################################################
if __name__ == "__main__":
    main()
