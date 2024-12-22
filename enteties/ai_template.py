import gameplay.game_mechanics as game_mechanics

class AI:
    def __init__(self, name, image=None):
        self.name = name
        self.image = image

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
    


