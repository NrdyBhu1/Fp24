import pygame


def crop_img(sprite_sheet, x, y, w, h, scale_ratio):
    surf = pygame.Surface((w, h))
    surf.blit(sprite_sheet.convert_alpha(), (x, y, w, h))
    surf.set_colorkey((0, 0, 0))
    return pygame.transform.scale(surf, scale_ratio)
