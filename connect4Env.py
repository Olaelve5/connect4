from typing import Optional
import gymnasium as gym
from gymnasium import spaces
import numpy as np
from board.board import Board


class Connect4Env(gym.Env):
    def __init__(self, board: Board, agent_number=1):
        super(Connect4Env, self).__init__()
        self.board = board
        self.agent = agent_number
        self.action_space = spaces.Discrete(7)
        self.observation_space = spaces.Box(low=0, high=2, shape=(42,), dtype=np.int32)

    def reset(self, seed: Optional[int] = None, options: Optional[dict] = None):
        super().reset(seed=seed)
        return self.get_observation(), {}

    def step(self, action):

        if self.board is None:
            return self.get_observation(), 0, False, False, {}

        valid = self.board.is_valid_move(action)
        if not valid:
            return self.get_observation(), -10, False, False, {"invalid_action": True}

        reward = 0
        done = False
        truncated = False
        info = {}

        if self.board.is_loosing_move(action):
            reward = -1

        if self.board.is_winning_move(action):
            done = True
            reward = 1 

        elif not self.board.available_columns():  # Check for a draw
            done = True
            reward = 0.5

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
