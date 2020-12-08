class Setting(object):

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.bg = (230, 230, 230)
        self.fps = 30
        self.ship_bul_color = (0, 0, 0)
        self.en_bul_col = (255, 0, 0)
        self.ship_bul_speed = 15
        self.en_bul_speed = 10
        self.ship_speed = 15
        self.enemy_speed = 4
        self.enemy_img_path = "images/alien.bmp"
        self.ship_img_path = "images/ship.bmp"
        self.font_col = (100, 100, 100)
        self.font_size = 30
        self.score_x = 5
        self.score_y = 5
        self.game_over_size = 50
        self.shoot_sound_path = "sounds/shoot.wav"
        self.kill_sound_path = "sounds/invaderkilled.wav"
