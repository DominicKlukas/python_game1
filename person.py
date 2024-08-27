class Person():
    def __init__(self):
        self.jump = False
        self.vx = 0
        self.vy = 0
        self.xa = 50 #running
        self.ja = 500 #jumping
        self.fa = 1000 #falling
        self.sa = self.xa*3 #slowing
        self.max_speed = self.xa*15
        self.floor = 520
        return

    def move(self, keys):
        if keys[self.pg.K_w] and not self.jump:
            self.jump = True
            self.vy -= self.ja
        if keys[self.pg.K_a]:
            self.vx += -self.xa
            self.left = True
        elif keys[self.pg.K_d]:
            self.vx += self.xa
            self.left = False
        else:
            if(self.vx > 0):
                self.vx -= self.sa/2
            elif(self.vx < 0):
                self.vx += self.sa/2
        return

    def update(self,dt):
        if(self.left):
            image = self.img_left
        else:
            image = self.img_right

        self.check_limits()

        self.pos.x += self.vx*dt
        self.pos.y += self.vy*dt
        if self.pos.y >= 520:
            self.jump = False

        self.sc.blit(image, self.pos)
        self.vy += self.fa*dt

    def check_limits(self):
        if(self.pos.x > 1280):
            self.pos.x = 0
        elif(self.pos.x < 0):
            self.pos.x = 1280
        if(self.pos.y < 0):
            self.pos.y = 0
            self.vy = 0
        elif(self.pos.y > self.floor):
            self.pos.y = 520
            self.vy = 0
        if(self.vx < -self.max_speed):
            self.vx = -self.max_speed
        elif(self.vx > self.max_speed):
            self.vx = self.max_speed
