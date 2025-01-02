import numpy as np
from stable_baselines3 import PPO
from enteties.template_bot import Template_Bot
import copy


class El_Gato_2(Template_Bot):
    def __init__(self, name, image_url, env, model_path=None):
        super().__init__(name, image_url, type="rl_bot")
        self.env = env  # Pass the Connect4Env instance

        if model_path:
            # Load the saved model
            self.model = PPO.load(model_path, env=self.env)
            print(f"Loaded model from {model_path}")
        else:
            # Create a new model if no saved model exists
            self.model = PPO(
                "MlpPolicy",
                self.env,
                verbose=1,
                tensorboard_log="./logs/",
            )

    def get_move(self, board):
        # Get the current observation
        observation = self.env.get_observation()

        # Use the model to predict the next action
        action, _ = self.model.predict(observation)

        # Return the action
        return action

    def train_model(self, total_timesteps):
        print(f"Training model for {total_timesteps} timesteps...")

        # Train the model
        self.model.learn(total_timesteps=total_timesteps, reset_num_timesteps=False)

        print("Training complete. Model updated.")
        self.model.save("el_gato_2_trained_model")
