from enteties.template_bot import Template_Bot


class El_Gato(Template_Bot):
    def __init__(self, name, image_url):
        super().__init__(name, image_url)
        self.last_index = 0

    def get_move(self, board):
        moves = board.available_columns()[:4]

        if self.last_index >= len(moves):
            self.last_index = 0
        
        move = moves[self.last_index]
        self.last_index += 1
        return move
        
