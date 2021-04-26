import pygame
from scripts.utils import crop_img

class Player:
    def __init__(self):
        self.rect = pygame.Rect(600, 100, 50, 70)
        self.velocity = 10
        self.axis = 0
        self.sprite = pygame.image.load("assets/img/player.png")
        self.frames = []
        self.current_frame = 0
        self.init()

    def init(self):
        self.frames.append(crop_img(self.sprite, 0, 0, 16, 16, (128, 128)))
        self.frames.append(crop_img(self.sprite, 16, 0, 16, 16, (128, 128)))
        self.frames.append(crop_img(self.sprite, 0, 16, 16, 16, (128, 128)))

    def render(self, win):
        # if self.current_frame >= 2:
            # self.current_frame = 0
        # self.current_frame += 1
        win.blit(self.frames[self.current_frame], self.rect)

    def move(self, event):
        self.rect.x += self.velocity * self.axis
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.axis = 1
            elif event.key == pygame.K_a:
                self.axis = -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.axis = 0
            elif event.key == pygame.K_a:
                self.axis = 0
