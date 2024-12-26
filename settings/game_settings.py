class Game_Settings:
    def __init__(
        self, player_1, player_2, score=(0, 0), continuous=False, total_games=1
    ):
        self.player_1 = player_1
        self.player_2 = player_2
        self.score = score
        self.total_games = total_games
        self.continuous = continuous
        self.move_delay = 500
        self.played_games = 0
        self.games_left = total_games - self.played_games

    def set_settings(self, player_1, player_2, score, continuous, total_games, played_games = 0):
        self.player_1 = player_1
        self.player_2 = player_2
        self.score = score
        self.continuous = continuous
        self.total_games = total_games
        self.played_games = played_games

        if self.total_games > 45:
            self.move_delay = 5
        elif self.total_games > 20:
            self.move_delay = 15
        elif self.total_games > 5:
            self.move_delay = 50
        else:
            self.move_delay = 500
        
    def reset(self):
        self.score = (0, 0)
        self.played_games = 0
        self.games_left = self.total_games - self.played_games
