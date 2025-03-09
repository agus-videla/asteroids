import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_KINDS, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        first_vel = self.velocity.rotate(angle)
        second_vel = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first = Asteroid(self.position[0], self.position[1], new_radius)
        second = Asteroid(self.position[0], self.position[1], new_radius)
        first.velocity = first_vel * 1.2
        second.velocity = second_vel * 1.2
