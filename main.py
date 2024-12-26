import pygame
import settings.properties as properties
from menus.main_menu import main_menu
from settings.game_settings import Game_Settings
from players import players

pygame.init()

pygame.mixer.init()
pygame.mixer.set_num_channels(64)

# Create the screen with the size of the client's screen
screen = pygame.display.set_mode(
    (properties.WINDOW_WIDTH, properties.WINDOW_HEIGHT), pygame.FULLSCREEN
)
screen.fill(properties.BACKGROUND)
pygame.display.set_caption("Connect 4")
pygame.mouse.set_visible(False)

game_settings = Game_Settings(players[0], players[0])

main_menu(screen, game_settings)
