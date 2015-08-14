import pygame

class Debug(object):
    enable = False
    def printHeader(self, txt):
        if self.enable:
            print('=' * 80)
            print(txt)
            print('-' * 80)
    def printMsg(self, txt):
        if self.enable:
            print(txt)
debug = Debug()
debug.enable = True

##############################################################################
# Action
# Handles keyboard events/ especially movment
##############################################################################
class Action(object):

    def check(self, status):
            # check for keys and handle movement
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                raise SystemExit("QUIT")
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                raise SystemExit("ESCAPE")
            if e.type == pygame.KEYDOWN and (e.key == pygame.K_UP or e.key == pygame.K_j):
                status['up'] = True
                debug.printMsg((('action is up')))
            if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
                status['down'] = True
                debug.printMsg('action is down')
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                status['left'] = True
                debug.printMsg('action is left')
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                status['right'] = True
                debug.printMsg('action is right')
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                status['running'] = True
                debug.printMsg('action is running')
            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                status['up'] = False
            if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
                status['down'] = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                status['right'] = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                status['left'] = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                status['right'] = False
