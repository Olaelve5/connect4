import random
from enteties.template_bot import Template_Bot


class Bot(Template_Bot):
    def __init__(self, name, image_url):
        super().__init__(name, image_url)

    def get_move(self, board):
        # Decide on which move, first available returned for now
        return random.choice(board.available_columns())
