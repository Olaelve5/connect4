import pygame
from board.board import Board
from cursor import Cursor
from gameplay.ui import ui
import settings.properties as properties
from settings.game_settings import Game_Settings

# Create the board
board = Board()

# Frame rate
clock = pygame.time.Clock()


def player_is_bot(player):
    return player.type == "bot"


game_start_sound = pygame.mixer.Sound("assets/sounds/game_start.mp3")
move_sound = pygame.mixer.Sound("assets/sounds/slot.mp3")


def play_sound(last_time, current_time, sound, move_delay=50):
    if current_time - last_time > move_delay:  # Cooldown of 100ms
        sound.play()
        return current_time
    return last_time


def play(screen, game_settings: Game_Settings):

    board.reset()
    cursor = Cursor(screen)
    ui_instance = ui(
        game_settings.player_1,
        game_settings.player_2,
        game_settings.score,
        game_settings.total_games - game_settings.played_games,
    )

    player_turn = (
        game_settings.player_1 if board.player_turn == 1 else game_settings.player_2
    )

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
            if (
                game_settings.continuous
                and game_settings.played_games < game_settings.total_games - 1
            ):
                game_settings.score = (
                    game_settings.score[0] + 0.5,
                    game_settings.score[1] + 0.5,
                )
                game_settings.played_games += 1
                play(screen, game_settings)
            else:
                if game_settings.continuous:
                    winner = 1 if game_settings.score[0] > game_settings.score[1] else 2

                # Final game over menu
                from menus.game_over_menu import game_over_menu

                winner = (
                    game_settings.player_1 if winner == 1 else game_settings.player_2
                )

                game_over_menu(
                    screen,
                    winner,
                    game_settings.player_1,
                    game_settings.player_2,
                    game_settings.continuous,
                    0,
                    game_settings.total_games,
                )
            break

        # Check if there is a winner
        winner = board.winner
        if winner:
            if (
                game_settings.continuous
                and game_settings.played_games < game_settings.total_games - 1
            ):
                if winner == 1:
                    game_settings.score = (
                        game_settings.score[0] + 1,
                        game_settings.score[1],
                    )
                else:
                    game_settings.score = (
                        game_settings.score[0],
                        game_settings.score[1] + 1,
                    )

                ui_instance.update_score(game_settings.score)
                game_settings.played_games += 1

                # Start a new game
                play(
                    screen,
                    game_settings,
                )
            else:
                # Final game over menu
                from menus.game_over_menu import game_over_menu

                if game_settings.continuous:
                    winner = 1 if game_settings.score[0] > game_settings.score[1] else 2

                winner = (
                    game_settings.player_1 if winner == 1 else game_settings.player_2
                )

                game_over_menu(
                    screen,
                    winner,
                    game_settings.player_1,
                    game_settings.player_2,
                    game_settings.continuous,
                    0,
                    game_settings.max_count,
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
            if pygame.time.get_ticks() - bot_move_start_time > game_settings.move_delay:
                column = player_turn.get_move(board)
                board.make_move(column)
                player_turn = (
                    game_settings.player_1
                    if board.player_turn == 1
                    else game_settings.player_2
                )
                turn_taken = True

                # Play the sound
                last_sound_time = play_sound(
                    last_sound_time,
                    pygame.time.get_ticks(),
                    move_sound,
                    game_settings.move_delay,
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
                player_turn = (
                    game_settings.player_1
                    if board.player_turn == 1
                    else game_settings.player_2
                )
                move_sound.play()
                turn_taken = True

                # Play the sound
                last_sound_time = play_sound(
                    last_sound_time,
                    pygame.time.get_ticks(),
                    move_sound,
                    game_settings.move_delay,
                )

        pygame.display.update()
        clock.tick(properties.FPS)

        if turn_taken:
            turn_taken = False
