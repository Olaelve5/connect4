from typing import Optional
import gymnasium as gym
from gymnasium import spaces
import numpy as np
from board.board import Board
from environment.env_utils import handle_winner, calculate_move_delay, get_move_score
from gameplay.game_mechanics import check_winner, check_full
from player_manager import Player_Manager


# Connect4Env class - Gym environment for the Connect4 game + handles the game logic
class Connect4Env(gym.Env):
    def __init__(
        self,
        player_manager: Player_Manager,
        score=(0, 0),
        continuous=False,
        total_games=1,
        selected_mode="Continous 25",
        agent_number=1,
        training_mode=False,
    ):
        super(Connect4Env, self).__init__()
        self.agent = agent_number
        self.action_space = spaces.Discrete(7)
        self.observation_space = spaces.Box(low=0, high=2, shape=(42,), dtype=np.int32)

        # States for the game
        self.board = Board()
        self.player_manager = player_manager
        self.player_1 = player_manager.players[0]
        self.player_2 = player_manager.players[1]
        self.player_turn = self.player_1
        self.winner = None
        self.score = score
        self.total_games = total_games
        self.continuous = continuous
        self.move_delay = 500
        self.played_games = 0
        self.games_left = total_games - self.played_games
        self.selected_mode = selected_mode
        self.training_mode = training_mode

    def reset(self, seed: Optional[int] = None, options: Optional[dict] = None):
        # Reset the board and the game state
        super().reset(seed=seed)
        self.board.reset()
        self.winner = None
        self.player_turn = self.player_1
        self.games_left = self.total_games - self.played_games

        # Return the initial observation
        return self.get_observation(), {}

    def step(self, action):

        if self.board is None:
            return self.get_observation(), 0, False, False, {}

        valid = self.board.is_valid_move(action)
        if not valid:
            # Skip the turn if the move is invalid
            self.change_player_turn()
            return self.get_observation(), -10, False, False, {"invalid_action": True}

        reward = 0
        done = False
        truncated = False
        info = {}

        self.board.make_move(action, 1 if self.player_turn == self.player_1 else 2)
        winner = check_winner(self.board)
        full = check_full(self.board)

        reward = get_move_score(
            self.board, action, 1 if self.player_turn == self.player_1 else 2
        )

        # handle winning move
        if winner:
            self.winner = self.player_1 if winner == 1 else self.player_2
            if self.winner.type == "rl_bot":
                reward = 10
            self.played_games += 1
            done = True
            self.score = handle_winner(self, self.winner)
        # handle draw
        elif full:
            self.played_games += 1
            done = True
            reward += 0.5
            self.score = (self.score[0] + 0.5, self.score[1] + 0.5)

        # Switch the player turn
        self.change_player_turn()

        # Execute bot mode if training mode is enabled
        if self.training_mode:
            if not done:  # Only proceed if the game isn't over
                done, reward = self.execute_bot_mode()

        return self.get_observation(), reward, done, truncated, info

    def render(self):
        pass

    def get_observation(self):
        # Flatten the 6x7 board into a 1D array of length 42
        if self.board is None:
            return np.zeros((42,), dtype=np.int32)

        return np.array(
            [slot.player for column in self.board.columns for slot in column.slots],
            dtype=np.int32,
        )

    def change_player_turn(self):
        self.player_turn = (
            self.player_1 if self.player_turn == self.player_2 else self.player_2
        )

    def switch_sides(self):
        self.player_1, self.player_2 = self.player_2, self.player_1

    def set_players(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def set_settings(
        self, player_1, player_2, score, continuous, total_games, played_games=0
    ):
        self.player_1 = player_1
        self.player_2 = player_2
        self.score = score
        self.continuous = continuous
        self.total_games = total_games
        self.played_games = played_games
        self.games_left = total_games - played_games
        self.move_delay = calculate_move_delay(self.total_games)

    def execute_bot_mode(self):
        done = False
        reward = 0
        # Let the opponent bot take its move
        if self.player_turn.type != "rl_bot":
            action = self.player_turn.get_move(self.board)
            print(f"{self.player_turn.name} played move: {action}")

            # Update the board for the opponent's move
            if self.board.is_valid_move(action):
                self.board.make_move(
                    action, 2 if self.player_turn == self.player_2 else 1
                )

            # Check if the game ends after the bot's move
            winner = check_winner(self.board)
            full = check_full(self.board)

            if winner:
                self.winner = self.player_turn
                self.played_games += 1
                reward = -10
                done = True
            elif full:
                self.played_games += 1
                done = True
                reward = 0.5

            # Switch the player turn back to the RL agent
            self.change_player_turn()

            if done:
                self.score = handle_winner(self, self.winner)

        return done, reward
