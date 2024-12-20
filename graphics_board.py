import properties
from slot import Slot
import pygame


class Board: 
    def __init__(self):
        self.columns = []
        for i in range(7):
            self.columns.append(Column(i))
    
    def draw(self, screen):
        pygame.draw.rect(screen, properties.BLUE, 
                    ((properties.WINDOW_WIDTH - properties.BOARD_WIDTH) // 2, 
                    (properties.WINDOW_HEIGHT - properties.BOARD_HEIGHT) // 2,
                    properties.BOARD_WIDTH, properties.BOARD_HEIGHT), 0, 10)
        for column in self.columns:
            column.draw(screen)
    
    def handle_click(self, mouse_pos):
        for column in self.columns:
            if column.rect.collidepoint(mouse_pos):  # Check if mouse is inside the column
                column.handle_click()




class Column(pygame.sprite.Sprite):
    def __init__(self, index):
        super().__init__()
        self.height = properties.BOARD_HEIGHT
        self.width = properties.COLUMN_WIDTH
        self.color = (0, 0, 0, 0)
        self.slots = []
        self.index = index

        # Calculate position of the column
        board_x = (properties.WINDOW_WIDTH - properties.BOARD_WIDTH) // 2
        self.x = board_x + index * self.width
        self.y = (properties.WINDOW_HEIGHT - properties.BOARD_HEIGHT) // 2

        # Create a rect for collision detection
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Create the slots
        for i in range(6):
            self.slots.append(Slot((index, i), 0))

    def update(self):
        pass

    def draw(self, screen):
        for slot in self.slots:
            slot.draw(screen)

    def handle_click(self):
        print('Clicked on column', self.index)