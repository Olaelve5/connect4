import pygame
from board import Board
from cursor import Cursor
from gameplay.ui import ui
import properties

# Create the board
board = Board()

# Frame rate
clock = pygame.time.Clock()

# ui
ui = ui("Player 1", "Player 2")

def play(screen):
    board.reset()
    cursor = Cursor(screen)

    pygame.mouse.set_visible(False)

    while True:
        screen.blit(properties.BACKGROUND_IMAGE, (0, 0))

        # Draw the board
        board.draw(screen)

        for column in board.columns:
            if column.is_hovered(pygame.mouse.get_pos()):
                if board.player_turn == 1:
                    cursor.set_mode("drop_1")
                else:
                    cursor.set_mode("drop_2")
                column.hovered_draw(screen)
                break
        else:
            cursor.set_mode("default")

        winner = board.winner
        if winner:
            from menus.game_over_menu import game_over_menu
            game_over_menu(screen, winner)
            break

        # Draw the UI
        ui.draw(screen)

        # Draw the cursor
        cursor.draw(pygame.mouse.get_pos())

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Handle mouse click on the board
                board.handle_click(event.pos)

        pygame.display.update()
        clock.tick(properties.FPS)