import random
from enteties.template_bot import Template_Bot


class Randotron(Template_Bot):
    def __init__(self, name, image_url):
        super().__init__(name, image_url)

    def get_move(self, board):
        # Decide on which move to make
        return random.choice(board.available_columns())

    def get_good_move(self, board):
        pass
