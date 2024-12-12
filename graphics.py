import pygame

pygame.init()

# Create the screen
screen = pygame.display.set_mode((700, 600))
pygame.display.set_caption('Connect 4')


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    pygame.display.update()
