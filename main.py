import pygame
import sys
import random
from scripts.entities import PhysicsEntity
from scripts.utility import get_img

class Game:
  def __init__(self):
    pygame.init()
    pygame.display.set_caption('J Game')
    self.DISPLAYSURF = pygame.display.set_mode((512, 760))
    self.clock = pygame.time.Clock()
    """p = ['princess_1.png', 'princess_2.png', 'princess_3.png']
    princess = random.choice(p)
    self.img = pygame.image.load(f'E:\Projects\pygame\data\images\endpics\{princess}')
    self.img_pos = [0, 0]"""
