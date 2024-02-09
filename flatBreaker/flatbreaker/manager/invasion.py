# the invader manager
import pyglet
from objects.characters.invaders.invader import invader
import random
from dataclasses import dataclass


@dataclass
class deadInvader() :
    invader : invader
    time : float

@dataclass 
class livingInvader() :
    invader : invader
    time : float
    mvmt : int

class invasion() :

    def __init__(self,window : pyglet.window) -> None:
        self.invaders = []
        self.deadInvaders = []
        self.window = window
        self.width = window.width
        self.height = window.height
        self.dt = 0
        self.bulletcolider = None

    def addBulletColider(self, bulletColider) -> None :
       # from manager.colider.bulletColider import bulletColider
        self.bulletcolider = bulletColider

    def newInvader(self) -> None :
        #Generate a new invader.
        self.invaders.append(invader(self.window.width/2, self.window))


    def updateDead(self, dt) -> None :
        for dead in self.deadInvaders :
            dead.time += dt
            if dead.time > 1.5 :
                self.deadInvaders.remove(dead)

    def update(self, dt) -> None :
        #@note : provisoire.
        # check dead invader and start dead animation
        self.updateDead(dt)
        for invader in self.invaders :
            if invader.hp < 0 :
                invader.invaderDying()
                self.deadInvaders.append(deadInvader(invader,0))
                self.invaders.remove(invader)
                continue

        self.dt += dt
        if self.dt < 0.2 :
            return
        self.dt = 0
        pixelMoveY = [5,3,2,1,0,-1,-2,-3,-5,-8,-13,-21]
        pixelMoveX = [-21,-13,-8,-5,-3,-2,-1,0,1,2,3,5,8,13,21]
        for invader in self.invaders :
            dy = random.choice(pixelMoveY)
            dx = random.choice(pixelMoveX)
            invader.move(dx,dy)

            if random.random() > 0.9 :
                x,y = invader.invaderShootPosition()
                self.bulletcolider.creatInvaderBullet(x,y)

    def draw(self) -> None :
        for invader in self.invaders :
            invader.draw()
        for dead in self.deadInvaders :
            dead.invader.draw()
