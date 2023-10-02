import pygame
from scripts.spritesheet import load_spritesheet

"""class Player(pygame.sprite.Sprite):
  GRAVITY = 1
  COLOR = (255, 0, 0)
  SPRITES = load_spritesheet("images", "player_char", 32, 32, True)
  ANIMATION_DELAY = 3

  def __init__(self, x, y, width, height) -> None:
    self.rect = pygame.Rect(x, y , width, height)
    self.x_velocity = x
    self.y_velocity = y
    self.direction = "left"
    self.fall_count = 0 # manages the gravity speed
    self.animation_count = 0
    self.mask = None
  
  def move(self, dy, dx):
    self.rect.x += dx
    self.rect.y += dy

  def move_left(self, velocity):
    self.x_velocity = -velocity
    if self.direction != "left":
      self.direction = "left"

  def move_right(self, velocity):
    self.y_velocity = velocity
    if self.direction != "right":
      self.direction = "right"

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
    self.rect = self.sprite.get_rect(topLeft = (self.rect.x, self.rect.y))
    # a mask is a mapping of all the pixel that exist in the sprite
    # masks allow us to preform pixel perfect collision
    # whereas rectangle collision is clunky because the rectangle is langer than our sprite
    self.mask = pygame.mask.from_surface(self.sprite) 

  # called once every frame to control movement and update directions
  def loop(self, fps):
    self.move(self.x_velocity, self.y_velocity)
    self.update_sprite()

  def draw(self, window):
    window.blit(self.sprite, (self.rect.x, self.rect.y))"""