import pygame
import os
from os.path import join
IMAGE_PATH = 'E:/Projects-Python/J_Game/data/images/'
PLAYER_VELOCITY = 8

def get_img(path):
    img = pygame.image.load(os.path.normpath(IMAGE_PATH + path)).convert()
    return img

def handle_move(player):
    keys = pygame.key.get_pressed()
    player.x_velocity = 0
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VELOCITY)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VELOCITY)
    
def handle_vertical_collision(player, objects, y_velocity):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            # player falling down landing on object
            if y_velocity > 0: 
                pass
            # jumping up hitting object
            elif y_velocity < 0:
                pass
        collided_objects.append(obj)
    return collided_objects

def load_block(size, name):
    path = join("E:\Projects-Python\J_Game\data\images", "terrain", name)
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)
