import pygame
from scripts.utils import crop_img

class Coin:
    def __init__(self, pos, size):
        self.sprite = pygame.image.load("assets/img/coin.png")
        self.sprite = self.sprite.convert_alpha(self.sprite)
        self.frames = []
        self.current_frame = 0
        self.rect = pygame.Rect(pos[0], pos[1], size, size)
        self.size = size
        self.init()
    
    def init(self):
        self.frames.append(crop_img(self.sprite, 0, 0, 16, 16, (self.size, self.size)))
        self.frames.append(crop_img(self.sprite, 16, 0, 16, 16, (self.size, self.size)))
        self.frames.append(crop_img(self.sprite, 32, 0, 16, 16, (self.size, self.size)))
        self.frames.append(crop_img(self.sprite, 0, 16, 16, 16, (self.size, self.size)))
        self.frames.append(crop_img(self.sprite, 16, 16, 16, 16, (self.size, self.size)))
        self.frames.append(crop_img(self.sprite, 32, 16, 16, 16, (self.size, self.size)))
    
    def render(self, win):
        win.blit(self.frames[self.current_frame], self.rect)
