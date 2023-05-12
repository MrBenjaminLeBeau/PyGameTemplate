import pygame
import settings
import player
import enemy
import wall
import random
import game
import menus
import gui

pygame.init()
pygame.font.init()

# Set Up A Window
window = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)

# Create Our Game
game = game.Game()

# Create a Wall Object
wall1 = wall.Wall(300, 300)

# Create Player Object
player = player.Player(wall1)

# Create Enemy Object
enemy1 = enemy.Enemy()

game.start()

# MAIN LOOP
while game.running:
    # Updates
    game.update()
    player.update()

    # Events
    game.events()

    # Check if They Collide - MOVE LATER
    if player.rect.colliderect(enemy1.rect):
        enemy1.x_pos = random.randint(0, settings.WIDTH - enemy1.box_width)
        enemy1.y_pos = random.randint(0, settings.HEIGHT - enemy1.box_height)
        enemy1.update()

    # DRAW STUFF

    # Set Background Color
    window.fill(settings.SILVER)

    if game.state == "main menu":
        menus.main_menu(window, game.play_button)
    else:
        # Draw Sprites
        player.draw(window)
        enemy1.draw(window)
        wall1.draw(window)

        # Draw Text
        gui.draw_text(window, "Sample Text", 30, settings.BLACK, 100, 100, False)

    # DISPLAY FRAME
    pygame.display.update()
