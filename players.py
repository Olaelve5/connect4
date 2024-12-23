from enteties.bots.randobot import Randobot
from enteties.player import Player
from enteties.bots.ditto import Ditto
from enteties.bots.randotron import Randotron

# Players/bots
players = [
    Player("Human", "assets/player_images/human.png"),
    Randobot("Randobot", "assets/player_images/robot.png"),
    Ditto("Ditto", "assets/player_images/ditto.png"),
    Randotron("Randotron", "assets/player_images/randotron.png"),
]