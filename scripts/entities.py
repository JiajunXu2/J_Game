import pygame

class PhysicsEntity:
    def __init__(self, game, entity_type, position, size) -> None:
        self.game = game
        self.type = entity_type
        self.pos = list(position)
        self.size = size
        self.velocity = [0, 0]
