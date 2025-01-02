import settings.properties as properties
from menus.main_menu import main_menu
from menus.button import Button
import pygame
from cursor import Cursor
from environment.connect4Env import Connect4Env


def mode_menu(screen, env: Connect4Env):

    title = properties.TITLE_FONT.render("Choose Mode", True, properties.WHITE)
    title_rect = title.get_rect(center=(properties.WINDOW_WIDTH / 2, 100))

    single_button = Button(
        "Single Game",
        properties.WINDOW_WIDTH / 2,
        properties.WINDOW_HEIGHT - 600,
        properties.FONT,
        properties.WHITE,
        screen,
    )

    continous_10_button = Button(
        "Continous 25",
        properties.WINDOW_WIDTH / 2,
        properties.WINDOW_HEIGHT - 500,
        properties.FONT,
        properties.WHITE,
        screen,
    )

    continous_25_button = Button(
        "Continous 50",
        properties.WINDOW_WIDTH / 2,
        properties.WINDOW_HEIGHT - 400,
        properties.FONT,
        properties.WHITE,
        screen,
    )

    continous_50_button = Button(
        "Continous 100",
        properties.WINDOW_WIDTH / 2,
        properties.WINDOW_HEIGHT - 300,
        properties.FONT,
        properties.WHITE,
        screen,
    )

    back_button = Button(
        "Go Back",
        properties.WINDOW_WIDTH / 2,
        properties.WINDOW_HEIGHT - 100,
        properties.FONT,
        properties.WHITE,
        screen,
    )

    buttons = [
        single_button,
        continous_10_button,
        continous_25_button,
        continous_50_button,
        back_button,
    ]

    cursor = Cursor(screen)

    clock = pygame.time.Clock()

    while True:
        screen.blit(properties.BACKGROUND_IMAGE, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        screen.blit(title, title_rect)

        for button in buttons:
            if button.text == env.selected_mode:
                button.selected_draw()
            else:
                button.draw(mouse_pos)

        for button in buttons:
            if button.is_hovered(mouse_pos):
                cursor.set_mode("click")
                break
            else:
                cursor.set_mode("default")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_hovered(mouse_pos):
                    return main_menu(screen, env)

                for button in buttons:
                    if button.is_hovered(mouse_pos):
                        env.selected_mode = button.text

        cursor.draw(mouse_pos)

        pygame.display.update()
        clock.tick(properties.FPS)
