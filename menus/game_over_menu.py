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

    GAME_OVER_TITLE = properties.FONT.render("Winner is", True, properties.WHITE)
    GAME_OVER_TITLE_RECT = GAME_OVER_TITLE.get_rect(
        center=(properties.WINDOW_WIDTH / 2, 100)
    )

    PLAY_AGAIN_BUTTON = Button(
        "Play Again",
        properties.WINDOW_WIDTH / 2,
        properties.WINDOW_HEIGHT - 300,
        properties.FONT,
        properties.WHITE,
        screen,
    )

    MAIN_MENU_BUTTON = Button(
        "Main Menu",
        properties.WINDOW_WIDTH / 2,
        properties.WINDOW_HEIGHT - 200,
        properties.FONT,
        properties.WHITE,
        screen,
    )

    QUIT_BUTTON = Button(
        "Quit",
        properties.WINDOW_WIDTH / 2,
        properties.WINDOW_HEIGHT - 100,
        properties.FONT,
        properties.WHITE,
        screen,
    )

    player_image = pygame.image.load(winner.image_url)
    player_image = pygame.transform.scale(player_image, (200, 200))
    player_image_rect = player_image.get_rect(center=(properties.WINDOW_WIDTH / 2, 350))

    player_text = properties.SUB_FONT.render(winner.name, True, properties.WHITE)
    player_text_rect = player_text.get_rect(center=(properties.WINDOW_WIDTH / 2, 490))

    player_title = properties.SUB_FONT.render("Player 1", True, properties.WHITE)
    player_title_rect = player_title.get_rect(center=(properties.WINDOW_WIDTH / 2, 220))

    clock = pygame.time.Clock()

    while True:
        screen.blit(properties.BACKGROUND_IMAGE, (0, 0))

        GAME_OVER_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(GAME_OVER_TITLE, GAME_OVER_TITLE_RECT)
        PLAY_AGAIN_BUTTON.draw(GAME_OVER_MOUSE_POS)
        MAIN_MENU_BUTTON.draw(GAME_OVER_MOUSE_POS)
        QUIT_BUTTON.draw(GAME_OVER_MOUSE_POS)
        screen.blit(player_image, player_image_rect)
        screen.blit(player_text, player_text_rect)
        screen.blit(player_title, player_title_rect)

        for button in [PLAY_AGAIN_BUTTON, MAIN_MENU_BUTTON, QUIT_BUTTON]:
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

                if MAIN_MENU_BUTTON.is_hovered(GAME_OVER_MOUSE_POS):
                    from menus.main_menu import main_menu

                    game_settings.reset()
                    main_menu(screen)

                if QUIT_BUTTON.is_hovered(GAME_OVER_MOUSE_POS):
                    pygame.quit()
                    quit()

        clock.tick(properties.FPS)

        pygame.display.update()
