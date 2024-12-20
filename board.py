import properties
from slot import Slot
import pygame
import game_mechanics
from game_over import game_over_screen


class Board:
    def __init__(self):
        self.columns = []
        for i in range(7):
            self.columns.append(Column(i))
        self.slots = []
        for column in self.columns:
            for slot in column.slots:
                self.slots.append(slot)
        self.player = 1  # Player 1 starts
        self.winner = None

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            properties.BLUE,
            (
                (properties.WINDOW_WIDTH - properties.BOARD_WIDTH) // 2,
                (properties.WINDOW_HEIGHT - properties.BOARD_HEIGHT) // 2 + properties.VERTICAL_GAP // 2,
                properties.BOARD_WIDTH,
                properties.BOARD_HEIGHT,
            ),
            0,
            10,
        )
        for column in self.columns:
            column.draw(screen)

    def handle_click(self, mouse_pos):
        for column in self.columns:
            if column.rect.collidepoint(
                mouse_pos
            ):  # Check if mouse is inside the column
                column.handle_click(self.player)
                self.check_winner()
                self.switch_player()
                break

    def switch_player(self):
        self.player = 1 if self.player == 2 else 2

    def check_winner(self):
        winnner = game_mechanics.check_winner(self)
        if winnner:
            self.winner = winnner


class Column(pygame.sprite.Sprite):
    def __init__(self, index):
        super().__init__()
        self.height = properties.BOARD_HEIGHT
        self.width = properties.COLUMN_WIDTH
        self.color = (0, 0, 0, 0)
        self.slots = []
        self.index = index

        # Calculate position of the column
        board_x = (properties.WINDOW_WIDTH - properties.BOARD_WIDTH) // 2
        self.x = board_x + index * self.width
        self.y = (properties.WINDOW_HEIGHT - properties.BOARD_HEIGHT) // 2 + properties.VERTICAL_GAP // 2

        # Create a rect for collision detection
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Create the slots
        for i in range(6):
            self.slots.append(Slot((index, i), 0))

    def draw(self, screen):
        for slot in self.slots:
            slot.draw(screen)

    def handle_click(self, player):
        for slot in self.slots:
            if slot.player == 0:
                slot.update(player)
                break
