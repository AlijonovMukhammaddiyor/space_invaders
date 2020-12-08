import pygame


class Bullet(object):

    def __init__(self, rect: pygame.Rect, speed, screen: pygame.Surface, color, upDown, x_change=0):
        if upDown == -1:
            self.bullet = pygame.Surface((10, 10))
        else:
            self.bullet = pygame.Surface((3, 6))
        self.bullet.fill(color)
        self.rect = self.bullet.get_rect()
        self.screen = screen
        self.s_rect = self.screen.get_rect()

        if upDown == 1:
            self.rect.bottom = rect.top
        elif upDown == -1:
            self.rect.top = rect.bottom
        self.rect.centerx = rect.centerx
        self.speed = speed

        self.dir = upDown
        self.x_change = x_change
        self.hit = False

    def check_pos(self):
        if self.rect.bottom <= 0 or self.rect.top >= self.s_rect.bottom:
            return False
        return True

    def update(self):
        self.screen.blit(self.bullet, self.rect)
        if self.dir < 0:
            self.rect.bottom += self.speed
        else:
            self.rect.bottom -= self.speed
        self.rect.centerx += self.x_change
