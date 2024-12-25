import pygame
from board.board import Board
from cursor import Cursor
from gameplay.ui import ui
import properties

# Create the board
board = Board()

# Frame rate
clock = pygame.time.Clock()

# Bot move delay
MOVE_DELAY = 10


def player_is_bot(player):
    return player.type == "bot"


game_start_sound = pygame.mixer.Sound("assets/sounds/game_start.mp3")
move_sound = pygame.mixer.Sound("assets/sounds/slot.mp3")


def play_sound(last_time, current_time, sound):
    if current_time - last_time > MOVE_DELAY:  # Cooldown of 100ms
        sound.play()
        return current_time
    return last_time


def play(screen, player_1, player_2, continuous=True, score=(0, 0), count=0):

    # game_start_sound.play()

    board.reset()
    cursor = Cursor(screen)
    ui_instance = ui(player_1, player_2, score)

    player_turn = player_1 if board.player_turn == 1 else player_2

    pygame.mouse.set_visible(False)

    turn_taken = False
    bot_move_start_time = None
    last_sound_time = 0  # Used to prevent multiple sounds from playing at the same time

    while True:
        screen.blit(properties.BACKGROUND_IMAGE, (0, 0))

        # Draw the board
        board.draw(screen)

        # Check if the cursor is hovering over a column
        for column in board.columns:
            if column.is_hovered(pygame.mouse.get_pos()) and not player_is_bot(
                player_turn
            ):
                if board.player_turn == 1:
                    cursor.set_mode("drop_1")
                else:
                    cursor.set_mode("drop_2")
                column.hovered_draw(screen)
                break
        else:
            cursor.set_mode("default")

        # Handle a draw
        if board.available_columns() == []:
            if continuous and count < 9:
                score = (score[0] + 0.5, score[1] + 0.5)
                play(
                    screen,
                    player_1,
                    player_2,
                    continuous=True,
                    score=score,
                    count=count + 1,
                )
            else:
                if continuous:
                    winner = 1 if score[0] > score[1] else 2
                # Final game over menu
                from menus.game_over_menu import game_over_menu

                winner = player_1 if winner == 1 else player_2

                game_over_menu(screen, winner, player_1, player_2)
            break

        # Check if there is a winner, if so, show the game over menu
        winner = board.winner
        if winner:
            if continuous and count < 9:
                if winner == 1:
                    score = (score[0] + 1, score[1])
                else:
                    score = (score[0], score[1] + 1)

                ui_instance.update_score(score)

                # Start a new game
                play(
                    screen,
                    player_1,
                    player_2,
                    continuous=True,
                    score=score,
                    count=count + 1,
                )
            else:
                # Final game over menu
                from menus.game_over_menu import game_over_menu

                if continuous:
                    winner = 1 if score[0] > score[1] else 2

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
            if pygame.time.get_ticks() - bot_move_start_time > MOVE_DELAY:
                column = player_turn.get_move(board)
                board.make_move(column)
                player_turn = player_1 if board.player_turn == 1 else player_2
                turn_taken = True

                # Play the sound
                last_sound_time = play_sound(
                    last_sound_time, pygame.time.get_ticks(), move_sound
                )

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
                move_sound.play()
                turn_taken = True

                # Play the sound
                last_sound_time = play_sound(
                    last_sound_time, pygame.time.get_ticks(), move_sound
                )

        pygame.display.update()
        clock.tick(properties.FPS)

        if turn_taken:
            turn_taken = False
