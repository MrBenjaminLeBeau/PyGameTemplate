import settings
import gui
import pygame


def main_menu(window, play_button):
    pygame.draw.rect(window, settings.BLUE,
                     (0, 0, settings.WIDTH, settings.HEIGHT / 2))
    gui.draw_text(window, "Main Menu", 80, settings.BLACK,
                  settings.WIDTH / 2, settings.HEIGHT / 4, True)
    pygame.draw.rect(window, settings.RED,
                     (0, settings.HEIGHT / 2, settings.WIDTH / 2, settings.HEIGHT / 2))
    gui.draw_text(window, "Options", 80, settings.BLACK,
                  settings.WIDTH / 4, 3 * settings.HEIGHT / 4, True)
    pygame.draw.rect(window, settings.GREEN,
                     (settings.WIDTH / 2, settings.HEIGHT / 2, settings.WIDTH / 2, settings.HEIGHT / 2))
    gui.draw_text(window, "Quit", 80, settings.BLACK,
                  3 * settings.WIDTH / 4, 3 * settings.HEIGHT / 4, True)

    play_button.update(window)
