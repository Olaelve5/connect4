import pygame
import settings.properties as properties
from board.slot import Slot


class Column(pygame.sprite.Sprite):
    def __init__(self, index):
        super().__init__()
        self.height = properties.BOARD_HEIGHT
        self.width = properties.COLUMN_WIDTH
        self.color = (0, 0, 0, 0)
        self.slots = []
        self.index = index
        self.top_slot = 0

        # Calculate position of the column
        board_x = (properties.WINDOW_WIDTH - properties.BOARD_WIDTH) // 2
        self.x = board_x + index * self.width
        self.y = (
            properties.WINDOW_HEIGHT - properties.BOARD_HEIGHT
        ) // 2 + properties.VERTICAL_GAP // 2

        # Create a rect for collision detection
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Create the slots
        for i in range(6):
            self.slots.append(Slot((index, i), 0))

    def draw(self, screen):
        for slot in self.slots:
            slot.draw(screen)

    def hovered_draw(self, screen):
        for slot in self.slots:
            if slot.player == 0:
                slot.hovered_draw(screen)
                break

    def handle_click(self, player):
        if not self.is_valid_move():
            return False

        for slot in self.slots:
            if slot.player == 0:
                slot.update(player)
                self.top_slot = slot.player
                break
        return True

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
    def is_valid_move(self):
        return self.slots[5].player == 0
    
    def __str__(self):
        for slot in self.slots:
            print(slot)
