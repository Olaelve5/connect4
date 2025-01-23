import random
from enteties.template_bot import Template_Bot


class Randobot(Template_Bot):
    def __init__(self):
        super().__init__()
        self.name = "Randobot"

    def get_move(self, board):
        # Returns a random move from the available columns
        return random.choice(board.available_columns())
