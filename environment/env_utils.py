from environment.connect4Env import Connect4Env

def handle_winner(env: Connect4Env, winning_player):
    reward = 0
    score = (0, 0)

    if winning_player is not None:

        if winning_player.type == "rl_bot":
            reward = 1
        else:
            reward = -1

        if winning_player == env.player_1:
            score = (env.score[0] + 1, env.score[1])
        else:
            score = (env.score[0], env.score[1] + 1)


    return reward, score
