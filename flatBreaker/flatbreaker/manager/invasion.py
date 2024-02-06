# the invader manager
import pyglet
from objects.invader import invader
import random
from dataclasses import dataclass

@dataclass
class deadInvader() :
    invader : invader
    time : float

class invasion() :

    def __init__(self,window : pyglet.window) -> None:
        self.invaders = []
        self.deadInvaders = []
        self.window = window
        self.width = window.width
        self.height = window.height
        self.dt = 0

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

        self.dt += dt
        if self.dt < 2 :
            return
        self.dt = 0
        pixelMove = [1,2,3,5,8,13,21,34,55,89,144]
        for invader in self.invaders :
            dy = random.choice(pixelMove) * -1
            dx = random.choice(pixelMove) * (-1 if (random.random() > 0.5 ) else 1)
            invader.move(dx,dy)

    def draw(self) -> None :
        for invader in self.invaders :
            invader.draw()
        for dead in self.deadInvaders :
            dead.invader.draw()
