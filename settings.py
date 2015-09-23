import pygame

WIN_WIDTH = 800
WIN_HEIGHT = int(WIN_WIDTH / 1.25)
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)
BLK_SIZE = 32

SWD_SIZE_X = 32
SWD_SIZE_Y = 8

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0
CAMERA_SLACK = 30

CHARACTER_WALK_SPEED = BLK_SIZE / 8
CHARACTER_JUMP_SPEED = BLK_SIZE / 4

FALLING_ACCELERATION = BLK_SIZE / 106.66
TERMINAL_VELOCITY = BLK_SIZE * 3

BACKGROUND_COLOR = "#000000"
PLATFORM_COLOR = "#DDDDDD"
EXIT_BLOCK_COLOR = "#C0C0C0"
CHARACTER_COLOR = "#0000FF"
NPC_COLOR = "#FF0000"


SCREEN = pygame.display.set_mode(
    DISPLAY,
    FLAGS,
    DEPTH
)

class Background(pygame.Surface):
    def __init__(self, color, width, height):
       pygame.Surface.__init__(self, (width, height))
       self.convert()
       self.fill(pygame.Color(color))

    def update(self):
        for y in range(WIN_HEIGHT // BLK_SIZE):
            for x in range(WIN_WIDTH // BLK_SIZE):
                SCREEN.blit(self, (x * BLK_SIZE, y * BLK_SIZE))

BACKGROUND = Background(
    BACKGROUND_COLOR,
    BLK_SIZE,
    BLK_SIZE
)
