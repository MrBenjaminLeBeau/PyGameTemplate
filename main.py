import pygame
import settings

# Set Up A Window
window = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)

# MAIN LOOP
running = True
while running:

    # EVENT LOOP
    for event in pygame.event.get():

        # Close Program on Quit
        if event.type == pygame.QUIT:
            running = False

    # DRAW STUFF

    # Set Background Color
    window.fill(settings.SILVER)

    # Draw Rectangle
    # pygame.draw.rect(window, color, pygame.Rect(x pos, y pos, width, height)
    pygame.draw.rect(window, settings.BLUE, pygame.Rect(0, 0, 100, 100))

    # DISPLAY FRAME
    pygame.display.update()
