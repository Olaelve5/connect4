import pygame
import settings.properties as properties
from menus.main_menu import main_menu
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.vec_env import DummyVecEnv
from environment.connect4Env import Connect4Env
from menus.player_manager import Player_Manager
from enteties.player import Player
from Progg_Pils.ola.bots.randobot import Randobot
from Progg_Pils.ola.bots.dalejandro import Randotron


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

# Add players to the player manager
player_manager = Player_Manager()
player_manager.add_player(Player())
player_manager.add_player(Randobot())
player_manager.add_player(Randotron())

env = Connect4Env(player_manager)
check_env(env)

vec_env = DummyVecEnv([lambda: env])

# Pass the original environment to main_menu
main_menu(screen, vec_env.envs[0])
