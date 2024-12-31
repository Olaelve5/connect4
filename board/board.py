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
        self.player_turn = 1  # Player 1 starts
        self.winner = None
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
                self.make_move(column.index)

    def make_move(self, column):
        if column is None:
            return random.choice(self.available_columns())

        altered = self.columns[column].handle_click(self.player_turn)
        if not altered:
            return

        self.last_move = column
        self.check_winner()
        self.switch_player()

    def switch_player(self):
        self.player_turn = 1 if self.player_turn == 2 else 2
        for slot in self.slots:
            slot.player_turn = self.player_turn

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

    def check_winner(self):
        winnner = game_mechanics.check_winner(self)
        if winnner:
            self.winner = winnner

    def is_valid_move(self, column):
        return self.columns[column].is_valid_move()

    def reset(self):
        for slot in self.slots:
            slot.update(0)
        self.player_turn = 1
        self.winner = None

    def copy(self):
        return copy.deepcopy(self)

    def is_winning_move(self, move):
        board = self.copy()
        board.make_move(move)
        return board.winner == self.player_turn

    def is_loosing_move(self, move):
        board = self.copy()
        board.make_move(move)

        for column in board.available_columns():
            if board.is_winning_move(column):
                return True

        return False
