import pygame
import settings
import random


class Wall:
    def __init__(self, x_pos, y_pos):
        self.color = settings.GRAY
        self.box_width = 100
        self.box_height = 100
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.rect = pygame.Rect(self.x_pos, self.y_pos,
                                self.box_width, self.box_height)

    def update(self):
        pass

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
