import pygame
import sys
import random
import math

from main import run_game

pygame.init()



WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids")

clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLUE = (120, 180, 255)
BG = (5, 5, 15)
GRAY = (40, 40, 40)


title_font = pygame.font.SysFont(
    "Arial",
    120,
    bold=True
)

menu_font = pygame.font.SysFont(
    "Arial",
    40,
    bold=True
)

small_font = pygame.font.SysFont(
    "Arial",
    28
)


menu_options = [
    "JOGAR",
    "CONFIGURAÇÕES",
    "SAIR"
]

selected = 0

volume = 0.5


stars = []

for i in range(250):

    stars.append({

        "x": random.randint(0, WIDTH),
        "y": random.randint(0, HEIGHT),

        "size": random.randint(1, 3),

        "speed": random.uniform(0.2, 1.2)

    })


class MenuAsteroid:

    def __init__(self):

        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)

        self.radius = random.randint(20, 90)

        self.speed = random.uniform(0.2, 1)

        self.rotation = 0
        self.rotation_speed = random.uniform(-1, 1)

        self.points = []

        self.generate_shape()

    def generate_shape(self):

        total = random.randint(8, 14)

        for i in range(total):

            angle = (math.pi * 2 / total) * i

            distance = random.randint(
                int(self.radius * 0.7),
                self.radius
            )

            x = math.cos(angle) * distance
            y = math.sin(angle) * distance

            self.points.append((x, y))

    def update(self):

        self.x -= self.speed

        self.rotation += self.rotation_speed

        if self.x < -150:

            self.x = WIDTH + 150
            self.y = random.randint(0, HEIGHT)

    def draw(self, screen):

        rotated_points = []

        radians = math.radians(self.rotation)

        for point in self.points:

            x, y = point

            rx = (
                x * math.cos(radians)
                - y * math.sin(radians)
            )

            ry = (
                x * math.sin(radians)
                + y * math.cos(radians)
            )

            rotated_points.append(
                (
                    self.x + rx,
                    self.y + ry
                )
            )

        # glow
        pygame.draw.polygon(
            screen,
            GRAY,
            rotated_points,
            8
        )

        # asteroid
        pygame.draw.polygon(
            screen,
            WHITE,
            rotated_points,
            2
        )


menu_asteroids = []

for i in range(10):

    menu_asteroids.append(
        MenuAsteroid()
    )

def draw_button(text, x, y, width, height, active):

    color = BLUE if active else WHITE

    points = [

        (x + 20, y),

        (x + width, y),

        (x + width, y + height - 20),

        (x + width - 20, y + height),

        (x, y + height),

        (x, y + 20)

    ]

    # glow
    pygame.draw.polygon(
        screen,
        (40, 40, 70),
        points,
        8
    )

    pygame.draw.polygon(
        screen,
        color,
        points,
        2
    )

    rendered = menu_font.render(
        text,
        True,
        color
    )

    text_rect = rendered.get_rect(
        center=(x + width // 2, y + height // 2)
    )

    screen.blit(rendered, text_rect)


def draw_volume():

    volume_text = small_font.render(
        "VOLUME",
        True,
        WHITE
    )

    screen.blit(volume_text, (560, 645))

    # barra fundo
    pygame.draw.line(
        screen,
        GRAY,
        (500, 700),
        (780, 700),
        10
    )

    # barra ativa
    pygame.draw.line(
        screen,
        WHITE,
        (500, 700),
        (
            500 + (volume * 2.8),
            700
        ),
        6
    )

    # círculo
    pygame.draw.circle(
        screen,
        WHITE,
        (
            int(500 + volume * 2.8),
            700
        ),
        12
    )


while True:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            # navegação
            if event.key == pygame.K_DOWN:

                selected += 1

                if selected >= len(menu_options):
                    selected = 0

            if event.key == pygame.K_UP:

                selected -= 1

                if selected < 0:
                    selected = len(menu_options) - 1

            # volume
            if selected == 1:

                if event.key == pygame.K_RIGHT:

                    volume += 5

                    if volume > 100:
                        volume = 100

                if event.key == pygame.K_LEFT:

                    volume -= 5

                    if volume < 0:
                        volume = 0

            # selecionar
            if event.key == pygame.K_RETURN:

                option = menu_options[selected]

                if option == "JOGAR":

                    run_game()

                elif option == "SAIR":

                    pygame.quit()
                    sys.exit()


    for star in stars:

        star["x"] -= star["speed"]

        if star["x"] < 0:

            star["x"] = WIDTH
            star["y"] = random.randint(0, HEIGHT)

    for asteroid in menu_asteroids:

        asteroid.update()


    screen.fill(BG)

    # estrelas
    for star in stars:

        pygame.draw.circle(
            screen,
            WHITE,
            (
                int(star["x"]),
                int(star["y"])
            ),
            star["size"]
        )

    # asteroids
    for asteroid in menu_asteroids:

        asteroid.draw(screen)

    # glow do título
    glow = title_font.render(
        "ASTEROIDS",
        True,
        (40, 40, 60)
    )

    screen.blit(glow, (350, 65))

    # título
    title = title_font.render(
        "ASTEROIDS",
        True,
        WHITE
    )

    screen.blit(title, (340, 50))

    # linha
    pygame.draw.line(
        screen,
        WHITE,
        (350, 220),
        (930, 220),
        2
    )

    # botões
    start_y = 300

    for i, option in enumerate(menu_options):

        draw_button(

            option,

            440,
            start_y + i * 120,

            400,
            80,

            selected == i

        )

    # volume
    if selected == 1:

        draw_volume()

    pygame.display.flip()

    clock.tick(60)