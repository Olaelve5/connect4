from enteties.template_bot import Template_Bot
from board.board import Board
from gameplay.game_mechanics import check_winner
import random


class Georgian(Template_Bot):
    def __init__(self, name, image_url, player=None):
        super().__init__(name, image_url)
        self.player = player

    def get_move(self, board: Board):
        top_moves = []
        top_score = -10000000000

        for move in board.available_columns():
            board.make_move(move, self.player)
            score = self.calculate_move(board)
            board.revert_move()

            if score > top_score:
                # New top score, reset the list
                top_score = score
                top_moves = [move]
            elif score == top_score:
                # Add to the list of top-scoring moves
                top_moves.append(move)

        # Randomly select one of the top-scoring moves
        return random.choice(top_moves)


    def calculate_move(self, board: Board):
        score = 0

        if check_winner(board) == self.player:
            return 1000000

        score += self.calculate_self_score(board)
        score -= self.calculate_opponent_score(board)

        return score

    def calculate_self_score(self, board: Board):
        score = 0

        # check vertical score
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
        return score

    # calculate the score of the opponent
    def calculate_opponent_score(self, board: Board):
        opponent = 1 if self.player == 2 else 2
        score = 0

        for column in board.available_columns():
            board.make_move(column, opponent)
            if check_winner(board) == opponent:
                board.revert_move()
                return 100000000
            board.revert_move()

        for column in board.columns:
            for row in range(2):
                if (
                    column.slots[row].player
                    == column.slots[row + 1].player
                    == column.slots[row + 2].player
                    == opponent
                    and column.slots[row + 3].player == 0
                ):
                    score += 100
                    continue

                elif (
                    column.slots[row].player == column.slots[row + 1].player == opponent
                    and column.slots[row + 2].player == 0
                ):
                    score += 50
                    continue

                elif (
                    column.slots[row].player == opponent
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
                    == opponent
                    and board.columns[column + 3].slots[row].player == 0
                ):
                    score += 100
                    continue

                elif (
                    board.columns[column].slots[row].player
                    == board.columns[column + 1].slots[row].player
                    == opponent
                    and board.columns[column + 2].slots[row].player == 0
                ):
                    score += 50
                    continue

                elif (
                    board.columns[column].slots[row].player == opponent
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
                    == opponent
                    and board.columns[column + 3].slots[row + 3].player == 0
                ):
                    score += 100
                    continue

                elif (
                    board.columns[column].slots[row].player
                    == board.columns[column + 1].slots[row + 1].player
                    == opponent
                    and board.columns[column + 2].slots[row + 2].player == 0
                ):
                    score += 50
                    continue

                elif (
                    board.columns[column].slots[row].player == opponent
                    and board.columns[column + 1].slots[row + 1].player == 0
                ):
                    score += 10
                    continue

        return score
