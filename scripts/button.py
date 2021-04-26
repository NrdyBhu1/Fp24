import pygame

class Button:
    def __init__(self, x, y, w, h, text, font, func, color=(255, 255, 100)):
        self.text = text
        self.font = font
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.func = func
        self.is_hovered = False

    def render(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        font = self.font.get_font(self.rect.h - 4)
        text_rendered = font.render(self.text, True, (255, 255, 255), None)
        text_rect = text_rendered.get_rect()
        text_rect.center = self.rect.center
        win.blit(text_rendered, text_rect)

    def hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.is_hovered = True
            self.color = (100, 100, 100)
        else:
            self.is_hovered = False
            self.color = (255, 255, 100)

    def clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.is_hovered:
            self.func()

