from scripts.objects import Object
from os.path import join, isfile
import pygame

class Block(Object):
    def __init__(self, x, y, size) -> None:
        super().__init__(x, y, size, size)
        block = self.load_block(size, "terrain.png")
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
    
    def load_block(self, size, name):
        path = join("E:\Projects\J_Game\data\images", "terrain", name)
        image = pygame.image.load(path).convert_alpha()
        surface = pygame.Surface((size, size), pygame.SRCALPHA)
        rect = pygame.Rect(96, 0, (size, size))
        surface.blit(image, (0, 0), rect)
        return pygame.transform.scale2x(surface)
