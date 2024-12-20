import pygame
import properties


def game_over_screen(screen, winner):
    pygame.display.set_caption("Game Over Screen")

    while True:
        screen.fill((0, 0, 0, 120))

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

        QUIT_BUTTON = properties.TITLE_FONT.render("Quit", True, properties.WHITE)
        QUIT_BUTTON_RECT = QUIT_BUTTON.get_rect(
            center=(properties.WINDOW_WIDTH / 2, 400)
        )

        screen.blit(GAME_OVER_TITLE, GAME_OVER_TITLE_RECT)
        screen.blit(PLAY_AGAIN_BUTTON, PLAY_AGAIN_BUTTON_RECT)
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
                    return True

                if QUIT_BUTTON_RECT.collidepoint(GAME_OVER_MOUSE_POS):
                    pygame.quit()
                    quit()

        pygame.display.update()
