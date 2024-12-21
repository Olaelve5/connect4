import pygame
import properties
from board import Board
from ui import ui
from button import Button
from cursor import Cursor


# Create the main menu
def menu(screen):
    pygame.display.set_caption("Menu")

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
    cursor = Cursor(screen)

    pygame.mouse.set_visible(False)

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

        # Draw the cursor
        cursor.draw(pygame.mouse.get_pos())

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

    pygame.mouse.set_visible(False)
    cursor = Cursor(screen)

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
                    play(screen)
                    return True

                if MAIN_MENU_BUTTON.is_clicked(GAME_OVER_MOUSE_POS):
                    menu(screen)
                    return True

                if QUIT_BUTTON.is_clicked(GAME_OVER_MOUSE_POS):
                    pygame.quit()
                    quit()

        pygame.display.update()
