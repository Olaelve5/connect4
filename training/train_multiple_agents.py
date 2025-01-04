import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from environments.MA_env import env_wrapper

env = env_wrapper(render_mode="human")
env.reset(seed=45)

for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last(observe=True)

    if termination or truncation:
        action = None
        break
    else:
        # this is where you would insert your policy
        action = env.action_space(agent).sample()

    env.step(action)
env.close()