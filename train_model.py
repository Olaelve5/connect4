from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_vec_env  # If you want vectorized environments

def train_model(model_path, env, total_timesteps):
    """
    Train an existing model from its file path.

    :param model_path: str - Path to the saved model file.
    :param env: gym.Env - The environment to train the model in.
    :param total_timesteps: int - Number of timesteps to train the model.
    """
    # Load the model
    print(f"Loading model from {model_path}...")
    model = DQN.load(model_path, env=env)
    print(f"Replay buffer size: {model.replay_buffer.size()}")

    print(f"Model loaded successfully.")

    # Train the model
    print(f"Training model for {total_timesteps} timesteps...")
    model.learn(total_timesteps=total_timesteps, reset_num_timesteps=False)

    # Save the updated model
    updated_model_path = model_path.replace(".zip", "_updated.zip")
    model.save(updated_model_path)
    print(f"Model trained and saved to {updated_model_path}")

    print(f"Replay buffer size: {model.replay_buffer.size()}")
    return model


# Import your custom environment
from environment.connect4Env import Connect4Env
from player_manager import Player_Manager
from enteties.player import Player
from enteties.bots.randobot import Randobot

# Initialize your custom environment
player_manager = Player_Manager()
player_manager.add_player(Player("Human", "assets/player_images/human.png"))
player_manager.add_player(Randobot("Randobot", "assets/player_images/robot.png"))
env = Connect4Env(player_manager)

# File path of the existing model
model_path = "el_gato_trained_model"

# Train the model
trained_model = train_model(model_path, env, total_timesteps=50000)

