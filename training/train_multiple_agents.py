import random
import sys
import os
from ray.rllib.env import PettingZooEnv
from ray.rllib.algorithms.dqn import DQNConfig
from ray.tune.registry import register_env
from pettingzoo.test import api_test

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from environments.MA_env import env_wrapper, MA_env
from enteties.bots.el_gato import El_Gato

temp_env = MA_env()

observation_space = MA_env().observation_space("player_1")
action_space = MA_env().action_space("player_1")

# Register and initialize the environment
def env_creator():
    return env_wrapper(render_mode="human")

raw_env = env_creator()
api_test(raw_env)


register_env("connect4", lambda config: PettingZooEnv(raw_env))

env = PettingZooEnv(raw_env)
observation_space = observation_space
action_space = action_space

# RLlib configuration
config = (
    DQNConfig()
    .environment(env="connect4")
    .multi_agent(
        policies={
            "player_1": (
                None,
                env_creator().observation_space("player_1"),
                env_creator().action_space("player_1"),
                {},
            ),
            "player_2": (
                None,
                env_creator().observation_space("player_2"),
                env_creator().action_space("player_2"),
                {},
            ),
        },
        policy_mapping_fn=lambda agent_id, *args, **kwargs: agent_id,  # Map agent ID to its policy
    )
    .framework("torch")
    .rollouts(rollout_fragment_length=42)
    .exploration(explore=True)
    .training(
        replay_buffer_config={
            "type": "MultiAgentPrioritizedReplayBuffer",
            "prioritized_replay_alpha": 0.6,
            "prioritized_replay_beta": 0.4,
            "prioritized_replay_eps": 1e-6,
        },
        train_batch_size=42,
    )
)

config.api_stack(
    enable_rl_module_and_learner=False,
    enable_env_runner_and_connector_v2=False
)

algorithm = config.build()

# Create model instance
el_gato_1 = El_Gato("El Gato", env, policy_id="player_2", algorithm=algorithm)

# Define a single checkpoint path for the algorithm
checkpoint_path = os.path.abspath("training/checkpoints/el_gato_algorithm")

# Load models before training (if a checkpoint exists)
if os.path.exists(checkpoint_path):
    algorithm.restore(checkpoint_path)
    print(f"Loaded checkpoint from {checkpoint_path}")

# Train the models (both player_1 and player_2 policies are trained together)
el_gato_1.train_model(50)

# Save the algorithm checkpoint (includes both player_1 and player_2 policies)
algorithm.save(checkpoint_path)
print(f"Checkpoint saved to {checkpoint_path}")

