import properties


class Button:
    def __init__(self, text, x, y, font, color, screen):
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.color = color
        self.screen = screen
        self.text_surface = self.font.render(self.text, True, self.color)
        self.rect = self.text_surface.get_rect(center=(self.x, self.y))

    def draw(self, mouse_pos):
        self.change_color(mouse_pos)
        self.screen.blit(self.text_surface, self.rect)
    
    def selected_draw(self):
        self.color = properties.GREEN
        self.text_surface = self.font.render(self.text, True, self.color)
        self.screen.blit(self.text_surface, self.rect)

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def change_color(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            new_color = properties.RED
        else:
            new_color = properties.WHITE

        if new_color != self.color:
            self.color = new_color
            self.text_surface = self.font.render(self.text, True, self.color)
