import pygame
import os
IMAGE_PATH = 'E:/Projects/J_Game/data/images/'

def get_img(path):
    img = pygame.image.load(os.path.normpath(IMAGE_PATH + path)).convert()
    return img

def handle_move(player):
    keys = pygame.key.get_pressed()