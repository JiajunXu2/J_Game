import pygame
from os.path import join, isfile
from os import listdir

def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_spritesheet(dir1, dir2, height, width, direction = False):
    path = join("E:\Projects\J_Game\data", dir1, dir2)
    print(path)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for img in images:
        sprite_sheet = pygame.image.load(join(path, img)).convert()

        sprites = []
        for i in range(sprite_sheet.get_width()// width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(surface)

        if direction:
            all_sprites[img.replace(".png", "") + "_right"] + sprites
            all_sprites[img.replace(".png", "") + "_left"] + flip(sprites)
        else:
            all_sprites[img.replace(".png", "")] + sprites

    return all_sprites
