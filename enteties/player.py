import pygame


class Player:
    def __init__(self):
        self.name = "Human"
        self.image_url = "assets/player_images/human.png"
        self.type = "human"
        self.sound = None

    def draw(self, screen, position):
        image = pygame.image.load(self.image_url)
        scaled_image = pygame.transform.scale(image, (200, 200))
        screen.blit(scaled_image, position)

    def get_move(self, board):
        pass
