import pygame
import properties
from board import Board
from ui import ui
from button import Button


# Create the main menu
def menu(screen):
    pygame.display.set_caption("Menu")

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

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.is_clicked(MENU_MOUSE_POS):
                    play(screen)

                if QUIT_BUTTON.is_clicked(MENU_MOUSE_POS):
                    pygame.quit()
                    quit()

        pygame.display.update()


# Create the play function

# Create the board
board = Board()

# Frame rate
clock = pygame.time.Clock()
FPS = 60

# ui
ui = ui("Player 1", "Player 2")


def play(screen):
    board.reset()

    while True:
        screen.blit(properties.BACKGROUND_IMAGE, (0, 0))

        # Draw the board
        board.draw(screen)

        winner = board.winner
        if winner:
            game_over_screen(screen, winner)
            break

        # Draw the UI
        ui.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Handle mouse click on the board
                board.handle_click(event.pos)

        pygame.display.update()
        clock.tick(FPS)


# Create the game over screen
def game_over_screen(screen, winner):
    pygame.display.set_caption("Game Over Screen")

    overlay = pygame.Surface(screen.get_size())  # Create an alpha-enabled surface
    overlay.fill((0, 0, 0))  # Fill the surface with black
    overlay.set_alpha(150)  # Set the transparency level
    screen.blit(overlay, (0, 0))

    while True:

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

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_AGAIN_BUTTON.is_clicked(GAME_OVER_MOUSE_POS):
                    play(screen)
                    return True

                if MAIN_MENU_BUTTON.is_clicked(GAME_OVER_MOUSE_POS):
                    menu(screen)
                    return True

                if QUIT_BUTTON.is_clicked(GAME_OVER_MOUSE_POS):
                    pygame.quit()
                    quit()

        pygame.display.update()
