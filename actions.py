import pygame
import characters

class Action(object):
    def __init__(self):
        self.keyboard_event = {

            pygame.K_UP : {
                pygame.KEYDOWN : GoUp(characters.player),
                pygame.KEYUP   : StopY(characters.player),
                },

            pygame.K_DOWN : {
                pygame.KEYDOWN : GoDown(characters.player),
                pygame.KEYUP   : StopY(characters.player),
                },

            pygame.K_LEFT : {
                pygame.KEYDOWN : GoLeft(characters.player),
                pygame.KEYUP   : StopX(characters.player),
                },

            pygame.K_RIGHT : {
                pygame.KEYDOWN : GoRight(characters.player),
                pygame.KEYUP   : StopX(characters.player),
                },

            pygame.K_ESCAPE: {
                pygame.KEYDOWN : Exit,
                pygame.KEYUP   : DoNothing,
            },
        }

    def set_player(self, player):
        self.player = player

    def is_keyboard_event(self, event):
        return ((event.type == pygame.KEYDOWN or
                event.type == pygame.KEYUP) and
                event.key in self.keyboard_event.keys())

    def handle_keyboard_events(self, event):
        if self.is_keyboard_event(event):
            keyHandler = self.keyboard_event[event.key][event.type].execute()

    def check(self):
        for event in pygame.event.get():
            self.handle_keyboard_events(event)


class Command(object):
    def __init__(self):
        pass


class DoNothing(Command):
    def __init__(self):
        super().__init__()

    def execute(self):
        pass


class CharacterCommand(Command):
    def __init__(self, character):
        Command().__init__()
        self.character = character


class GoUp(CharacterCommand):
    def __init__(self, character):
        super().__init__(character)

    def execute(self):
        self.character.go_up()


class GoDown(CharacterCommand):
    def __init__(self, character):
        super().__init__(character)

    def execute(self):
        self.character.go_down()


class GoLeft(CharacterCommand):
    def __init__(self, character):
        super().__init__(character)

    def execute(self):
        self.character.go_left()


class GoRight(CharacterCommand):
    def __init__(self, character):
        super().__init__(character)

    def execute(self):
        self.character.go_right()


class StopX(CharacterCommand):
    def __init__(self, character):
        super().__init__(character)

    def execute(self):
        self.character.stop_x()


class StopY(CharacterCommand):
    def __init__(self, character):
        super().__init__(character)

    def execute(self):
        self.character.stop_y()


class InterfaceCommand(Command):
    def __init__(self):
        pass


class Exit(InterfaceCommand):
    def __init__(self):
        super().__init__()

    def execute():
        raise SystemExit()


