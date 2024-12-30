from stable_baselines3 import DQN
from enteties.template_bot import Template_Bot


class El_Gato(Template_Bot):
    def __init__(self, name, image_url, env, model_path=None):
        super().__init__(name, image_url, type="rl_bot")
        self.env = env  # Pass the Connect4Env instance

        if model_path:
            # Load the saved model
            self.model = DQN.load(model_path, env=self.env)
            print(f"Loaded model from {model_path}")
        else:
            # Create a new model if no saved model exists
            self.model = DQN(
                "MlpPolicy",
                self.env,
                verbose=1,
                learning_rate=0.001,
                buffer_size=10000,
                learning_starts=100,
                batch_size=64,
                gamma=0.99,
                exploration_fraction=0.1,
                exploration_final_eps=0.02,
            )

    def get_move(self, board):
        # Get the current observation
        observation = self.env.get_observation()

        # Use the model to predict the next action
        action, _ = self.model.predict(observation)

        return action

    def train(self):
        # Train the agent after each game
        self.model.learn(total_timesteps=500)
        self.model.save("el_gato_dqn_agent")
