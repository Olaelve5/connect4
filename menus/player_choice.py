import pygame
from enteties.player import Player
import properties


class Side_Button:
    def __init__(self, direction, position):
        self.direction = direction
        self.position = position
        self.image = (
            pygame.image.load("assets/left_arrow.png")
            if direction == -1
            else pygame.image.load("assets/right_arrow.png")
        )
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return self.direction
        return False


class Player_Choice:
    def __init__(self, screen, position=(0, 0), player_1=True):
        self.players = [
            Player("Randobot", "assets/player_images/robot.png"),
            Player("Player", "assets/player_images/human.png"),
        ]
        self.bots = []
        self.current_player = (
            self.players[0]
            if player_1
            else (self.players[1] if len(self.players) > 1 else None)
        )
        self.screen = screen
        self.position = position
        self.rect = pygame.Rect(position, (200, 200))
        self.player_1 = player_1

        # Side button width is 50
        self.left_button = Side_Button(
            -1, (self.position[0] - 75, self.position[1] + 100)
        )
        self.right_button = Side_Button(
            1, (self.position[0] + self.rect.width + 75, self.position[1] + 100)
        )

    def add_bot(self, bot):
        self.bots.append(bot)
        if not self.current_player:
            self.current_player = bot
            self.image = bot.image

    def draw(self):
        # The player choice title
        title = properties.SUB_FONT.render(
            "Player 1" if self.player_1 else "Player 2", True, properties.WHITE
        )
        title_rect = title.get_rect(
            center=(self.position[0] + self.rect.width // 2, self.position[1] - 25)
        )
        self.screen.blit(title, title_rect)

        # The player choice active player
        name = properties.SUB_FONT.render(
            self.current_player.name, True, properties.WHITE
        )
        name_rect = name.get_rect(
            center=(
                self.position[0] + self.rect.width // 2,
                self.position[1] + self.rect.height + 40,
            )
        )
        self.screen.blit(name, name_rect)

        if self.current_player:
            self.current_player.draw(self.screen, self.position)

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
