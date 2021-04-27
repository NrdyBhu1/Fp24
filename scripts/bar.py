import pygame

class Bar:
    def __init__(self, pos, value=0, size_ratio=1):
        self.pos = pos
        self.value = value
        self.holder = pygame.Rect(self.pos[0], self.pos[1], 100*size_ratio, 10*size_ratio)
        self.bar = pygame.Rect(0, 0, 15*size_ratio, 15*size_ratio)
        self.is_hovered = False
        self.bar_color = (100, 100, 100)

    def render(self, win):
        self.bar.centery = self.holder.centery
        pygame.draw.rect(win, (100, 100, 100), self.holder)
        pygame.draw.rect(win, self.bar_color, self.bar)

    def hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.holder.collidepoint(mouse_pos):
            self.bar_color = (200, 200, 200)
            self.is_hovered = True
        else:
            self.is_hovered = True
            self.bar_color = (100, 100, 100)

    def dragged(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if self.bar.x < self.holder.x:
            self.bar.x = self.holder.x-5
        elif self.bar.x > self.holder.x+self.holder.w:
            self.bar.x = self.holder.x+self.holder.w-15

        if event.type == pygame.MOUSEBUTTONDOWN and self.is_hovered:
            if mouse_pos[0] < self.holder.x+self.holder.w and mouse_pos[0] > self.holder.x:
                if mouse_pos[1] > self.holder.y and mouse_pos[1] < self.holder.y+self.holder.h:
                    self.bar.centerx = mouse_pos[0]
