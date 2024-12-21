import pygame
from enteties.player import Player


class Player_Choice:
    def __init__(self, screen):
        self.players = [
            Player("Player 1", "assets/human.png"),
            Player("Player 2", "assets/human.png"),
        ]
        self.bots = []
        self.current_player = self.players[0]
        self.screen = screen

    def add_bot(self, bot):
        self.bots.append(bot)
        if not self.current_player:
            self.current_player = bot
            self.image = bot.image

    def draw(self):
        if self.current_player:
            self.current_player.draw(self.screen, (0, 0))

    def switch_player(self, direction):
        all_players = self.players + self.bots
        current_index = all_players.index(self.current_player)
        new_index = current_index + direction
        if new_index < 0:
            new_index = len(all_players) - 1
        elif new_index >= len(all_players):
            new_index = 0
        self.current_player = all_players[new_index]
