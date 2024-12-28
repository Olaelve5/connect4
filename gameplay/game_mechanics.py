# A slot has a position (x, y) and a player (1 or 2 - 0 is empty)


# Check winner
def check_winner(board):
    winner = vertical_winner(board)
    if winner:
        return winner
    winner = horizontal_winner(board)
    if winner:
        return winner
    return diagonal_winner(board)


def check_full(board):
    return all(slot.player != 0 for slot in board.slots)


def get_slot_player(board, coordinates):
    # find the slot in the board
    slot = next((slot for slot in board.slots if slot.coordinates == coordinates), None)
    return slot.player


# Check Vertical winner
def vertical_winner(board):
    for column in range(7):
        for row in range(3):
            if (
                get_slot_player(board, (column, row))
                == get_slot_player(board, (column, row + 1))
                == get_slot_player(board, (column, row + 2))
                == get_slot_player(board, (column, row + 3))
                != 0
            ):
                player = get_slot_player(board, (column, row))
                return player
    return None


# Check Horizontal winner
def horizontal_winner(board):
    for column in range(4):
        for row in range(6):
            if (
                get_slot_player(board, (column, row))
                == get_slot_player(board, (column + 1, row))
                == get_slot_player(board, (column + 2, row))
                == get_slot_player(board, (column + 3, row))
                != 0
            ):
                player = get_slot_player(board, (column, row))
                return player
    return None


# Check Diagonal winner
def diagonal_winner(board):
    for column in range(4):
        for row in range(3):
            if (
                get_slot_player(board, (column, row))
                == get_slot_player(board, (column + 1, row + 1))
                == get_slot_player(board, (column + 2, row + 2))
                == get_slot_player(board, (column + 3, row + 3))
                != 0
            ):
                player = get_slot_player(board, (column, row))
                return player
    for column in range(3, 7):
        for row in range(3):
            if (
                get_slot_player(board, (column, row))
                == get_slot_player(board, (column - 1, row + 1))
                == get_slot_player(board, (column - 2, row + 2))
                == get_slot_player(board, (column - 3, row + 3))
                != 0
            ):
                player = get_slot_player(board, (column, row))
                return player
    return None
