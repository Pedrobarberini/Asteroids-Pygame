import pygame
import math


class Bullet:

    def __init__(self, x, y, angle):

        self.x = x
        self.y = y

        self.speed = 10

        radians = math.radians(angle)

        self.vel_x = math.sin(radians) * self.speed
        self.vel_y = math.cos(radians) * self.speed

    def update(self):

        self.x += self.vel_x
        self.y -= self.vel_y

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.x), int(self.y)),
            3
        )