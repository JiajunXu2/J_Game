import pygame

class PhysicsEntity:
    def __init__(self, game, entity_type, position, size) -> None:
        self.game = game
        self.type = entity_type
        self.pos = list(position)
        self.size = size
        self.velocity = [0, 0]

    def update(self, movement = [0, 0]):
        frame_movement = (self.velocity[0] + movement[0], self.velocity[1] + movement[1])
        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]

    def render(self, surface):
        surface.blit() # fill in later
