import random
from enteties.template_bot import Template_Bot


class Randotron(Template_Bot):
    def __init__(self, name):
        super().__init__(name)

    def get_move(self, board):
        # Decide on which move to make
        moves = board.available_columns()
        return random.choice(moves[:4])

    def get_good_move(self, board):
        pass
