import pygame

class Button:
    def __init__(self, x, y, w, h, text, font, func, color=(255, 255, 100)):
        self.text = text
        self.font = font
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.sound = pygame.mixer.Sound("./assets/sounds/select.mkv")
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
            self.sound.play(maxtime=1)
            self.is_hovered = True
            self.color = (100, 100, 100)
        else:
            self.sound.stop()
            self.is_hovered = False
            self.color = (255, 255, 100)

    def clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.is_hovered:
            self.func()

class RadioButton:
    def __init__(self, x, y, size, text, font):
        self.rect = pygame.Rect(x, y, size, size)
        self.size = size
        self.text = text
        self.font = font
        self.is_hovered = False
        self.selected = False
        self.color = (100, 100, 100)

    def render(self, win):
        font = self.font.get_font(self.size)
        txt = font.render(self.text, True, (200, 200, 200), None)
        txt_rect = txt.get_rect()
        txt_rect.centery = self.rect.centery
        txt_rect.x = self.rect.x + self.size + self.size/2
        win.blit(txt, txt_rect)
        if not self.selected:
            pygame.draw.rect(win, self.color, self.rect, int(self.size-(self.size/2)))
        else:
            pygame.draw.rect(win, (10, 10, 200), self.rect, int(self.size-(self.size/2)))

    def hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.color = (255, 255, 255)
            self.is_hovered = True
        else:
            self.color = (100, 100, 100)
            self.is_hovered = False

    def clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.is_hovered:
            self.selected = not self.selected
