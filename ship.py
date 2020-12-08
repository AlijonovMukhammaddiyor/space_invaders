import pygame


class Ship(object):

    def __init__(self, screen: pygame.Surface, speed, path):
        self.screen = screen
        self.image = pygame.image.load(path).convert()
        # now initialize position
        self.rect = self.image.get_rect()
        self.s_rect = self.screen.get_rect()

        self.rect.centerx = self.s_rect.centerx
        self.rect.bottom = self.s_rect.bottom

        self.speed = speed
        self.moving_right = False
        self.moving_left = False
        self.shooted = 0

    def blitShip(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right <= self.screen.get_width() - self.speed:
            self.rect.right += self.speed

        elif self.moving_left and self.rect.left >= self.speed:
            self.rect.left -= self.speed
