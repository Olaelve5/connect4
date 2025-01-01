import pygame
from cursor import Cursor
from gameplay.ui import ui
import settings.properties as properties
from environment.connect4Env import Connect4Env
from gameplay.play_utils import player_is_bot, play_sound, move_sound


def play(screen, env: Connect4Env):
    env.reset()  # Reset the environment

    cursor = Cursor(screen)
    ui_instance = ui(env)

    # Frame rate
    clock = pygame.time.Clock()

    pygame.mouse.set_visible(False)

    turn_taken = False
    bot_move_start_time = None
    last_sound_time = 0  # Used to prevent multiple sounds from playing at the same time

    while True:
        screen.blit(properties.BACKGROUND_IMAGE, (0, 0))

        turn_taken = False

        # Draw the board
        env.board.draw(screen)

        # Check if the cursor is hovering over a column and change the cursor mode
        for column in env.board.columns:
            if column.is_hovered(pygame.mouse.get_pos()) and not player_is_bot(
                env.player_turn
            ):
                if env.player_turn == env.player_1:
                    cursor.set_mode("drop_1")
                else:
                    cursor.set_mode("drop_2")
                column.hovered_draw(screen)
                break
        else:
            cursor.set_mode("default")

        # Draw the UI
        ui_instance.draw(screen)

        # Draw the cursor
        cursor.draw(pygame.mouse.get_pos())

        # Handle a draw
        if env.board.available_columns() == []:

            if env.continuous and env.played_games < env.total_games:
                return play(screen, env)

            # Show the game over menu
            from menus.game_over_menu import game_over_menu

            return game_over_menu(screen, env)

        # Handle a winner
        if env.winner:
            if env.continuous and env.played_games < env.total_games:
                print(env.played_games, env.total_games)
                return play(screen, env)

            # Show the game over menu
            from menus.game_over_menu import game_over_menu
            return game_over_menu(screen, env)

        # Handle bot move with delay
        if player_is_bot(env.player_turn) and not turn_taken:

            if bot_move_start_time is None:  # Start the timer
                bot_move_start_time = pygame.time.get_ticks()

            # Check if move delay have passed
            if pygame.time.get_ticks() - bot_move_start_time > env.move_delay:
                move = env.player_turn.get_move(env.board)
                env.step(move)
                turn_taken = True

                # Play the sound
                last_sound_time = play_sound(
                    last_sound_time,
                    pygame.time.get_ticks(),
                    move_sound,
                    env.move_delay,
                )

                bot_move_start_time = None  # Reset the timer

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                quit()

            # Handle mouse click and human move
            if event.type == pygame.MOUSEBUTTONDOWN and not player_is_bot(
                env.player_turn
            ):
                # Handle mouse click on the board
                move = env.board.handle_click(event.pos)
                if move is not None:
                    env.step(move)
                    move_sound.play()
                    turn_taken = True

                    # Play the sound
                    last_sound_time = play_sound(
                        last_sound_time,
                        pygame.time.get_ticks(),
                        move_sound,
                        env.move_delay,
                    )

        pygame.display.update()
        clock.tick(properties.FPS)
