from board.board import Board
from gameplay.game_mechanics import check_winner


def handle_winner(env, winning_player):
    reward = 0
    score = env.score

    if winning_player is not None:
        if winning_player.type == "rl_bot":
            reward = 10
        else:
            reward = -5

        if winning_player == env.player_1:
            score = (score[0] + 1, score[1])
        else:
            score = (score[0], score[1] + 1)

    return reward, score


def calculate_move_delay(total_games):
    if total_games > 55:
        move_delay = 1
    elif total_games > 20:
        move_delay = 5
    elif total_games > 5:
        move_delay = 10
    else:
        move_delay = 500
    return move_delay
