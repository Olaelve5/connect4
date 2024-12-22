import pygame
import properties
from cursor import Cursor
from menus.button import Button
from menus.player_choice import Player_Choice


# Create the main menu
def main_menu(screen):
    pygame.display.set_caption("Menu")
    player_choice = Player_Choice(screen)

    cursor = Cursor(screen)

    while True:
        screen.blit(properties.BACKGROUND_IMAGE, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TITLE = properties.TITLE_FONT.render("Connect 4", True, properties.WHITE)
        MENU_TITLE_RECT = MENU_TITLE.get_rect(center=(properties.WINDOW_WIDTH / 2, 100))

        PLAY_BUTTON = Button(
            "Play",
            properties.WINDOW_WIDTH / 2,
            300,
            properties.TITLE_FONT,
            properties.WHITE,
            screen,
        )
        QUIT_BUTTON = Button(
            "Quit",
            properties.WINDOW_WIDTH / 2,
            400,
            properties.TITLE_FONT,
            properties.WHITE,
            screen,
        )

        screen.blit(MENU_TITLE, MENU_TITLE_RECT)
        PLAY_BUTTON.draw(MENU_MOUSE_POS)
        QUIT_BUTTON.draw(MENU_MOUSE_POS)

        # Draw player choice
        player_choice.draw()

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            if button.is_clicked(MENU_MOUSE_POS):
                cursor.set_mode("click")
                break
            else:
                cursor.set_mode("default")

        cursor.draw(MENU_MOUSE_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.is_clicked(MENU_MOUSE_POS):
                    from play import play
                    play(screen)

                if QUIT_BUTTON.is_clicked(MENU_MOUSE_POS):
                    pygame.quit()
                    quit()
                
                player_choice.handle_click(MENU_MOUSE_POS)


        pygame.display.update()
