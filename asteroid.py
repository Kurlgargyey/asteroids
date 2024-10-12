import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        offshoot_angle = random.uniform(20, 50)
        child_vels = list(map(
            lambda x:self.velocity.rotate(offshoot_angle*x), [1, -1]
        ))
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        for vel in child_vels:
            new_asteroid =Asteroid(self.position.x, self.position.y, child_radius)
            new_asteroid.velocity = vel*1.2