class Rectangulo():
    def __init__(self,pos_x, pos_y, color=(255, 255, 255), w = 20, h = 20, vx = 1, vy = 1): #metodo constructor o inicializador
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h

        self.vx = vx
        self.vy = vy
    
    def mover(self, xmax, ymax):
        self.pos_x += self.vx
        self.pos_y += self.vy
        if self.pos_x >= xmax or self.pos_x <=0: #los limites en x
            self.vx *= -1
        if self.pos_y >= ymax or self.pos_y <= 0: #los limites de y
            self.vy *= -1

class Bolillas():
    def __init__(self, pos_x, pos_y, color = (245, 74, 107), radio = 5, vx = 1, vy = 1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color 
        self.radio = radio
        self.vx = vx
        self.vy = vy 
    
    def mover(self, xmax, ymax):
        self.pos_x += self.vx
        self.pos_y += self.vy
        if self.pos_x >= xmax or self.pos_x <=0: #los limites en x
            self.vx *= -1
        if self.pos_y >= ymax or self.pos_y <= 0: #los limites de y
            self.vy *= -1



