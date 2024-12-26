import properties
from menus.main_menu import main_menu
from menus.button import Button
import pygame
from cursor import Cursor


def mode_menu(screen, selected_mode="Single Game"):

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
        "Continous 10",
        properties.WINDOW_WIDTH / 2,
        properties.WINDOW_HEIGHT - 500,
        properties.FONT,
        properties.WHITE,
        screen,
    )

    continous_25_button = Button(
        "Continous 25",
        properties.WINDOW_WIDTH / 2,
        properties.WINDOW_HEIGHT - 400,
        properties.FONT,
        properties.WHITE,
        screen,
    )

    continous_50_button = Button(
        "Continous 50",
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
            if button.text == selected_mode:
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
                if single_button.is_hovered(mouse_pos):
                    selected_mode = single_button.text
                    print(selected_mode)
                if continous_10_button.is_hovered(mouse_pos):
                    selected_mode = continous_10_button.text
                    print(selected_mode)
                if continous_25_button.is_hovered(mouse_pos):
                    selected_mode = continous_25_button.text
                if continous_50_button.is_hovered(mouse_pos):
                    selected_mode = continous_50_button.text
                if back_button.is_hovered(mouse_pos):
                    return main_menu(screen, selected_mode)

        cursor.draw(mouse_pos)

        pygame.display.update()
        clock.tick(properties.FPS)
