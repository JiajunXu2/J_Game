import pygame
IMAGE_PATH = 'E:\Projects\pygame\data'

def get_img(path):
    img = pygame.image.load(IMAGE_PATH + path).convert()
    return img
