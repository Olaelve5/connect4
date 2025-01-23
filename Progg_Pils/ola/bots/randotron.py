import random
from enteties.template_bot import Template_Bot


class Randotron(Template_Bot):
    def __init__(self):
        super().__init__()
        self.image_url = "Progg_Pils/ola/assets/randotron.png"
        self.name = "Randotron"
        self.sound = "Progg_Pils/ola/assets/randotron.mp3"

    def get_move(self, board):
        # Returns a move in one of the first four columns
        moves = board.available_columns()
        return random.choice(moves[:4])
