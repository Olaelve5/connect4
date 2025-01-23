from abc import ABC, abstractmethod
import pygame


class Template_Bot(ABC):
    def __init__(self, name, type="bot"):
        self.name = name
        self.image_url = "assets/player_images/robot.png"
        self.type = type
        self.player = None

    @abstractmethod
    def get_move(self, board):
        """Function to get the move of the bot"""
        """Returns the index of the column - 0 to 6"""
        pass

    def draw(self, screen, position):
        """Function to draw the bot on the screen"""
        image = pygame.image.load(self.image_url)
        scaled_image = pygame.transform.scale(image, (200, 200))
        screen.blit(scaled_image, position)
