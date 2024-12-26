import pygame
import properties
from cursor import Cursor
from menus.button import Button
from menus.player_choice import Player_Choice
from players import players


# Create the main menu
def main_menu(screen, selected_mode="Single Game"):
    pygame.display.set_caption("Menu")
    player_choice_1 = Player_Choice(
        screen, (properties.WINDOW_WIDTH / 5, 250), True, players
    )
    player_choice_2 = Player_Choice(
        screen, (properties.WINDOW_WIDTH / 5 * 4 - 200, 250), False, players
    )

    cursor = Cursor(screen)

    MENU_TITLE = properties.TITLE_FONT.render("Connect 4", True, properties.WHITE)
    MENU_TITLE_RECT = MENU_TITLE.get_rect(center=(properties.WINDOW_WIDTH / 2, 100))

    selected_text = properties.SUB_FONT.render(selected_mode, True, properties.YELLOW)
    selected_text_rect = selected_text.get_rect(
        center=(properties.WINDOW_WIDTH / 2, 160)
    )

    PLAY_BUTTON = Button(
        "Play",
        properties.WINDOW_WIDTH / 2,
        properties.WINDOW_HEIGHT - 300,
        properties.FONT,
        properties.WHITE,
        screen,
    )

    MODE_BUTTON = Button(
        "Choose Mode",
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

    buttons = [
        PLAY_BUTTON,
        QUIT_BUTTON,
        MODE_BUTTON,
        player_choice_1.left_button,
        player_choice_1.right_button,
        player_choice_2.left_button,
        player_choice_2.right_button,
    ]

    # Sounds
    hover_sound = pygame.mixer.Sound("assets/sounds/hover_button.mp3")

    last_hovered_button = None

    clock = pygame.time.Clock()

    while True:
        screen.blit(properties.BACKGROUND_IMAGE, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(MENU_TITLE, MENU_TITLE_RECT)
        screen.blit(selected_text, selected_text_rect)
        PLAY_BUTTON.draw(MENU_MOUSE_POS)
        QUIT_BUTTON.draw(MENU_MOUSE_POS)
        MODE_BUTTON.draw(MENU_MOUSE_POS)

        # Draw player choice
        player_choice_1.draw()
        player_choice_2.draw()

        hovered_button = None

        for button in buttons:
            if button.is_hovered(MENU_MOUSE_POS):
                hovered_button = button
                cursor.set_mode("click")
                break
            else:
                cursor.set_mode("default")

        # Play hover sound only if the hovered button changes
        if hovered_button != last_hovered_button:
            if hovered_button is not None:  # Only play if hovering over a button
                hover_sound.play()
            last_hovered_button = hovered_button

        cursor.draw(MENU_MOUSE_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.is_hovered(MENU_MOUSE_POS):
                    from gameplay.play import play

                    play(
                        screen,
                        player_choice_1.current_player,
                        player_choice_2.current_player,
                    )

                if MODE_BUTTON.is_hovered(MENU_MOUSE_POS):
                    from menus.mode_menu import mode_menu

                    mode_menu(screen, selected_mode)

                if QUIT_BUTTON.is_hovered(MENU_MOUSE_POS):
                    pygame.quit()
                    quit()

                player_choice_1.handle_click(MENU_MOUSE_POS)
                player_choice_2.handle_click(MENU_MOUSE_POS)

        clock.tick(properties.FPS)

        pygame.display.update()
