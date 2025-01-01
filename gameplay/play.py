import pygame
from cursor import Cursor
from gameplay.ui import ui
import settings.properties as properties
from environment.connect4Env import Connect4Env
from play_utils import player_is_bot, play_sound, move_sound

# Frame rate
clock = pygame.time.Clock()


def play(screen, env: Connect4Env):
    env.reset()  # Reset the environment

    cursor = Cursor(screen)
    ui_instance = ui(env)

    player_turn = env.player_1 if env.board.player_turn == 1 else env.player_2

    pygame.mouse.set_visible(False)

    turn_taken = False
    bot_move_start_time = None
    last_sound_time = 0  # Used to prevent multiple sounds from playing at the same time

    while True:
        screen.blit(properties.BACKGROUND_IMAGE, (0, 0))

        # Draw the board
        env.board.draw(screen)

        # Check if the cursor is hovering over a column
        for column in env.board.columns:
            if column.is_hovered(pygame.mouse.get_pos()) and not player_is_bot(
                player_turn
            ):
                if env.board.player_turn == 1:
                    cursor.set_mode("drop_1")
                else:
                    cursor.set_mode("drop_2")
                column.hovered_draw(screen)
                break
        else:
            cursor.set_mode("default")

        # Handle a draw
        if env.board.available_columns() == []:

            if (
                env.continuous
                and env.played_games < env.total_games - 1
            ):
                env.played_games += 1

                play(screen, env)
            else:
                if env.continuous:
                    winner = 1 if env.score[0] > env.score[1] else 2

                # Final game over menu
                from menus.game_over_menu import game_over_menu

                # Check if there is a winner, set the winner to None if it's a draw
                winner = (
                    env.player_1 if winner == 1 else env.player_2
                )

                if env.score[0] == env.score[1]:
                    winner = None

                game_over_menu(screen, winner, env)
            break

        # Check if there is a winner
        winner = game_settings.board.winner
        if winner:
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

            if (
                game_settings.continuous
                and game_settings.played_games < game_settings.total_games - 1
            ):

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

                if game_settings.score[0] == game_settings.score[1]:
                    winner = None

                game_over_menu(screen, winner, game_settings)
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
                move = player_turn.get_move(game_settings.board)

                if not game_settings.board.is_valid_move(move):
                    # print(f"Invalid move by {player_turn.name}, skipping turn")

                    # Skip the turn by switching to the next player
                    game_settings.board.switch_player()
                    player_turn = (
                        game_settings.player_1
                        if game_settings.board.player_turn == 1
                        else game_settings.player_2
                    )
                    turn_taken = True
                    bot_move_start_time = None  # Reset the timer
                    continue  # Skip the rest of the bot move logic

                game_settings.board.make_move(move)
                player_turn = (
                    game_settings.player_1
                    if game_settings.board.player_turn == 1
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
                game_settings.board.handle_click(event.pos)
                player_turn = (
                    game_settings.player_1
                    if game_settings.board.player_turn == 1
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
