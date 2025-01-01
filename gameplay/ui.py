import pygame
from settings.properties import (
    HORIZONTAL_GAP,
    WHITE,
    WINDOW_WIDTH,
    YELLOW,
    RED,
    GREEN,
    FONT,
    TITLE_FONT,
    SUB_FONT,
)
from environment.connect4Env import Connect4Env

pygame.init()


class ui:
    def __init__(self, env: Connect4Env):
        self.env = env
        self.font = FONT
        self.text_elements = []
        self.circle_elements = []
        self.player_1 = env.player_1
        self.player_2 = env.player_2
        self.score = env.score
        self.total_games = env.total_games
        self.initialize()

    def add_circle(self, position, color):
        self.circle_elements.append({"position": position, "color": color})

    def add_text(self, text, position, color=WHITE, font=SUB_FONT):
        position = (position[0] - font.size(text)[0] // 2, position[1])
        self.text_elements.append(
            {"text": text, "position": position, "color": color, "font": font}
        )

    def draw(self, screen):
        if self.text_elements:
            for element in self.text_elements:
                text_surface = element["font"].render(
                    element["text"], True, element["color"]
                )
                screen.blit(text_surface, element["position"])

        if self.circle_elements:
            for element in self.circle_elements:
                pygame.draw.circle(screen, element["color"], element["position"], 30)

        # Draw the player image from the url

        player_1_image = pygame.image.load(self.player_1.image_url)
        player_1_image = pygame.transform.scale(player_1_image, (150, 150))
        player_2_image = pygame.image.load(self.player_2.image_url)
        player_2_image = pygame.transform.scale(player_2_image, (150, 150))

        screen.blit(player_1_image, (HORIZONTAL_GAP // 2 - 75, 275))
        screen.blit(player_2_image, (WINDOW_WIDTH - HORIZONTAL_GAP // 2 - 75, 275))
    
    @property
    def games_left(self):
        return self.env.total_games - self.env.played_games


    def update_score(self):
        self.score = self.env.score
        self.text_elements[-2] = {
            "text": f"Score: {self.score[0]}",
            "position": (HORIZONTAL_GAP // 2, 600),
            "color": WHITE,
            "font": SUB_FONT,
        }
        self.text_elements[-1] = {
            "text": f"Score: {self.score[1]}",
            "position": (WINDOW_WIDTH - HORIZONTAL_GAP // 2, 600),
            "color": WHITE,
            "font": SUB_FONT,
        }

        self.text_elements[1] = {
            "text": f"Games left: {self.games_left}",
            "position": (WINDOW_WIDTH // 2, 160),
            "color": GREEN,
            "font": SUB_FONT,
        }

    def initialize(self):
        self.add_text("Connect 4", (WINDOW_WIDTH // 2, 50), WHITE, TITLE_FONT)
        self.add_text(
            f"Games left: {self.games_left}",
            (WINDOW_WIDTH // 2, 160),
            GREEN,
        )
        self.add_text(self.player_1.name, (HORIZONTAL_GAP // 2, 200))
        self.add_circle((HORIZONTAL_GAP // 2, 500), YELLOW)
        self.add_text(self.player_2.name, (WINDOW_WIDTH - HORIZONTAL_GAP // 2, 200))
        self.add_circle((WINDOW_WIDTH - HORIZONTAL_GAP // 2, 500), RED)
        self.add_text(f"Score: {self.score[0]}", (HORIZONTAL_GAP // 2, 600))
        self.add_text(
            f"Score: {self.score[1]}", (WINDOW_WIDTH - HORIZONTAL_GAP // 2, 600)
        )

        return self
