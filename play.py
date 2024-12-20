import pygame
from board import Board
from ui import ui
from properties import BACKGROUND
from game_over import game_over_screen

# Create the board
board = Board()

# Frame rate
clock = pygame.time.Clock()
FPS = 60

# ui
ui = ui("Player 1", "Player 2")

def play(screen):

    while True:
        screen.fill(BACKGROUND)

        # Draw the board
        board.draw(screen)

        winner = board.winner
        if winner:
            game_over_screen(screen, winner)
            break

        # Draw the UI
        ui.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Handle mouse click on the board
                board.handle_click(event.pos)

        pygame.display.update()
        clock.tick(FPS)
    
