from enteties.bots.randobot import Randobot
from enteties.player import Player
from enteties.bots.ditto import Ditto
from enteties.bots.randotron import Randotron
from enteties.bots.georgian import Georgian
from enteties.bots.torres import Torres

# Players/bots
players = [
    Player("Human", "assets/player_images/human.png"),
    Randobot("Randobot", "assets/player_images/robot.png"),
    Ditto("Ditto", "assets/player_images/ditto.png"),
    Randotron("Randotron", "assets/player_images/randotron.png"),
    Georgian("Georgian", "assets/player_images/georgian.png"),
    Torres("Torres", "assets/player_images/torres.png")
]