import pygame
import properties
import pygame.gfxdraw

def calculate_position(x, y):
    x = properties.HORIZONTAL_START + properties.CHIP_RADIUS * 2 * x + properties.CHIP_GAP * x
    y = properties.VERTICAL_START - properties.CHIP_RADIUS * 2 * y - properties.CHIP_GAP * y
    return x, y

class Slot:
    def __init__(self, coordinates, player):
        self.coordinates = coordinates
        self.position = calculate_position(*coordinates)
        self.player = player
        self.color = (115, 192, 255)
        self.radius = properties.CHIP_RADIUS
        if player == 1:
            self.color = properties.YELLOW
        elif player == 2:
            self.color = properties.RED
        elif coordinates[1] == 0 and coordinates[0] == 3:
            self.color = properties.RED
    
    def draw(self, screen):
        # pygame.draw.circle(screen, self.color, self.position, self.radius)
        pygame.gfxdraw.aacircle(screen, self.position[0], self.position[1], self.radius, self.color)
        pygame.gfxdraw.filled_circle(screen, self.position[0], self.position[1], self.radius, self.color)