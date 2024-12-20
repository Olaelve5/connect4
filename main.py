import pygame
import properties
from play import play

pygame.init()

# Create the screen with the size of the client's screen
screen = pygame.display.set_mode(
    (properties.WINDOW_WIDTH, properties.WINDOW_HEIGHT), pygame.FULLSCREEN
)
screen.fill(properties.BACKGROUND)
pygame.display.set_caption("Connect 4")


def menu(screen):
    pygame.display.set_caption("Menu")

    while True:
        screen.fill(properties.BACKGROUND)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TITLE = properties.TITLE_FONT.render("Connect 4", True, properties.WHITE)
        MENU_TITLE_RECT = MENU_TITLE.get_rect(center=(properties.WINDOW_WIDTH / 2, 100))

        PLAY_BUTTON = properties.TITLE_FONT.render("Play", True, properties.WHITE)
        PLAY_BUTTON_RECT = PLAY_BUTTON.get_rect(
            center=(properties.WINDOW_WIDTH / 2, 300)
        )

        QUIT_BUTTON = properties.TITLE_FONT.render("Quit", True, properties.WHITE)
        QUIT_BUTTON_RECT = QUIT_BUTTON.get_rect(
            center=(properties.WINDOW_WIDTH / 2, 400)
        )

        screen.blit(MENU_TITLE, MENU_TITLE_RECT)
        screen.blit(PLAY_BUTTON, PLAY_BUTTON_RECT)
        screen.blit(QUIT_BUTTON, QUIT_BUTTON_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON_RECT.collidepoint(MENU_MOUSE_POS):
                    play(screen)
                
                if QUIT_BUTTON_RECT.collidepoint(MENU_MOUSE_POS):
                    pygame.quit()
                    quit()

        pygame.display.update()


menu(screen)
