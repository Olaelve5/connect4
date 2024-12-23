import pygame
from properties import HORIZONTAL_GAP, WHITE, WINDOW_WIDTH, YELLOW, RED, FONT, TITLE_FONT, SUB_FONT

pygame.init()

class ui:
    def __init__(self, player1, player2):
        self.font = FONT
        self.text_elements = []
        self.circle_elements = []
        self.player1 = player1
        self.player2 = player2
        self.initialize()

    def add_circle(self, position, color):
        self.circle_elements.append({"position": position, "color": color})

    def add_text(self, text, position, color=WHITE, font=SUB_FONT):
        position = (position[0] - font.size(text)[0] // 2, position[1])
        self.text_elements.append({"text": text, "position": position, "color": color, "font": font})

    def draw(self, screen):
        if self.text_elements:
            for element in self.text_elements:
                text_surface = element["font"].render(element["text"], True, element["color"])
                screen.blit(text_surface, element["position"])

        if self.circle_elements:
            for element in self.circle_elements:
                pygame.draw.circle(screen, element["color"], element["position"], 30)

        # Draw the player image from the url

        player_1_image = pygame.image.load(self.player1.image_url)
        player_1_image = pygame.transform.scale(player_1_image, (150, 150))
        player_2_image = pygame.image.load(self.player2.image_url)
        player_2_image = pygame.transform.scale(player_2_image, (150, 150))

        screen.blit(player_1_image, (HORIZONTAL_GAP // 2 - 75, 275))
        screen.blit(player_2_image, (WINDOW_WIDTH - HORIZONTAL_GAP // 2 - 75, 275))
    
    def initialize(self):
        self.add_text("Connect 4", (WINDOW_WIDTH // 2, 50), WHITE, TITLE_FONT)
        self.add_text(self.player1.name, (HORIZONTAL_GAP // 2, 200))
        self.add_circle((HORIZONTAL_GAP // 2, 500), YELLOW)
        self.add_text(self.player2.name, (WINDOW_WIDTH - HORIZONTAL_GAP // 2, 200))
        self.add_circle((WINDOW_WIDTH - HORIZONTAL_GAP // 2, 500), RED)

        return self
