import pygame
import settings.properties as properties
from menus.main_menu import main_menu
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.vec_env import DummyVecEnv
from players import game_settings

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

check_env(game_settings.env)

env = DummyVecEnv([lambda: game_settings.env])

main_menu(screen, game_settings)
