import pygame
class Player(pygame.sprite.Sprite):
  GRAVITY = 1
  COLOR = (255, 0, 0)

  def __init__(self, x, y, width, height) -> None:
    self.rect = pygame.Rect(x, y , width, height)
    self.x_velocity = x
    self.y_velocity = y
    self.direction = "left"
    self.fall_count = 0
    self.animation_count = 0
  
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
  
  # called once every frame to control movement and update directions
  def loop(self, fps):
    self.move(self.x_velocity, self.y_velocity)

  def draw(self, window):
    pygame.draw.rect(window, self.COLOR, self.rect)