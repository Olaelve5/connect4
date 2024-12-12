board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '], # 0
    [' ', ' ', ' ', ' ', ' ', ' ', ' '], # 1
    [' ', ' ', ' ', ' ', ' ', ' ', ' '], # 2
    [' ', ' ', ' ', ' ', ' ', ' ', ' '], # 3
    [' ', ' ', ' ', ' ', ' ', ' ', ' '], # 4
    [' ', ' ', ' ', ' ', ' ', ' ', ' '], # 5
]


# Board class
class Board:
    def __init__(self) -> None:
        self.board = board


    # Update the board with the player's move
    def update(self, column, player) -> None:
        if self.check_move(column):
            for i in range(5, -1, -1):
                if self.board[i][column] == ' ':
                    if player == 1:
                        self.board[i][column] = 'X'
                    else:
                        self.board[i][column] = 'O'
                    break
        else:
            print('Invalid move')
        

    # Check if the move is valid
    def check_move(self, column) -> bool:
        if column < 0 or column > 6:
            return False
        
        if self.board[0][column] == ' ':
            return True
        else:
            return False

    # Check if there is a winner
    def check_winner(self) -> bool:
        for i in range(6):
            for j in range(7):
                if self.board[i][j] != ' ':
                    if self.check_horizontal(i, j) or self.check_vertical(i, j) or self.check_diagonal(i, j):
                        return True
        return False

    # Check if there is a horizontal winner
    def check_horizontal(self, i, j) -> bool:
        if j < 4:
            if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3]:
                return True
        return False


    # Check if there is a vertical winner
    def check_vertical(self, i, j) -> bool:
        if i < 3:
            if self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]:
                return True
        return False
    

    # Check if there is a diagonal winner
    def check_diagonal(self, i, j) -> bool:
        if i < 3 and j < 4:
            if self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3]:
                return True
        if i < 3 and j > 2:
            if self.board[i][j] == self.board[i+1][j-1] == self.board[i+2][j-2] == self.board[i+3][j-3]:
                return True
        return False

    # Print the board
    def print_board(self) -> None:
        for i in range(6):
            print(self.board[i])
        print('---------------')
        print('  0   1   2   3   4   5   6')
        print('---------------')
        print('')

    
    # Check if the board is full
    def check_full(self) -> bool:
        for i in range(6):
            for j in range(7):
                if self.board[i][j] == ' ':
                    return False
        return True
    

    # Reset the board
    def reset(self) -> None:
        for i in range(6):
            for j in range(7):
                self.board[i][j] = ' '
        print('Board reset')
        print('')


