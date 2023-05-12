import pygame
import settings
import random


class Enemy:
    def __init__(self):
        self.color = settings.YELLOW
        self.box_width = 100
        self.box_height = 100
        self.x_pos = random.randint(0, settings.WIDTH - self.box_width)
        self.y_pos = random.randint(0, settings.HEIGHT - self.box_height)

        self.rect = pygame.Rect(self.x_pos, self.y_pos,
                                self.box_width, self.box_height)

    def update(self):
        self.rect = pygame.Rect(self.x_pos, self.y_pos,
                                self.box_width, self.box_height)

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
