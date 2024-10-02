import pygame, sys
from pygame.locals import *
import parametric
import time
screen = pygame.display.set_mode((640,480))
screen.fill((255,255,255))
pygame.init()

class player:
    def __init__(self):
        self.pos = parametric.orderedPair(320,240)
        self.vel = parametric.orderedPair(0,0)
        self.moveState = "still"
        self.fall = True
    def disp(self):
        pygame.draw.rect(screen, (128,128,128), (self.pos.x-10,self.pos.y-10,20,20))

class block:
    def __init__(self,pos):
        self.pos = pos
    def disp(self,p):
        pygame.draw.rect(screen, (0,0,0), (self.pos.x-10,self.pos.y-10,20,20))
        if p.pos.x+10+p.vel.x > self.pos.x-10 and p.pos.x-10 < self.pos.x+10 and p.pos.y+10 > self.pos.y-10 and p.pos.y-10 < self.pos.y+10:
            p.pos.x = self.pos.x-20
            p.vel.x = 0
            p.moveState = "still"
        if p.pos.x-10+p.vel.x < self.pos.x+10 and p.pos.x+10 > self.pos.x-10 and p.pos.y+10 > self.pos.y-10 and p.pos.y-10 < self.pos.y+10:
            p.pos.x = self.pos.x+20
            p.vel.x = 0
            p.moveState = "still"
        if p.pos.y+10+p.vel.y >= self.pos.y-10 and p.pos.y-10+p.vel.y < self.pos.y+10 and p.pos.x+10 > self.pos.x-10 and p.pos.x-10 < self.pos.x+10 and p.fall and p.pos.y < self.pos.y:
            p.pos.y = self.pos.y-20
            p.vel.y = 0
            p.fall = False
        if p.pos.y-10+p.vel.y < self.pos.y+10 and p.pos.y+10+p.vel.y > self.pos.y-10 and p.pos.x+10 > self.pos.x-10 and p.pos.x-10 < self.pos.x+10 and p.pos.y > self.pos.y:
            p.pos.y = self.pos.y+20
            p.vel.y = 0

p = player()
bL = []
for i in range(32):
    bL.append(block(parametric.orderedPair(10+i*20,260)))
b = block(parametric.orderedPair(450,240))
b2 = block(parametric.orderedPair(450,220))
b3 = block(parametric.orderedPair(450,200))
b4 = block(parametric.orderedPair(450,180))
while True:
    p.fall = True
    screen.fill((255,255,255))
    p.disp()
    for i in range(len(bL)):
        bL[i].disp(p)
    #b.disp(p)
    #b2.disp(p)
    #b3.disp(p)
    b4.disp(p)
    if p.moveState == "right":
        p.vel.x += 0.25
        if p.vel.x > 5:
            p.vel.x = 5
    if p.moveState == "left":
        p.vel.x -= 0.25
        if p.vel.x < -5:
            p.vel.x = -5
    if p.moveState == "still":
        if p.vel.x > 0:
            p.vel.x -= 0.25
            if p.vel.x < 0:
                p.vel.x = 0
        elif p.vel.x < 0:
            p.vel.x += 0.25
            if p.vel.x > 0:
                p.vel.x = 0
    if p.fall:
        p.vel.y += 0.25
    p.pos.x += p.vel.x
    p.pos.y += p.vel.y
    pygame.display.update()
    time.sleep(1/60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                p.moveState = "right"
            if event.key == K_LEFT:
                p.moveState = "left"
            if event.key == K_UP:
                if not p.fall:
                    p.vel.y = -5
        elif event.type == KEYUP:
            if event.key == K_RIGHT or event.key == K_LEFT:
                p.moveState = "still"
        
