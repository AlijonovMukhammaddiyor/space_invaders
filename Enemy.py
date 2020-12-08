from random import randint

import pygame


class Enemy(object):
    def __init__(self, screen: pygame.Surface, speed, path):
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.screen = screen

        self.rect = self.image.get_rect()
        self.rect.left = randint(10, screen.get_width() - 10 - self.image.get_width())
        self.rect.bottom = 0
        self.speed = speed
        self.shoot = [0, 0]
        self.shooted = False

    def update(self):
        self.screen.blit(self.image, self.rect)
        self.rect.bottom += self.speed

    def check_pos(self):
        if self.rect.top >= self.screen.get_height():
            return False
        else:
            return True

    def isShooting(self):
        if self.shoot[0] < 2 and self.rect.bottom - self.shoot[1] > 100 \
                and 150 < self.rect.bottom < self.screen.get_height() - 200:
            self.shoot[0] += 1
            self.shoot[1] = self.rect.bottom
            return True
        return False
