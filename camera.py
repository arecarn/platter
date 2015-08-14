import pygame
import settings

##############################################################################
# Camera
# keep scroll on the map following a target sprite
##############################################################################
class Camera(object):
    def __init__(self, width, height):
        self.state = pygame.Rect(0, 0, width, height)
    # provide the offset for each block
    def apply(self, target):
        return target.rect.move(self.state.topleft)
    def update(self, target):
        self.state = self.complex_camera(self.state, target.rect)

    #TODO: integrate into class
    def simple_camera(self, camera, target_rect):
        l, t, _, _ = target_rect # left , top position
        # _, _, w, h = camera # width, height of camera
        w = settings.WIN_WIDTH
        h = settings.WIN_HEIGHT
        # center the camera on the target
        return pygame.Rect(-l+settings.HALF_WIDTH, -t+settings.HALF_HEIGHT, w, h)

    #TODO: integrate into class
    def complex_camera(self, camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera
        l, t, _, _ = -l+settings.HALF_WIDTH, -t+settings.HALF_HEIGHT, w, h

        l = min(0, l)                           # stop scrolling at the left edge
        l = max(-(camera.width-settings.WIN_WIDTH), l)   # stop scrolling at the right edge
        t = max(-(camera.height-settings.WIN_HEIGHT), t) # stop scrolling at the bottom
        t = min(0, t)                           # stop scrolling at the top
        return pygame.Rect(l, t, w, h)
