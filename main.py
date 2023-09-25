import pygame
import sys
import random
from scripts.entities import PhysicsEntity
from scripts.utility import get_img
from scripts.spritesheet import flip, load_spritesheet

class Player(pygame.sprite.Sprite):
  GRAVITY = 1

  def __init__(self, x, y, width, height) -> None:
    self.rect = pygame.Rect(x, y , width, height)
    self.x_velocity = x
    self.y_velocity = y
    self.direction = "left"
    self.fall_count = 0
    self.animation_count = 0

class Game:
  def __init__(self):
    pygame.init()
    pygame.display.set_caption('J Game')
    self.DISPLAYSURF = pygame.display.set_mode((512, 760))
    self.clock = pygame.time.Clock()

  def run(self):
    while True:
      # self.DISPLAYSURF.blit(self.img, self.img_pos)

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
        # 10 frames per second
        self.clock.tick(10)
    
  def ending(self):
    p = ['ending_1.png', 'ending_2.png', 'ending_3.png']
    end = random.choice(p)
    self.end_img = pygame.image.load(f'E:\Projects\pygame\data\images\endpics\{end}')
    self.end_img_pos = [0, 0]
    self.DISPLAYSURF.blit(self.end_img, self.end_img_pos)

if __name__ == 'main':
  new_game = Game()
  new_game.run()
