import pygame as pg
import random
import time

pg.init()

bg_color = (255,255,255)
(width, height) = (400,400)

scr = pg.display.set_mode((width,height))

class Circle(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.speed = pg.Vector2(0.1,0.1)
        self.acceleration = pg.Vector2(0.00001, 0.00001)
        self.colour = (255,0,0)
        self.pos = pg.Vector2(x, y)
        self.size = 15
        self.thickness = 1
        self.vel = 0
    def draw(self, scr):
        pg.draw.circle(scr, self.colour, (int(self.pos.x), int(self.pos.y)), self.size, self.thickness)
        self.update()
    def update(self):
        self.pos.x += self.speed.x 
        self.pos.y += self.speed.y 
        if int(self.pos.x) < int(0+self.size):
            self.speed.x*=-1
        if int(self.pos.x) > int(width-self.size):
            self.speed.x*=-1
        if int(self.pos.y) < int(0+self.size):
            self.speed.y*=-1
        if int(self.pos.y) > int(height-self.size):
            self.speed.y*=-1

x = random.randint(15, width)
y = random.randint(15, height)
square = Circle(x,y)

square_sprite = pg.sprite.Group()
square_sprite.add(square)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    square.draw(scr)
    pg.display.flip()
    scr.fill(bg_color)
pg.quit()
