import pygame
import characters


def do_nothing(__):
    pass

def do_raise(exception):
    raise(exception)

class Action(object):
    def __init__(self):
        self.keyboard_event = {

            pygame.K_UP : {
                pygame.KEYDOWN : characters.player.go_up,
                pygame.KEYUP   : characters.player.stop_go_up,
                },

            pygame.K_DOWN : {
                pygame.KEYDOWN : characters.player.go_down,
                pygame.KEYUP   : characters.player.stop_go_down,
                },

            pygame.K_LEFT : {
                pygame.KEYDOWN : characters.player.go_left,
                pygame.KEYUP   : characters.player.stop_go_left,
                },

            pygame.K_RIGHT : {
                pygame.KEYDOWN : characters.player.go_right,
                pygame.KEYUP   : characters.player.stop_go_right,
                },

            pygame.K_SPACE : {
                pygame.KEYDOWN : characters.player.run,
                pygame.KEYUP   : characters.player.stop_run,
            },

            pygame.K_ESCAPE: {
                pygame.KEYDOWN : exit,
                pygame.KEYUP   : exit,
            },
        }

    def handle_keyboard_events(self, event):
        if is_keyboard_event(self, event):
            keyHandler = self.keyboard_event[event.key][event.type]()

    def check(self, player):
        for event in pygame.event.get():
            handle_keyboard_events(self, event)

    def is_keyboard_event(self, event):
        return ((event.type == pygame.KEYDOWN or
                event.type == pygame.KEYUP) and
                event.key in self.keyboard_event.keys())


def exit():
    raise SystemExit()


