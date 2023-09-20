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
    
  def ending(self):
    p = ['ending_1.png', 'ending_2.png', 'ending_3.png']
    end = random.choice(p)
    self.end_img = pygame.image.load(f'E:\Projects\pygame\data\images\endpics\{end}')
    self.end_img_pos = [0, 0]
    self.DISPLAYSURF.blit(self.end_img, self.end_img_pos)

if __name__ == 'main':
  new_game = Game()
  new_game.run()
