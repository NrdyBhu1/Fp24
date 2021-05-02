import pygame


class Font:
    def __init__(self, font_name):
        self.fontname = font_name

    def get_font(self, size):
        return pygame.font.Font(self.fontname, size)
