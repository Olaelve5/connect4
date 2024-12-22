import pygame
import properties
from menus.button import Button
from cursor import Cursor

# Create the game over screen
def game_over_menu(screen, winner):
    pygame.display.set_caption("Game Over Screen")

    pygame.mouse.set_visible(False)
    cursor = Cursor(screen)

    clock = pygame.time.Clock()

    while True:
        screen.blit(properties.BACKGROUND_IMAGE, (0, 0))

        GAME_OVER_MOUSE_POS = pygame.mouse.get_pos()

        GAME_OVER_TITLE = properties.TITLE_FONT.render(
            str(winner) + " wins!", True, properties.WHITE
        )
        GAME_OVER_TITLE_RECT = GAME_OVER_TITLE.get_rect(
            center=(properties.WINDOW_WIDTH / 2, 100)
        )

        PLAY_AGAIN_BUTTON = Button(
            "Play Again",
            properties.WINDOW_WIDTH / 2,
            300,
            properties.TITLE_FONT,
            properties.WHITE,
            screen,
        )

        MAIN_MENU_BUTTON = Button(
            "Main Menu",
            properties.WINDOW_WIDTH / 2,
            400,
            properties.TITLE_FONT,
            properties.WHITE,
            screen,
        )

        QUIT_BUTTON = Button(
            "Quit",
            properties.WINDOW_WIDTH / 2,
            500,
            properties.TITLE_FONT,
            properties.WHITE,
            screen,
        )

        screen.blit(GAME_OVER_TITLE, GAME_OVER_TITLE_RECT)
        PLAY_AGAIN_BUTTON.draw(GAME_OVER_MOUSE_POS)
        MAIN_MENU_BUTTON.draw(GAME_OVER_MOUSE_POS)
        QUIT_BUTTON.draw(GAME_OVER_MOUSE_POS)

        for button in [PLAY_AGAIN_BUTTON, MAIN_MENU_BUTTON, QUIT_BUTTON]:
            if button.is_clicked(GAME_OVER_MOUSE_POS):
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
                if PLAY_AGAIN_BUTTON.is_clicked(GAME_OVER_MOUSE_POS):
                    from gameplay.play import play
                    play(screen)
                    return True

                if MAIN_MENU_BUTTON.is_clicked(GAME_OVER_MOUSE_POS):
                    from menus.main_menu import main_menu
                    main_menu(screen)
                    return True

                if QUIT_BUTTON.is_clicked(GAME_OVER_MOUSE_POS):
                    pygame.quit()
                    quit()

        clock.tick(properties.FPS)

        pygame.display.update()
