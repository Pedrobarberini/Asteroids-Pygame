import pygame
import random
import math

WIDTH = 1280
HEIGHT = 720


class Asteroid:

    def __init__(self, size="large", x=None, y=None):

        self.size = size

        if x is not None:
            self.x = x
            self.y = y

        else:

            side = random.choice([
                "top",
                "bottom",
                "left",
                "right"
            ])

            if side == "top":
                self.x = random.randint(0, WIDTH)
                self.y = -100

            elif side == "bottom":
                self.x = random.randint(0, WIDTH)
                self.y = HEIGHT + 100

            elif side == "left":
                self.x = -100
                self.y = random.randint(0, HEIGHT)

            else:
                self.x = WIDTH + 100
                self.y = random.randint(0, HEIGHT)

        # tamanhos
        if size == "large":
            self.radius = 70

        elif size == "medium":
            self.radius = 40

        else:
            self.radius = 20

        self.vel_x = random.uniform(-2, 2)
        self.vel_y = random.uniform(-2, 2)

        self.angle = 0
        self.rotation_speed = random.uniform(-2, 2)

        self.points = []

        self.generate_shape()

    def generate_shape(self):

        total_points = random.randint(8, 14)

        for i in range(total_points):

            angle = (
                math.pi * 2 / total_points
            ) * i

            distance = random.randint(
                int(self.radius * 0.6),
                self.radius
            )

            x = math.cos(angle) * distance
            y = math.sin(angle) * distance

            self.points.append((x, y))

    def update(self):

        self.x += self.vel_x
        self.y += self.vel_y

        self.angle += self.rotation_speed

        if self.x > WIDTH + 100:
            self.x = -100

        if self.x < -100:
            self.x = WIDTH + 100

        if self.y > HEIGHT + 100:
            self.y = -100

        if self.y < -100:
            self.y = HEIGHT + 100

    def split(self):

        asteroids = []

        if self.size == "large":

            for i in range(2):

                asteroids.append(
                    Asteroid(
                        "medium",
                        self.x,
                        self.y
                    )
                )

        elif self.size == "medium":

            for i in range(2):

                asteroids.append(
                    Asteroid(
                        "small",
                        self.x,
                        self.y
                    )
                )

        return asteroids

    def draw(self, screen):

        rotated_points = []

        radians = math.radians(self.angle)

        for point in self.points:

            x, y = point

            rotated_x = (
                x * math.cos(radians)
                - y * math.sin(radians)
            )

            rotated_y = (
                x * math.sin(radians)
                + y * math.cos(radians)
            )

            rotated_points.append(
                (
                    self.x + rotated_x,
                    self.y + rotated_y
                )
            )

        pygame.draw.polygon(
            screen,
            (200, 200, 200),
            rotated_points,
            2
        )