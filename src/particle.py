import pygame
import random
import math


class Particle:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(1, 6)

        self.vel_x = math.cos(angle) * speed
        self.vel_y = math.sin(angle) * speed

        self.life = random.randint(20, 40)

        self.size = random.randint(1, 3)

    def update(self):

        self.x += self.vel_x
        self.y += self.vel_y

        self.life -= 1

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.x), int(self.y)),
            self.size
        )