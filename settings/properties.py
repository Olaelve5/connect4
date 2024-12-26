import pygame

pygame.init()

info = pygame.display.Info()
WINDOW_WIDTH, WINDOW_HEIGHT = info.current_w, info.current_h
CHIP_RADIUS = 40
CHIP_GAP = 20
COLUMN_WIDTH = CHIP_RADIUS * 2 + CHIP_GAP
BOARD_WIDTH = COLUMN_WIDTH * 7 + CHIP_GAP
BOARD_HEIGHT = CHIP_RADIUS * 2 * 6 + CHIP_GAP * 7
VERTICAL_GAP = (WINDOW_HEIGHT - BOARD_HEIGHT) // 2 
HORIZONTAL_GAP = (WINDOW_WIDTH - BOARD_WIDTH) // 2
VERTICAL_START = WINDOW_HEIGHT  - VERTICAL_GAP - CHIP_RADIUS - CHIP_GAP
HORIZONTAL_START = (WINDOW_WIDTH - BOARD_WIDTH) // 2 + CHIP_RADIUS + CHIP_GAP

# Colors
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND = (36, 40, 51)
HOVER_RED = (255, 143, 200)
HOVER_YELLOW = (255, 255, 200)

# Font
TITLE_FONT = pygame.font.Font("assets/Symtext.ttf", 56)
FONT = pygame.font.Font("assets/Symtext.ttf", 40)
SUB_FONT = pygame.font.Font("assets/Symtext.ttf", 24)

# Background image
BACKGROUND_IMAGE = pygame.image.load("assets/background.jpg")
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WINDOW_WIDTH, WINDOW_HEIGHT))

# FPS
FPS = 60


