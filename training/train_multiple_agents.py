import sys
import os

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from environments.MA_env import env_wrapper
from enteties.bots.el_gato import El_Gato

# Initialize the environment
env = env_wrapper(render_mode="human")

# Initialize two models
model_1 = El_Gato("player_1", env)
model_2 = El_Gato("player_2", env)

# Training parameters
num_episodes = 100
total_timesteps = 10000

# Training loop
for episode in range(num_episodes):
    print(f"Starting Episode {episode + 1}/{num_episodes}")
    env.reset(seed=episode)

    for agent in env.agent_iter():
        observation, reward, termination, truncation, info = env.last(observe=True)

        if termination or truncation:
            action = None  # Skip terminated agents
        else:
            # Use respective models for each agent
            if agent == "player_1":
                action, _ = model_1.get_move(observation)
            elif agent == "player_2":
                action, _ = model_2.get_move(observation)

        # Perform the action in the environment
        env.step(action)

        # Update models with rewards
        if agent == "player_1":
            model_1.model.learn(total_timesteps=total_timesteps, reset_num_timesteps=False)
        elif agent == "player_2":
            model_2.model.learn(total_timesteps=total_timesteps, reset_num_timesteps=False)
        

    print(f"Episode {episode + 1} completed.")

env.close()

# Save the trained models
model_1.save("player_1_trained_model")
model_2.save("player_2_trained_model")
