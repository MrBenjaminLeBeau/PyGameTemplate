import settings
import pygame
import menus
import gui


class Game:
    def __init__(self):
        self.running = False
        self.clock = pygame.time.Clock()
        self.walls = []
        self.state = "main menu"
        self.play_button = gui.Button((0, 0, 100, 100), settings.RED,
                                 lambda: self.play_function(),
                                 text="Play",
                                 hover_color=settings.BLUE)

    def start(self):
        self.running = True

    def play_function(self):
        self.state = "Running"

    def update(self):
        self.clock.tick(settings.FPS)

    def events(self):
        # EVENT LOOP
        for event in pygame.event.get():

            self.play_button.check_event(event)

            # Close Program on Quit
            if event.type == pygame.QUIT:
                self.running = False

            # ALL KEYDOWN EVENTS HERE
            if event.type == pygame.KEYDOWN:

                # Press Escape to Quit
                if event.key == pygame.K_ESCAPE:
                    self.running = False

