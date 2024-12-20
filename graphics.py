import pygame
from properties import WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND
from graphics_board import Board

pygame.init()


# Create the screen with the size of the client's screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
screen.fill(BACKGROUND)
pygame.display.set_caption('Connect 4')

# Create the board
board = Board()

# Frame rate
clock = pygame.time.Clock()
FPS = 60

while True:
    screen.fill(BACKGROUND)

    # Draw the board
    board.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Handle mouse click on the board
            board.handle_click(event.pos)

    pygame.display.update()
    clock.tick(FPS)