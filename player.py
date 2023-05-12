import pygame
import settings


class Player:
    def __init__(self, wall):
        self.color = settings.BLUE
        self.box_width = 100
        self.box_height = 100
        self.speed = 10
        self.wall = wall

        self.rect = pygame.Rect(0, 0, self.box_width, self.box_height)

    def update(self):
        self.keyboard_movement()

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def keyboard_movement(self):
        dx = 0
        dy = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy = -self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy = self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = self.speed

        self.move(dx, dy)

    def move(self, dx, dy):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        self.check_boundary()

        # Check Wall Collision
        if self.rect.colliderect(self.wall.rect):
            if dy < 0:
                self.rect.top = self.wall.rect.bottom
            if dy > 0:
                self.rect.bottom = self.wall.rect.top
            if dx < 0:
                self.rect.left = self.wall.rect.right
            if dx > 0:
                self.rect.right = self.wall.rect.left

    def check_boundary(self):
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > settings.HEIGHT - self.box_height:
            self.rect.y = settings.HEIGHT - self.box_height
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > settings.WIDTH - self.box_width:
            self.rect.x = settings.WIDTH - self.box_width

