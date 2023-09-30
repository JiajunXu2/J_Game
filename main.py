import pygame
import sys
import random
from scripts.entities import PhysicsEntity
from scripts.utility import get_img
from scripts.spritesheet import flip, load_spritesheet

WIDTH = 800
HEIGHT = 450
fps = 20

class Game:
  def __init__(self):
    pygame.init()
    pygame.display.set_caption('J Game')
    self.DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
    self.clock = pygame.time.Clock()

  def run(self):
    while True:
      self.DISPLAYSURF.blit(get_img("backgrounds/sky.png"), [0, 0])
      self.DISPLAYSURF.blit(get_img("backgrounds/ground.png"), [0, 300])
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.KEYDOWN:
          print("key down")
        if event.type == pygame.KEYUP:
          print("key up")
        if event.type == pygame.MOUSEMOTION:
          print(event.pos)
        pygame.display.update()
        self.clock.tick(fps)
    
  def ending(self):
    p = ['ending_1.png', 'ending_2.png', 'ending_3.png']
    end = random.choice(p)
    self.end_img = pygame.image.load(f'E:\Projects\pygame\data\images\endpics\{end}')
    self.end_img_pos = [0, 0]
    self.DISPLAYSURF.blit(self.end_img, self.end_img_pos)

if __name__ == '__main__':
  new_game = Game()
  new_game.run()
