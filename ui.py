import pygame
from properties import HORIZONTAL_GAP, WHITE, WINDOW_WIDTH, YELLOW, RED, FONT, TITLE_FONT

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
        """Add a circle element to the UI."""
        self.circle_elements.append({"position": position, "color": color})

    def add_text(self, text, position, color=WHITE, font=FONT):
        """Add a text element to the UI."""
        position = (position[0] - font.size(text)[0] // 2, position[1])
        self.text_elements.append({"text": text, "position": position, "color": color, "font": font})

    def draw(self, screen):
        if self.text_elements:
            """Render all UI text elements."""
            for element in self.text_elements:
                text_surface = element["font"].render(element["text"], True, element["color"])
                screen.blit(text_surface, element["position"])

        if self.circle_elements:
            """Render all UI circle elements."""
            for element in self.circle_elements:
                pygame.draw.circle(screen, element["color"], element["position"], 40)
    
    def initialize(self):
        self.add_text("Connect 4", (WINDOW_WIDTH // 2, 50), WHITE, TITLE_FONT)
        self.add_text(self.player1, (HORIZONTAL_GAP // 2, 200))
        self.add_circle((HORIZONTAL_GAP // 2, 320), YELLOW)
        self.add_text(self.player2, (WINDOW_WIDTH - HORIZONTAL_GAP // 2, 200))
        self.add_circle((WINDOW_WIDTH - HORIZONTAL_GAP // 2, 320), RED)

        return self
