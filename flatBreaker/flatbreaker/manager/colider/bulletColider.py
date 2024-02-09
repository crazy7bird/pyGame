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

INVADER_BULLET_COLOR = (255,0,0,255)

class bulletColider :
    bullets : list [bullet]

    def __init__(self,wall : wall, boat : boat, window : pyglet.window, player : player, invasion : invasion) -> None:
        self.bullets = [] #@note player gives sent ball here.
        self.invaderBullet = []
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

    def creatInvaderBullet(self, x, y) -> None :
        self.bullets.append(bullet(x,y, -1000,INVADER_BULLET_COLOR))

    
    def testInvaderHit(self, bullet : bullet) -> invader :
        for invader in self.invasion.invaders :
            if invader.invaderHit(bullet.img[0].x,bullet.img[0].y) :
                return invader
        
    
    def updateBullet(self, dt) -> None:
        self.dt = dt
        
        for bullet in self.bullets :
            dir = 1 if bullet.y_speed > 0 else -1
            
            for id,img in enumerate(bullet.img) :
                img.y += (bullet.y_speed - (25*id * dir) )* self.dt

            if dir > 0 :
                invaderHit = self.testInvaderHit(bullet)
                if invaderHit is not None :
                    invaderHit.hp -= self.player.atk
            else :
                boatPosition = self.boat.getPosition()
                if bullet.img[0].y <= boatPosition.yMax and bullet.img[0].y > boatPosition.yMin :
                    if bullet.img[0].x > boatPosition.xMin and bullet.img[0].x < boatPosition.xMax :
                        #touch.
                        self.player.addLife(-1)
                        self.boat.sizeUpdateByLife(self.player.getLife())
                        self.bullets.remove(bullet)


    def draw(self) -> None :
        for bullet in self.bullets :
            bullet.draw()

