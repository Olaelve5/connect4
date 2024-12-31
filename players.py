from enteties.bots.randobot import Randobot
from enteties.player import Player
from enteties.bots.ditto import Ditto
from enteties.bots.randotron import Randotron
from enteties.bots.georgian import Georgian
from enteties.bots.el_gato import El_Gato
from settings.game_settings import Game_Settings

# Step 1: Initialize Game_Settings without players
game_settings = Game_Settings(None, None)

# Step 2: Create players/bots
players = [
    Player("Human", "assets/player_images/human.png"),
    Randobot("Randobot", "assets/player_images/robot.png"),
    Ditto("Ditto", "assets/player_images/ditto.png"),
    Randotron("Randotron", "assets/player_images/randotron.png"),
    Georgian("Georgian", "assets/player_images/georgian.png"),
    El_Gato(
        "El Gato",
        "assets/player_images/torres.png",
        game_settings.env,
        model_path="dqn_model.zip",  # Path to the saved model
    ),
]

game_settings.env.agent = 1

# Step 3: Update players in game_settings
game_settings.player_1 = players[0]
game_settings.player_2 = players[0]
