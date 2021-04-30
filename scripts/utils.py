import pygame

def crop_img(sprite_sheet, x, y, w, h, scale_ratio):
    surf = pygame.Surface((w, h)).convert_alpha()
    surf.blit(sprite_sheet.convert_alpha(), (x, y, w, h))
    return pygame.transform.scale(surf, scale_ratio)
