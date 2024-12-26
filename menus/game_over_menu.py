import pygame
import settings.properties as properties
from menus.button import Button
from cursor import Cursor
from settings.game_settings import Game_Settings


# Create the game over screen
def game_over_menu(
    screen,
    winner,
    game_settings: Game_Settings,
):
    pygame.display.set_caption("Game Over Screen")

    pygame.mouse.set_visible(False)
    cursor = Cursor(screen)

    GAME_OVER_TITLE = properties.FONT.render(
        f"{winner.name} wins!" if winner != None else "It's a draw!",
        True,
        properties.WHITE,
    )
    GAME_OVER_TITLE_RECT = GAME_OVER_TITLE.get_rect(
        center=(properties.WINDOW_WIDTH / 2, 100)
    )

    PLAY_AGAIN_BUTTON = Button(
        "Play Again",
        properties.WINDOW_WIDTH / 2,
        properties.WINDOW_HEIGHT - 275,
        properties.FONT,
        properties.WHITE,
        screen,
    )

    PLAY_AGAIN_SWITCH_BUTTON = Button(
        "Switch Sides",
        properties.WINDOW_WIDTH / 2,
        properties.WINDOW_HEIGHT - 175,
        properties.FONT,
        properties.WHITE,
        screen,
    )

    MAIN_MENU_BUTTON = Button(
        "Main Menu",
        properties.WINDOW_WIDTH / 2,
        properties.WINDOW_HEIGHT - 75,
        properties.FONT,
        properties.WHITE,
        screen,
    )

    # Player 1 text
    player_1_score = properties.SUB_FONT.render(
        "Score: " + str(game_settings.score[0]), True, properties.WHITE
    )
    player_1_score_rect = player_1_score.get_rect(
        center=(properties.WINDOW_WIDTH / 4 + 100, 520)
    )

    player_1_name = properties.SUB_FONT.render(
        game_settings.player_1.name, True, properties.WHITE
    )
    player_1_name_rect = player_1_name.get_rect(
        center=(properties.WINDOW_WIDTH / 4 + 100, 240)
    )

    # Player 2 text
    player_2_score = properties.SUB_FONT.render(
        "Score: " + str(game_settings.score[1]), True, properties.WHITE
    )
    player_2_score_rect = player_2_score.get_rect(
        center=(properties.WINDOW_WIDTH / 4 * 3 - 200 + 100, 520)
    )

    player_2_name = properties.SUB_FONT.render(
        game_settings.player_2.name, True, properties.WHITE
    )

    player_2_name_rect = player_2_name.get_rect(
        center=(properties.WINDOW_WIDTH / 4 * 3 - 200 + 100, 240)
    )

    clock = pygame.time.Clock()

    while True:
        screen.blit(properties.BACKGROUND_IMAGE, (0, 0))

        GAME_OVER_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(GAME_OVER_TITLE, GAME_OVER_TITLE_RECT)
        PLAY_AGAIN_BUTTON.draw(GAME_OVER_MOUSE_POS)
        PLAY_AGAIN_SWITCH_BUTTON.draw(GAME_OVER_MOUSE_POS)
        MAIN_MENU_BUTTON.draw(GAME_OVER_MOUSE_POS)
        screen.blit(player_1_score, player_1_score_rect)
        screen.blit(player_1_name, player_1_name_rect)
        screen.blit(player_2_score, player_2_score_rect)
        screen.blit(player_2_name, player_2_name_rect)

        game_settings.player_1.draw(screen, (properties.WINDOW_WIDTH / 4, 280))
        game_settings.player_2.draw(
            screen, (properties.WINDOW_WIDTH / 4 * 3 - 200, 280)
        )

        for button in [PLAY_AGAIN_BUTTON, MAIN_MENU_BUTTON, PLAY_AGAIN_SWITCH_BUTTON]:
            if button.is_hovered(GAME_OVER_MOUSE_POS):
                cursor.set_mode("click")
                break
            else:
                cursor.set_mode("default")

        cursor.draw(GAME_OVER_MOUSE_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_AGAIN_BUTTON.is_hovered(GAME_OVER_MOUSE_POS):
                    from gameplay.play import play

                    game_settings.reset()
                    play(screen, game_settings)

                if PLAY_AGAIN_SWITCH_BUTTON.is_hovered(GAME_OVER_MOUSE_POS):
                    from gameplay.play import play

                    game_settings.switch_sides()
                    game_settings.reset()
                    play(screen, game_settings)

                if MAIN_MENU_BUTTON.is_hovered(GAME_OVER_MOUSE_POS):
                    from menus.main_menu import main_menu

                    game_settings.reset()
                    main_menu(screen, game_settings)

        clock.tick(properties.FPS)

        pygame.display.update()
