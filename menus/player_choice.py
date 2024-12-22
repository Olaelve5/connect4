import pygame
from enteties.player import Player

class Side_Button:
    def __init__(self, direction, x, y):
        self.direction = direction
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

    def is_clicked(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return self.direction
        return False


class Player_Choice:
    def __init__(self, screen):
        self.players = [
            Player("Player 1", "assets/robot.png"),
            Player("Player 2", "assets/human.png"),
        ]
        self.bots = []
        self.current_player = self.players[0]
        self.screen = screen

        self.left_button = Side_Button(-1, 0, 0)
        self.right_button = Side_Button(1, 750, 0)

    def add_bot(self, bot):
        self.bots.append(bot)
        if not self.current_player:
            self.current_player = bot
            self.image = bot.image

    def draw(self):
        if self.current_player:
            self.current_player.draw(self.screen, (0, 0))

        self.left_button.draw(self.screen)
        self.right_button.draw(self.screen)

    def switch_player(self, direction):
        all_players = self.players + self.bots
        current_index = all_players.index(self.current_player)
        new_index = current_index + direction
        if new_index < 0:
            new_index = len(all_players) - 1
        elif new_index >= len(all_players):
            new_index = 0
        self.current_player = all_players[new_index]
    

    def handle_click(self, mouse_pos):
        direction = self.left_button.is_clicked(mouse_pos)
        if direction:
            self.switch_player(direction)
            return

        direction = self.right_button.is_clicked(mouse_pos)
        if direction:
            self.switch_player(direction)
            return

        return self.current_player
