import pygame

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


