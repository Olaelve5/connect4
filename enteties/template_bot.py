from abc import ABC, abstractmethod
import pygame


class Template_Bot(ABC):
    def __init__(self, name, image_url):
        self.name = name
        self.image_url = image_url
        self.type = "bot"

    @abstractmethod
    def get_move(self, board):
        """Function to get the move of the bot"""
        pass

    def draw(self, screen, position):
        """Function to draw the bot on the screen"""
        image = pygame.image.load(self.image_url)
        scaled_image = pygame.transform.scale(image, (200, 200))
        screen.blit(scaled_image, position)
    