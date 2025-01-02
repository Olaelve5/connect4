from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.vec_env import DummyVecEnv
from environment.connect4Env import Connect4Env
from player_manager import Player_Manager
from enteties.bots.randobot import Randobot
from enteties.bots.georgian import Georgian
from enteties.bots.el_gato import El_Gato
from enteties.bots.el_gato_2 import El_Gato_2

# Add players to the player manager
player_manager = Player_Manager()
randobot = Randobot("Randobot", "assets/player_images/robot.png")
georgian = Georgian("Georgian", "assets/player_images/georgian.png")
player_manager.add_player(randobot)
player_manager.add_player(georgian)

env = Connect4Env(player_manager, training_mode=True)

el_gato = El_Gato("El Gato", "assets/player_images/el_gato.png", env)
player_manager.add_player(el_gato)

el_gato_2 = El_Gato_2("El Gato 2", "assets/player_images/el_gato_2.png", env, "el_gato_2_trained_model")
player_manager.add_player(el_gato_2)


check_env(env)

vec_env = DummyVecEnv([lambda: env])

def train_model(model, opponent, total_timesteps, agent_is_first=True):
    if agent_is_first:
        env.set_players(model, opponent)
    else:
        env.set_players(opponent, model)

    print(f"Training model for {total_timesteps} timesteps...")
    model.train_model(total_timesteps)
    print("Training complete. Model updated.")


train_model(el_gato_2, georgian, 100000, agent_is_first=True)

    
