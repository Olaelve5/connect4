import pygame


class Player:
    def __init__(self, name, image_url):
        self.name = name
        self.image_url = image_url
        self.type = "human"

    def draw(self, screen, position):
        image = pygame.image.load(self.image_url)
        scaled_image = pygame.transform.scale(image, (200, 200))
        screen.blit(scaled_image, position)
    
    def get_move(self, board):
        pass