""" functions colides and results for balllls 
"""
from objects.bullet import bullet
from objects.boat import boat
from objects.player import player
from manager.wall import wall
import pyglet
import random
from manager.colider.dropColider import dropColider
from manager.invasion import invasion
from objects.invader import invader

class bulletColider :
    bullets : list [bullet]

    def __init__(self,wall : wall, boat : boat, window : pyglet.window, player : player, invasion : invasion) -> None:
        self.bullets = [] #@note player gives sent ball here.
        self.wall = wall
        self.invasion = invasion
        self.boat = boat
        self.window = window
        self.dropColider = dropColider
        self.dt = 0
        self.player = player

    def creatBullet(self) -> None :
        pos = self.boat.getPosition()
        x = (self.boat.img.x +self.boat.size + self.boat.img.x ) / 2
        y = pos.yMax
        self.bullets.append(bullet(x,y))

    
    def testInvaderHit(self, bullet : bullet) -> invader :
        for invader in self.invasion.invaders :
            if invader.invaderHit(bullet.img[0].x,bullet.img[0].y) :
                return invader
        
    
    def updateBullet(self, dt) -> None:
        self.dt = dt
        for bullet in self.bullets :
            for id,img in enumerate(bullet.img) :
                img.y += (bullet.y_speed - 25*id )* self.dt
            invaderHit = self.testInvaderHit(bullet)
            if invaderHit is not None :
                invaderHit.hp -= self.player.atk


    def draw(self) -> None :
        for bullet in self.bullets :
            bullet.draw()

