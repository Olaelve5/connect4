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
el_gato_1 = El_Gato("El Gato", env, policy_id="player_1", algorithm=algorithm)
el_gato_2 = El_Gato("El Gato", env, policy_id="player_2", algorithm=algorithm)

checkpoint_path_1 = os.path.abspath("training/checkpoints/el_gato_1")  # Use a full path
checkpoint_path_2 = os.path.abspath("training/checkpoints/el_gato_2")  # Use a full path

# Load models before training
if os.path.exists(checkpoint_path_1):
    el_gato_1.load(checkpoint_path_1)

if os.path.exists(checkpoint_path_2):
    el_gato_2.load(checkpoint_path_2)


# Train the models
el_gato_1.train_model(20)
el_gato_2.train_model(20)

# Save models after training
el_gato_1.save(checkpoint_path_1)
el_gato_2.save(checkpoint_path_2)
