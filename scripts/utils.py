import pygame

def crop_img(sprite_sheet, x, y, w, h, scale_ratio):
    surf = pygame.Surface((w, h))
    surf.blit(sprite_sheet, (x, y, w, h))
    return pygame.transform.scale(surf, scale_ratio)