import pygame


class Cursor:
    def __init__(self, screen):
        self.mode = "default"
        self.screen = screen
        self.scale = (70, 70)
        self.image = pygame.transform.scale(
            pygame.image.load("assets/cursor/default_cursor.png"), self.scale
        )
        self.rect = self.image.get_rect()

    def draw(self, mouse_pos):
        cursor_pos = (
            mouse_pos[0] - self.rect.width // 2,
            mouse_pos[1] - self.rect.height // 2,
        )
        self.screen.blit(self.image, cursor_pos)

    def set_mode(self, mode):
        self.mode = mode

        if mode == "default":
            self.image = pygame.transform.scale(
                pygame.image.load("assets/cursor/default_cursor.png"), self.scale
            )
        elif mode == "click":
            self.image = pygame.transform.scale(
                pygame.image.load("assets/cursor/click_cursor.png"), self.scale
            )

        elif mode == "drop_1":
            self.image = pygame.transform.scale(
                pygame.image.load("assets/cursor/1_drop_cursor.png"), self.scale
            )

        elif mode == "drop_2":
            self.image = pygame.transform.scale(
                pygame.image.load("assets/cursor/2_drop_cursor.png"), self.scale
            )
