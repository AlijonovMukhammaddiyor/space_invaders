from random import randint
from sys import exit

import pygame
from pygame.locals import *

from Bullet import Bullet
from Enemy import Enemy
from ship import Ship

pygame.font.init()
pygame.mixer.init()


class GameFunction(object):
    def __init__(self, screen, setting):
        self.screen = screen
        self.setting = setting
        self.score = 0
        self.total_aliens = 0
        self.missed_aliens = 0
        self.over = False
        self.shoot_sound = pygame.mixer.Sound(self.setting.shoot_sound_path)
        self.kill_sound = pygame.mixer.Sound(self.setting.kill_sound_path)
        self.lives = 3

    def check_events(self, ship: Ship, bullets: list[Bullet], aliens: list[Enemy], al_bullet: list[Bullet]):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(1)
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    ship.moving_right = True
                elif event.key == K_LEFT:
                    ship.moving_left = True

            elif event.type == KEYUP:
                if event.key == K_RIGHT:
                    ship.moving_right = False
                if event.key == K_LEFT:
                    ship.moving_left = False
            self.check_fire(ship.rect, event, bullets)
        self.addEnemy(aliens)
        self.alien_shooting(al_bullet, ship, aliens)

    def updateScreen(self, ship: Ship, bullets: list[Bullet], aliens: list[Enemy], al_bullet: list[Bullet]):
        self.screen.fill(self.setting.bg)
        if self.lives == 0:
            self.game_over()
            self.over = True
        else:
            ship.update()
            GameFunction.bullet_update(bullets)
            GameFunction.bullet_update(al_bullet)
            self.find_collision(ship, bullets, al_bullet, aliens)
            self.updateEnemy(aliens)
            ship.blitShip()
        self.score_board()
        pygame.display.update()
        if self.over:
            return False
        return True

    def check_fire(self, rect, event, bullets: list[Bullet]):
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bullets.append(Bullet(rect, self.setting.ship_bul_speed, self.screen, self.setting.ship_bul_color, 1))
                self.shoot_sound.play()

    @staticmethod
    def bullet_update(bullets: list[Bullet]):
        for bullet in bullets:
            if bullet.hit or not bullet.check_pos():
                bullets.remove(bullet)
            else:
                bullet.update()

    def addEnemy(self, aliens: list[Enemy]):
        if not aliens:
            aliens.append(Enemy(self.screen, self.setting.enemy_speed, self.setting.enemy_img_path))
            self.total_aliens += 1
        if aliens[-1].rect.top >= 50:
            aliens.append(Enemy(self.screen, self.setting.enemy_speed, self.setting.enemy_img_path))
            self.total_aliens += 1

    def updateEnemy(self, aliens: list[Enemy]):
        if not aliens[0].check_pos():
            self.missed_aliens += 1
            aliens.remove(aliens[0])
        for alien in aliens:
            if alien.shooted:
                aliens.remove(alien)
            else:
                alien.update()

    def alien_shooting(self, bullets: list[Bullet], ship: Ship, aliens: list[Enemy]):
        index = randint(0, len(aliens) - 1)
        if aliens[index].isShooting():
            ship_x = ship.rect.centerx
            alien_x = aliens[index].rect.centerx
            x_change = self.setting.en_bul_speed * (ship_x - alien_x) / abs(aliens[index].rect.bottom - ship.rect.top)
            bullets.append(
                Bullet(aliens[index].rect, self.setting.en_bul_speed, self.screen, self.setting.en_bul_col, -1,
                       x_change))

    def find_collision(self, ship: Ship, ship_bullets: list[Bullet], al_bullets: list[Bullet], aliens: list[Enemy]):
        for bullet in al_bullets:
            if bullet.rect.colliderect(ship.rect):
                bullet.hit = True
                self.lives -= 1
                ship.shooted += 1
        for bullet in ship_bullets:
            for alien in aliens:
                if bullet.rect.colliderect(alien.rect):
                    bullet.hit = True
                    self.kill_sound.play()
                    alien.shooted = True
                    self.score += 1
                    break

    def score_board(self):
        font = pygame.font.SysFont('arial', self.setting.font_size, True)
        score = font.render("Score: " + str(self.score) + " | Missed: " + str(self.missed_aliens), True,
                            self.setting.font_col).convert_alpha()
        s_rect = score.get_rect()
        s_rect.center = (self.setting.score_x + score.get_width() / 2, self.setting.score_y + score.get_height() / 2)
        self.screen.blit(score, s_rect)
        lives = font.render("Lives: " + str(self.lives), True, self.setting.font_col).convert_alpha()
        l_rect = lives.get_rect()
        l_rect.center = (self.screen.get_width() - lives.get_width() / 2 - 5, 5 + lives.get_height() / 2)
        self.screen.blit(lives, l_rect)

    def game_over(self):
        font = pygame.font.SysFont('arial', self.setting.game_over_size, True)
        over = font.render("Game Over", True,
                           self.setting.font_col).convert_alpha()
        s_rect = over.get_rect()
        s_rect.center = (self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.screen.blit(over, s_rect)
        font2 = pygame.font.SysFont('arial', self.setting.game_over_size - 10)
        again = font2.render("Press any key to play again ...", True,
                             self.setting.font_col).convert_alpha()
        a_rect = again.get_rect()
        a_rect.center = (self.screen.get_width() / 2, self.screen.get_height() / 2 + 2 * over.get_height())
        self.screen.blit(again, a_rect)

    @staticmethod
    def check_again():
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    return True
                elif event.type == QUIT:
                    return False
