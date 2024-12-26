from enteties.template_bot import Template_Bot


class Georgian(Template_Bot):
    def __init__(self, name, image_url):
        super().__init__(name, image_url)

    def get_move(self, board):
        return board.available_columns()[0]
        
