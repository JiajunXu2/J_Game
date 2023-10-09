import pygame
import os
IMAGE_PATH = 'E:/Projects/J_Game/data/images/'
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
    