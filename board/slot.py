import pygame
import settings.properties as properties
import pygame.gfxdraw


def calculate_position(x, y):
    x = (
        properties.HORIZONTAL_START
        + properties.CHIP_RADIUS * 2 * x
        + properties.CHIP_GAP * x
    )
    y = (
        properties.VERTICAL_START
        - properties.CHIP_RADIUS * 2 * y
        - properties.CHIP_GAP * y
        + properties.VERTICAL_GAP // 2
    )
    return x, y


class Slot:
    def __init__(self, coordinates, player):
        self.coordinates = coordinates
        self.position = calculate_position(*coordinates)
        self.player = player
        self.color = (115, 192, 255)  # Default color (e.g., empty slot)
        self.radius = properties.CHIP_RADIUS
        self.player_turn = 1
        self.update_color()

    def update_color(self):
        """Update the slot's color based on the player."""
        if self.player == 1:
            self.color = properties.YELLOW
        elif self.player == 2:
            self.color = properties.RED
        else:
            self.color = (115, 192, 255)  # Default color for empty slot

    def update(self, player):
        """Update the player and the color."""
        self.player = player
        self.update_color()

    def draw(self, screen):
        # pygame.draw.circle(screen, self.color, self.position, self.radius)
        pygame.gfxdraw.aacircle(
            screen, self.position[0], self.position[1], self.radius, self.color
        )
        pygame.gfxdraw.filled_circle(
            screen, self.position[0], self.position[1], self.radius, self.color
        )

    def hovered_draw(self, screen):
        color = properties.HOVER_YELLOW if self.player_turn == 1 else properties.HOVER_RED
        pygame.gfxdraw.aacircle(
            screen, self.position[0], self.position[1], self.radius, color
        )
        pygame.gfxdraw.filled_circle(
            screen, self.position[0], self.position[1], self.radius, color
        )
