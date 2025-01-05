import os
import time
import numpy as np
from stable_baselines3 import PPO
from enteties.template_bot import Template_Bot


class El_Gato(Template_Bot):
    def __init__(self, name, env, image_url=None, policy_id=None, algorithm=None):
        super().__init__(name, image_url, type="rl_bot")
        self.env = env
        self.policy = policy_id
        self.algorithm = algorithm

    def get_move(self, observation):
        # Use RLlib policy to predict the next action
        policy = self.algorithm.get_policy(self.policy_id)
        action = policy.compute_single_action(observation)
        return action

    def train_model(self, total_timesteps):
        print(f"Training {self.name} for {total_timesteps} iterations...")
        starting_time = time.time()
        print(f"Starting time: {time.strftime('%X', time.localtime(starting_time))}")

        for _ in range(total_timesteps):
            self.algorithm.train()
        
        print(f"{self.name} training complete.")
        ending_time = time.time()
        print(f"Ending time: {time.strftime('%X', time.localtime(ending_time))}")
        print(f"Training duration: {time.strftime('%X', time.gmtime(ending_time - starting_time))}")

    def save(self, path):
        self.algorithm.save(path)
        print(f"Model saved at path: ", path)

    def load(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Checkpoint path does not exist: {path}")
        self.algorithm.restore(path)
        print(f"Model loaded from {path}")
