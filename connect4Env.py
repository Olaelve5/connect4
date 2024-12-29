import gymnasium as gym
from gymnasium import spaces
import numpy as np
from board.board import Board


class Connect4Env(gym.Env):
    def __init__(self, board: Board):
        super(Connect4Env, self).__init__()
        self.board = board
        self.action_space = spaces.Discrete(7)
        self.observation_space = spaces.Box(low=0, high=2, shape=(6, 7), dtype=int)

    def reset(self):
        return self.get_observation(), {}

    def step(self, action):
        # Validate action externally before calling this
        valid = self.board.is_valid_move(action)
        if not valid:
            return self.get_observation(), -10, True, {"invalid_action": True}

        # Assume the move has already been made externally
        reward = 0
        done = False
        info = {}

        if self.board.winner is not None:
            done = True
            reward = 1 if self.board.winner == 1 else -1
        elif not self.board.available_columns():  # Check for a draw
            done = True
            reward = 0.5

        return self.get_observation(), reward, done, info

    def render(self):
        pass

    def get_observation(self):
        return np.array(
            [[slot.player for slot in column.slots] for column in self.board.columns]
        )
