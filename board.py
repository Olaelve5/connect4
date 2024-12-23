import properties
from slot import Slot
import pygame
import gameplay.game_mechanics as game_mechanics


class Board:
    def __init__(self):
        self.columns = []
        for i in range(7):
            self.columns.append(Column(i))
        self.slots = []
        for column in self.columns:
            for slot in column.slots:
                self.slots.append(slot)
        self.player_turn = 1  # Player 1 starts
        self.winner = None

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            properties.BLUE,
            (
                (properties.WINDOW_WIDTH - properties.BOARD_WIDTH) // 2,
                (properties.WINDOW_HEIGHT - properties.BOARD_HEIGHT) // 2
                + properties.VERTICAL_GAP // 2,
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
                self.make_move(column.index)

        for slot in self.slots:
            slot.player_turn = self.player_turn
    
    def make_move(self, column):
        altered = self.columns[column].handle_click(self.player_turn)
        if not altered:
            return

        self.check_winner()
        self.switch_player()

    def switch_player(self):
        self.player_turn = 1 if self.player_turn == 2 else 2

    def check_winner(self):
        winnner = game_mechanics.check_winner(self)
        if winnner:
            self.winner = winnner

    def reset(self):
        for slot in self.slots:
            slot.update(0)
        self.player_turn = 1
        self.winner = None


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
        self.y = (
            properties.WINDOW_HEIGHT - properties.BOARD_HEIGHT
        ) // 2 + properties.VERTICAL_GAP // 2

        # Create a rect for collision detection
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Create the slots
        for i in range(6):
            self.slots.append(Slot((index, i), 0))

    def draw(self, screen):
        for slot in self.slots:
            slot.draw(screen)

    def hovered_draw(self, screen):
        for slot in self.slots:
            if slot.player == 0:
                slot.hovered_draw(screen)
                break

    def handle_click(self, player):
        if self.slots[5].player != 0:
            return False

        for slot in self.slots:
            if slot.player == 0:
                slot.update(player)
                break
        return True

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
