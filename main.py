import pygame
import sys
import random
import pygame
from os.path import join, isfile
from os import listdir
from scripts.entities import PhysicsEntity
from scripts.utility import *
from scripts.block import Block
from scripts.objects import Object

WIDTH = 800
HEIGHT = 450
fps = 20

pygame.init()
pygame.display.set_caption('J Game')
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))

def flip(sprites):
  return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_spritesheet(dir1, dir2, height, width, direction = False):
  path = join("E:\Projects-Python\J_Game\data", dir1, dir2)
  print(path)
  images = [f for f in listdir(path) if isfile(join(path, f))]

  all_sprites = {}

  for img in images:
      sprite_sheet = pygame.image.load(join(path, img)).convert_alpha()

      sprites = []
      for i in range(sprite_sheet.get_width() // width):
          surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
          rect = pygame.Rect(i * width, 0, width, height)
          surface.blit(sprite_sheet, (0, 0), rect)
          sprites.append(pygame.transform.scale2x(surface))

      if direction:
          all_sprites[img.replace(".png", "") + "_right"] = sprites
          all_sprites[img.replace(".png", "") + "_left"] = flip(sprites)
      else:
          all_sprites[img.replace(".png", "")] = sprites

  return all_sprites

class Player(pygame.sprite.Sprite):
  GRAVITY = 1
  COLOR = (255, 0, 0)
  SPRITES = load_spritesheet("images", "player_char", 32, 32, True)
  ANIMATION_DELAY = 1

  def __init__(self, x, y, width, height) -> None:
    self.rect = pygame.Rect(x, y, width, height)
    self.x_velocity = 0
    self.y_velocity = 0
    self.direction = "right"
    self.fall_count = 0 # manages the gravity speed
    self.animation_count = 0
    self.mask = None
  
  def move(self, dx, dy):
    self.rect.x += dx
    self.rect.y += dy

  def move_left(self, velocity):
    self.x_velocity = -velocity
    if self.direction != "left":
      self.direction = "left"
      self.animation_count = 0

  def move_right(self, velocity):
    self.x_velocity = velocity
    if self.direction != "right":
      self.direction = "right"
      self.animation_count = 0

  def update_sprite(self):
    spritesheet = "idle"
    if self.x_velocity != 0:
      spritesheet = "run"
    spritesheet_name = spritesheet + "_" + self.direction
    sprites = self.SPRITES[spritesheet_name]
    sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
    self.sprite = sprites[sprite_index]
    self.animation_count += 1
    self.update()

  def update(self):
    # the rectangle we're using is constantly adjusting to our character
    self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
    # a mask is a mapping of all the pixel that exist in the sprite
    # masks allow us to preform pixel perfect collision
    # whereas rectangle collision is clunky because the rectangle is langer than our sprite
    self.mask = pygame.mask.from_surface(self.sprite) 

  # called once every frame to control movement and update directions
  def loop(self, fps):
    self.move(self.x_velocity, self.y_velocity)
    self.update_sprite()

  def draw(self, window):
    window.blit(self.sprite, (self.rect.x, self.rect.y))

def draw(display, coordinates, image = None, block = None):
  if image:
    display.blit(image, coordinates)
  if block:
    pass
  pygame.display.update()

def draw_player(display, player):
  player.draw(display)
  pygame.display.update()

def main(display):
  clock = pygame.time.Clock()
  player = Player(100, 100, 50, 50)
  #block = Block(0, 0, 96)
  sky = get_img("backgrounds/sky.png")
  ground = get_img("backgrounds/ground.png")
  draw(display, [0, 0], sky)
  draw(display, [0, 300], ground)
  while True:
    clock.tick(fps)
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
    #draw(display, block, [0, 0])
    draw(display, [0, 0], sky)
    draw(display, [0, 300], ground)
    player.loop(fps)
    handle_move(player)
    draw_player(display, player)
    
def ending(self):
  p = ['ending_1.png', 'ending_2.png', 'ending_3.png']
  end = random.choice(p)
  self.end_img = pygame.image.load(f'E:\Projects\pygame\data\images\endpics\{end}')
  self.end_img_pos = [0, 0]
  self.DISPLAYSURF.blit(self.end_img, self.end_img_pos)

if __name__ == '__main__':
  main(DISPLAYSURF)
  #this is a test