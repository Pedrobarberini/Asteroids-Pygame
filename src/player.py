import pygame
import math

WIDTH = 1280
HEIGHT = 720


class Player:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.angle = 0

        self.vel_x = 0
        self.vel_y = 0

        self.acceleration = 0.2
        self.friction = 0.99

    def update(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.angle += 4

        if keys[pygame.K_RIGHT]:
            self.angle -= 4

        if keys[pygame.K_UP]:

            radians = math.radians(self.angle)

            self.vel_x += math.sin(radians) * self.acceleration
            self.vel_y += math.cos(radians) * self.acceleration

        self.x += self.vel_x
        self.y -= self.vel_y

        self.vel_x *= self.friction
        self.vel_y *= self.friction

        # atravessar tela
        if self.x > WIDTH:
            self.x = 0

        if self.x < 0:
            self.x = WIDTH

        if self.y > HEIGHT:
            self.y = 0

        if self.y < 0:
            self.y = HEIGHT

    def draw(self, screen):

        radians = math.radians(self.angle)

        tip_x = self.x + math.sin(radians) * 20
        tip_y = self.y - math.cos(radians) * 20

        left_x = self.x + math.sin(radians + 2.5) * 20
        left_y = self.y - math.cos(radians + 2.5) * 20

        right_x = self.x + math.sin(radians - 2.5) * 20
        right_y = self.y - math.cos(radians - 2.5) * 20

        pygame.draw.polygon(
            screen,
            (255, 255, 255),
            [
                (tip_x, tip_y),
                (left_x, left_y),
                (right_x, right_y)
            ],
            2
        )