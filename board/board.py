import settings.properties as properties
import pygame
import gameplay.game_mechanics as game_mechanics
from board.column import Column
import copy
import random


class Board:
    def __init__(self):
        self.columns = []
        for i in range(7):
            self.columns.append(Column(i))
        self.slots = []
        for column in self.columns:
            for slot in column.slots:
                self.slots.append(slot)
        self.last_move = None

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
                if column.handle_click():
                    self.last_move = column.index
                    return column.index
        return None

    def make_move(self, column, player=0):
        if column is None:
            return random.choice(self.available_columns())

        altered = self.columns[column].make_move(player)
        if not altered:
            return

        self.last_move = column

        for slot in self.slots:
            slot.player_turn = player

    def available_columns(self):
        if game_mechanics.check_full(self):
            return []

        moves = []
        for column in self.columns:
            for slot in column.slots:
                if slot.player == 0:
                    moves.append(column.index)
                    break

        return moves

    def is_valid_move(self, column):
        return self.columns[column].is_valid_move()

    def reset(self):
        for slot in self.slots:
            slot.update(0)
        self.player_turn = 1
        self.winner = None

    def copy(self):
        return copy.deepcopy(self)

    def __str__(self):
        board = ""
        for i in range(6):
            for column in self.columns:  # Iterate over the columns in reverse order
                board += str(column.slots[::-1][i].player) + " "
            board += "\n"
        return board
