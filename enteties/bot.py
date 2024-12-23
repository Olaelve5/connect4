import gameplay.game_mechanics as game_mechanics
import pygame

class Bot:
    def __init__(self, name, image_url):
        self.name = name
        self.image_url = image_url
        self.type = "bot"

    def find_available_moves(self, board):
        if game_mechanics.check_full(board):
            return []

        moves = []
        for column in board.columns:
            for slot in column.slots:
                if slot.player == 0:
                    moves.append(column.index)
                    break
        
        return moves
    
    def get_move(self, board):
        moves = self.find_available_moves(board)

        # Decide on which move, first available returned for now 
        return moves[0]
    
    def draw(self, screen, position):
        image = pygame.image.load(self.image_url)
        scaled_image = pygame.transform.scale(image, (200, 200))
        screen.blit(scaled_image, position)
    


