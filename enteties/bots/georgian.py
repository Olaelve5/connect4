from enteties.template_bot import Template_Bot
from board.board import Board
from gameplay.game_mechanics import check_winner
import random


class Georgian(Template_Bot):
    def __init__(self, name, image_url):
        super().__init__(name, image_url)

    def get_move(self, board: Board):
        top_move = None
        top_score = -10000000000

        for move in board.available_columns():
            score = self.calculate_move(board, move)
            if score > top_score:
                top_score = score
                top_move = move

        return top_move

    def calculate_move(self, board: Board, move):

        board_copy = board.copy()
        board_copy.make_move(move)
        score = 0

        if check_winner(board_copy) == self.player:
            return 1000000

        score += self.calculate_self_score(board_copy)
        score -= self.calculate_oponent_score(board_copy)

        return score

    def calculate_self_score(self, board: Board):
        score = 0

        for column in board.columns:
            for row in range(2):
                if (
                    column.slots[row].player
                    == column.slots[row + 1].player
                    == column.slots[row + 2].player
                    == self.player
                    and column.slots[row + 3].player == 0
                ):
                    score += 100
                    continue

                elif (
                    column.slots[row].player
                    == column.slots[row + 1].player
                    == self.player
                    and column.slots[row + 2].player == 0
                ):
                    score += 50
                    continue

                elif (
                    column.slots[row].player == self.player
                    and column.slots[row + 1].player == 0
                ):
                    score += 10
                    continue

        # check for horizontal score
        for row in range(6):
            for column in range(3):
                if (
                    board.columns[column].slots[row].player
                    == board.columns[column + 1].slots[row].player
                    == board.columns[column + 2].slots[row].player
                    == self.player
                    and board.columns[column + 3].slots[row].player == 0
                ):
                    score += 100
                    continue

                elif (
                    board.columns[column].slots[row].player
                    == board.columns[column + 1].slots[row].player
                    == self.player
                    and board.columns[column + 2].slots[row].player == 0
                ):
                    score += 50
                    continue

                elif (
                    board.columns[column].slots[row].player == self.player
                    and board.columns[column + 1].slots[row].player == 0
                ):
                    score += 10
                    continue

        # check for diagonal score
        for column in range(4):
            for row in range(3):
                if (
                    board.columns[column].slots[row].player
                    == board.columns[column + 1].slots[row + 1].player
                    == board.columns[column + 2].slots[row + 2].player
                    == self.player
                    and board.columns[column + 3].slots[row + 3].player == 0
                ):
                    score += 100
                    continue

                elif (
                    board.columns[column].slots[row].player
                    == board.columns[column + 1].slots[row + 1].player
                    == self.player
                    and board.columns[column + 2].slots[row + 2].player == 0
                ):
                    score += 50
                    continue

                elif (
                    board.columns[column].slots[row].player == self.player
                    and board.columns[column + 1].slots[row + 1].player == 0
                ):
                    score += 10
                    continue

        # return the score with some randomness
        return score + random.randint(-5, 5)

    # calculate the score of the oponent
    def calculate_oponent_score(self, board: Board):
        oponent = 1 if self.player == 2 else 2
        score = 0

        for column in board.available_columns():
            board_copy = board.copy()
            board_copy.make_move(column)
            if check_winner(board_copy) == oponent:
               return 100000000


        for column in board.columns:
            for row in range(2):
                if (
                    column.slots[row].player
                    == column.slots[row + 1].player
                    == column.slots[row + 2].player
                    == oponent
                    and column.slots[row + 3].player == 0
                ):
                    score += 100
                    continue

                elif (
                    column.slots[row].player == column.slots[row + 1].player == oponent
                    and column.slots[row + 2].player == 0
                ):
                    score += 50
                    continue

                elif (
                    column.slots[row].player == oponent
                    and column.slots[row + 1].player == 0
                ):
                    score += 10
                    continue

        # check for horizontal score
        for row in range(6):
            for column in range(3):
                if (
                    board.columns[column].slots[row].player
                    == board.columns[column + 1].slots[row].player
                    == board.columns[column + 2].slots[row].player
                    == oponent
                    and board.columns[column + 3].slots[row].player == 0
                ):
                    score += 100
                    continue

                elif (
                    board.columns[column].slots[row].player
                    == board.columns[column + 1].slots[row].player
                    == oponent
                    and board.columns[column + 2].slots[row].player == 0
                ):
                    score += 50
                    continue

                elif (
                    board.columns[column].slots[row].player == oponent
                    and board.columns[column + 1].slots[row].player == 0
                ):
                    score += 10
                    continue

        # check for diagonal score
        for column in range(4):
            for row in range(3):
                if (
                    board.columns[column].slots[row].player
                    == board.columns[column + 1].slots[row + 1].player
                    == board.columns[column + 2].slots[row + 2].player
                    == oponent
                    and board.columns[column + 3].slots[row + 3].player == 0
                ):
                    score += 100
                    continue

                elif (
                    board.columns[column].slots[row].player
                    == board.columns[column + 1].slots[row + 1].player
                    == oponent
                    and board.columns[column + 2].slots[row + 2].player == 0
                ):
                    score += 50
                    continue

                elif (
                    board.columns[column].slots[row].player == oponent
                    and board.columns[column + 1].slots[row + 1].player == 0
                ):
                    score += 10
                    continue

        return score + random.randint(-5, 5)
