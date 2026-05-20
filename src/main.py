import pygame
import sys
import math

from player import Player
from bullet import Bullet
from asteroid import Asteroid
from particle import Particle


def run_game(sounds):



    pygame.init()

    WIDTH = 1280
    HEIGHT = 720

    screen = pygame.display.set_mode(
        (WIDTH, HEIGHT)
    )
     
    pygame.display.set_caption("Asteroids")

    clock = pygame.time.Clock()

    font = pygame.font.SysFont(
        "Arial",
        32
    )

    player = Player(
        WIDTH // 2,
        HEIGHT // 2
    )

    bullets = []
    asteroids = []
    particles = []

    score = 0
    lives = 2
    game_over = False
    death_sound_played = False

    spawn_timer = 0

    for i in range(5):
        asteroids.append(Asteroid())


    def create_explosion(x, y):

        for i in range(25):

            particles.append(
                Particle(x, y)
            )
            sounds.play_explosion()


    while True:


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over:

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:

                        bullets.append(
                            Bullet(
                                player.x,
                                player.y,
                                player.angle
                            )
                        )
                        sounds.play_shooting()

            else:

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_r:

                        player.x = WIDTH // 2
                        player.y = HEIGHT // 2

                        player.vel_x = 0
                        player.vel_y = 0

                        bullets.clear()
                        asteroids.clear()
                        particles.clear()

                        for i in range(5):
                            asteroids.append(
                                Asteroid()
                            )

                        score = 0
                        lives = 2   
                        death_sound_played = False

                        game_over = False

        if not game_over:


            player.update()


            for bullet in bullets[:]:

                bullet.update()

                if (
                    bullet.x < 0 or
                    bullet.x > WIDTH or
                    bullet.y < 0 or
                    bullet.y > HEIGHT
                ):
                    bullets.remove(bullet)


            for asteroid in asteroids:
                asteroid.update()


            for particle in particles[:]:

                particle.update()

                if particle.life <= 0:
                    particles.remove(
                        particle
                    )


            for bullet in bullets[:]:

                for asteroid in asteroids[:]:

                    distance = math.sqrt(
                        (bullet.x - asteroid.x) ** 2 +
                        (bullet.y - asteroid.y) ** 2
                    )

                    if distance < asteroid.radius:

                        if bullet in bullets:
                            bullets.remove(bullet)

                        if asteroid in asteroids:
                            asteroids.remove(
                                asteroid
                            )

                        create_explosion(
                            asteroid.x,
                            asteroid.y
                        )

                        new_asteroids = asteroid.split()

                        asteroids.extend(
                            new_asteroids
                        )

                        score += 10

                        break

            for asteroid in asteroids[:]:

                distance = math.sqrt(
                    (player.x - asteroid.x) ** 2 +
                    (player.y - asteroid.y) ** 2
                )

                if distance < asteroid.radius:

                    create_explosion(
                        player.x,
                        player.y
                    )

                    asteroids.remove(
                        asteroid
                    )

                    lives -= 1

                    player.x = WIDTH // 2
                    player.y = HEIGHT // 2

                    player.vel_x = 0
                    player.vel_y = 0

                    if lives <= 0:
                        game_over = True


            spawn_timer += 1

            if spawn_timer >= 180:

                asteroids.append(
                    Asteroid()
                )

                spawn_timer = 0


        screen.fill((10, 10, 20))

        if not game_over:
            player.draw(screen)

        for bullet in bullets:
            bullet.draw(screen)

        for asteroid in asteroids:
            asteroid.draw(screen)

        for particle in particles:
            particle.draw(screen)

        # score
        score_text = font.render(
            f"Score: {score}",
            True,
            (255, 255, 255)
        )

        screen.blit(score_text, (20, 20))

        # vidas
        lives_text = font.render(
            f"Vidas: {lives}",
            True,
            (255, 255, 255)
        )

        screen.blit(lives_text, (20, 60))

        # game over
        if game_over:

            if not death_sound_played:
                sounds.play_death()
                death_sound_played = True

            game_over_text = font.render(
                "GAME OVER",
                True,
                (255, 255, 255)
            )

            restart_text = font.render(
                "Pressione R para reiniciar",
                True,
                (255, 255, 255)
            )

            screen.blit(
                game_over_text,
                (
                    WIDTH // 2 - 120,
                    HEIGHT // 2 - 50
                )
            )

            screen.blit(
                restart_text,
                (
                    WIDTH // 2 - 220,
                    HEIGHT // 2 + 10
                )
            )

        pygame.display.flip()

        clock.tick(60)
if __name__ == "__main__":
    run_game()