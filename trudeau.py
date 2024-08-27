from person import Person


class Trudeau(Person):
    def __init__(self,pygame,screen):
        self.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.pg = pygame
        self.sc = screen
        self.img_left = self.pg.image.load("images/jt_left.png")
        self.img_right = self.pg.image.load("images/jt_right.png")
        self.shooting_icicle = True
        self.left = False
        super().__init__()

    def shoot_icicle():
        # Implement
        return

    def dig():
        # Implement
        return

    def update(self, dt):
        super().update(dt)
        return
