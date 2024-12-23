import pygame
from board.board import Board
from cursor import Cursor
from gameplay.ui import ui
import properties

# Create the board
board = Board()

# Frame rate
clock = pygame.time.Clock()

def player_is_bot(player):
    return player.type == "bot"


def play(screen, player_1, player_2):

    board.reset()
    cursor = Cursor(screen)
    ui_instance = ui(player_1, player_2)

    player_turn = player_1 if board.player_turn == 1 else player_2

    pygame.mouse.set_visible(False)

    turn_taken = False
    bot_move_start_time = None

    while True:
        screen.blit(properties.BACKGROUND_IMAGE, (0, 0))

        # Draw the board
        board.draw(screen)

        # Check if the cursor is hovering over a column
        for column in board.columns:
            if column.is_hovered(pygame.mouse.get_pos()) and not player_is_bot(player_turn):
                if board.player_turn == 1:
                    cursor.set_mode("drop_1")
                else:
                    cursor.set_mode("drop_2")
                column.hovered_draw(screen)
                break
        else:
            cursor.set_mode("default")

        # Check if there is a winner, if so, show the game over menu
        winner = board.winner
        if winner:
            from menus.game_over_menu import game_over_menu

            game_over_menu(
                screen, player_1 if winner == 1 else player_2, player_1, player_2
            )
            break

        # Draw the UI
        ui_instance.draw(screen)

        # Draw the cursor
        cursor.draw(pygame.mouse.get_pos())

        # Handle bot move with delay
        if player_is_bot(player_turn) and not turn_taken:
            if bot_move_start_time is None:  # Start the timer
                bot_move_start_time = pygame.time.get_ticks()

            # Check if 0.5 seconds have passed
            if pygame.time.get_ticks() - bot_move_start_time > 500:
                column = player_turn.get_move(board)
                board.make_move(column)
                player_turn = player_1 if board.player_turn == 1 else player_2
                turn_taken = True
                bot_move_start_time = None  # Reset the timer

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                quit()

            # Handle mouse click and human move 
            if event.type == pygame.MOUSEBUTTONDOWN and player_turn.type == "human": 
                # Handle mouse click on the board
                board.handle_click(event.pos)
                player_turn = player_1 if board.player_turn == 1 else player_2
                turn_taken = True

        pygame.display.update()
        clock.tick(properties.FPS)

        if turn_taken:
            turn_taken = False
