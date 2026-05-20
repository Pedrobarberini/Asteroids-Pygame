import pygame
import os

# Caminho base para os assets
BASE = os.path.join(os.path.dirname(__file__), '..', 'assets', 'sounds')

def _load(filename):
    return pygame.mixer.Sound(os.path.join(BASE, filename))

class Sounds:
    def __init__(self):
        pygame.mixer.init()

        # Efeitos sonoros
        self.shooting  = _load('Shooting-sound.mp3')
        self.explosion = _load('Explosion-sound.mp3')
        self.death     = _load('Death-sound.mp3')

        # Volumes individuais (0.0 a 1.0)
        self.shooting.set_volume(0.4)
        self.explosion.set_volume(0.7)
        self.death.set_volume(0.8)

    def play_shooting(self):
        self.shooting.play()

    def play_explosion(self):
        self.explosion.play()

    def play_death(self):
        self.death.play()

    def play_menu(self):
        pygame.mixer.music.load(
            os.path.join(BASE, 'Menu-music.mp3')
        )
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)   # -1 = loop infinito

    def stop_menu(self):
        pygame.mixer.music.stop()