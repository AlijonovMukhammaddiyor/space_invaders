import pygame

from Settings import Setting
from game_functions import GameFunction
from ship import Ship

#############################################################################
setting = Setting(1000, 750)

screen = pygame.display.set_mode((setting.width, setting.height))
pygame.display.set_caption("Space Invaders")

# ship initialization
game = True
while game:
    ship = Ship(screen, setting.ship_speed, setting.ship_img_path)
    bullets = []
    aliens = []
    alien_bullet = []
    gm = GameFunction(screen, setting)
    #######################

    while True:
        gm.check_events(ship, bullets, aliens, alien_bullet)
        if not gm.updateScreen(ship, bullets, aliens, alien_bullet):
            if GameFunction.check_again():
                break
            else:
                game = False
                break
        pygame.time.Clock().tick(setting.fps)
