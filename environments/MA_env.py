import functools
import gymnasium
import numpy as np
from gymnasium import spaces
from board.board import Board
from gameplay.game_mechanics import check_winner, check_full
from pettingzoo import AECEnv
from pettingzoo.utils import agent_selector, wrappers


def env_wrapper(render_mode=None):
    """
    The env function often wraps the environment in wrappers by default.
    You can find full documentation for these methods
    elsewhere in the developer documentation.
    """
    internal_render_mode = render_mode if render_mode != "ansi" else "human"
    env = MA_env(render_mode=internal_render_mode)
    # This wrapper is only for environments which print results to the terminal
    if render_mode == "ansi":
        env = wrappers.CaptureStdoutWrapper(env)
    # this wrapper helps error handling for discrete action spaces
    env = wrappers.AssertOutOfBoundsWrapper(env)
    # Provides a wide vareity of helpful user errors
    # Strongly recommended
    env = wrappers.OrderEnforcingWrapper(env)

    return env


class MA_env(AECEnv):
    metadata = {"render_modes": ["human"], "name": "rps_v2"}

    def __init__(self, render_mode=None):
        self.possible_agents = ["player_" + str(r) for r in range(1, 3)]
        self.render_mode = render_mode

        # optional: a mapping between agent name and ID
        self.agent_name_mapping = dict(
            zip(self.possible_agents, list(range(len(self.possible_agents))))
        )

        self.board = Board()
        self.score = {"player_1": 0, "player_2": 0}

    @functools.lru_cache(maxsize=None)
    def observation_space(self, agent):
        return spaces.Box(low=0, high=2, shape=(42,), dtype=np.int32)

    @functools.lru_cache(maxsize=None)
    def action_space(self, agent):
        return spaces.Discrete(7)

    def observe(self, agent):
        return np.array(self.observations[agent])

    def reset(self, seed=None, options=None):
        print("Resetting environment")
        self.agents = self.possible_agents[:]
        self.rewards = {agent: 0 for agent in self.agents}
        self._cumulative_rewards = {agent: 0 for agent in self.agents}
        self.terminations = {agent: False for agent in self.agents}
        self.truncations = {agent: False for agent in self.agents}
        self.infos = {agent: {} for agent in self.agents}
        self.state = {agent: None for agent in self.agents}
        self.observations = {
            agent: np.zeros((42,), dtype=np.int32) for agent in self.agents
        }
        self.num_moves = 0

        self._agent_selector = agent_selector(self.agents)
        self.agent_selection = self._agent_selector.next()

        self.board.reset()

    def step(self, action):
        agent = self.agent_selection
        print(f"Agent {agent} is making the move: {action}")

        self._cumulative_rewards[agent] = 0

        # stores action of current agent
        self.state[self.agent_selection] = action

        # make move on board
        agent_index = self.agents.index(agent)
        self.board.make_move(action, agent_index + 1)

        if self._agent_selector.is_last():
            winner = check_winner(self.board)
            # check if game is over
            if winner is not None:
                self.terminations = {agent: True for agent in self.agents}
                if winner == 1:
                    self.rewards["player_1"] = 10
                    self.rewards["player_2"] = -10
                    self.score["player_1"] += 1
                else:
                    self.rewards["player_1"] = -10
                    self.rewards["player_2"] = 10
                    self.score["player_2"] += 1

            # check if game is a draw
            elif check_full(self.board):
                self.terminations = {agent: True for agent in self.agents}
                self.rewards["player_1"] = 0
                self.rewards["player_2"] = 0
                self.score["player_1"] += 0.5
                self.score["player_2"] += 0.5

            self.num_moves += 1

            # observe the current state
            for i in self.agents:
                self.observations[i] = np.array(
                    [
                        slot.player
                        for column in self.board.columns
                        for slot in column.slots
                    ],
                    dtype=np.int32,
                )

        else:
            # necessary so that observe() returns a reasonable observation at all times.
            self.state[self.agents[1 - self.agent_name_mapping[agent]]] = None

            # No rewards are given until the game is over
            self._clear_rewards()

        # selects the next agent.
        self.agent_selection = self._agent_selector.next()
        # Adds .rewards to ._cumulative_rewards
        self._accumulate_rewards()

        if self.render_mode == "human":
            self.render()

    def close(self):
        pass

    def render(self, mode="human"):
        if self.render_mode is None:
            gymnasium.logger.warn(
                "You are calling render method without specifying any render mode."
            )
            return

        if mode == "human":
            print("Score: ", self.score)
            print("Rewards: ", self.rewards)
            print(self.board)
        else:
            raise gymnasium.error.UnsupportedMode(f"Unsupported render mode: {mode}")
