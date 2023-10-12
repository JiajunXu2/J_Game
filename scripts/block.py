from scripts.objects import Object
from os.path import join, isfile
from scripts.utility import load_block
import pygame

class Block(Object):
    def __init__(self, x, y, size) -> None:
        super().__init__(x, y, size, size)
        block = load_block(size, "terrain.png")
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
    
