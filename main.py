import pygame
import properties
from menus.main_menu import main_menu
from enteties.player import Player
from enteties.bot import Bot

pygame.init()

# Create the screen with the size of the client's screen
screen = pygame.display.set_mode(
    (properties.WINDOW_WIDTH, properties.WINDOW_HEIGHT), pygame.FULLSCREEN
)
screen.fill(properties.BACKGROUND)
pygame.display.set_caption("Connect 4")
pygame.mouse.set_visible(False)

main_menu(screen)
