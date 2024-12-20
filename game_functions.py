import pygame
import properties
from board import Board
from ui import ui


# Create the main menu
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
        screen.fill(properties.BACKGROUND)

        # Draw the board
        board.draw(screen)

        winner = board.winner
        if winner:
            game_over_screen(screen, winner)
            break

        # Draw the UI
        ui.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
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

    overlay = pygame.Surface(
        screen.get_size(), pygame.SRCALPHA
    )  # Create an alpha-enabled surface
    overlay.fill((0, 0, 0, 120))

    while True:
        screen.blit(overlay, (0, 0))

        GAME_OVER_TITLE = properties.TITLE_FONT.render(
            str(winner) + " wins!", True, properties.WHITE
        )
        GAME_OVER_TITLE_RECT = GAME_OVER_TITLE.get_rect(
            center=(properties.WINDOW_WIDTH / 2, 100)
        )

        PLAY_AGAIN_BUTTON = properties.TITLE_FONT.render(
            "Play Again", True, properties.WHITE
        )
        PLAY_AGAIN_BUTTON_RECT = PLAY_AGAIN_BUTTON.get_rect(
            center=(properties.WINDOW_WIDTH / 2, 300)
        )

        MAIN_MENU_BUTTON = properties.TITLE_FONT.render(
            "Main Menu", True, properties.WHITE
        )
        MAIN_MENU_BUTTON_RECT = MAIN_MENU_BUTTON.get_rect(
            center=(properties.WINDOW_WIDTH / 2, 350)
        )

        QUIT_BUTTON = properties.TITLE_FONT.render("Quit", True, properties.WHITE)
        QUIT_BUTTON_RECT = QUIT_BUTTON.get_rect(
            center=(properties.WINDOW_WIDTH / 2, 400)
        )

        screen.blit(GAME_OVER_TITLE, GAME_OVER_TITLE_RECT)
        screen.blit(PLAY_AGAIN_BUTTON, PLAY_AGAIN_BUTTON_RECT)
        screen.blit(MAIN_MENU_BUTTON, MAIN_MENU_BUTTON_RECT)
        screen.blit(QUIT_BUTTON, QUIT_BUTTON_RECT)

        GAME_OVER_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_AGAIN_BUTTON_RECT.collidepoint(GAME_OVER_MOUSE_POS):
                    play(screen)
                    return True
                
                if MAIN_MENU_BUTTON_RECT.collidepoint(GAME_OVER_MOUSE_POS):
                    menu(screen)
                    return True

                if QUIT_BUTTON_RECT.collidepoint(GAME_OVER_MOUSE_POS):
                    pygame.quit()
                    quit()

        pygame.display.update()