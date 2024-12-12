from board import Board


def main() -> None:
    # Create a new board
    board = Board()
    board.print_board()
    player = 1

    # Game loop
    while True:
        # Get the column from the player
        column = int(input('Enter a column: '))
        while not column in range(7):
            column = int(input('Enter a valid column: '))

        # Place the piece
        board.update(column, player)
        board.print_board()

        # Check if there is a winner
        if board.check_winner():
            print(f'Player {player} wins!')
            break

        # Check if the board is full
        if board.check_full():
            print('The board is full!')
            break

        # Switch players
        if player == 1:
            player = 2
        else:
            player = 1
        


if __name__ == '__main__':
    main()