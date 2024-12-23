import random
from enteties.template_bot import Template_Bot


class Ditto(Template_Bot):
    def __init__(self, name, image_url):
        super().__init__(name, image_url)

    # This bot will always try to make the same move as the last move
    def get_move(self, board):
        available_columns = board.available_columns()
        last_move = board.last_move

        if last_move is not None and last_move in available_columns:
            return last_move
        return random.choice(available_columns)
        