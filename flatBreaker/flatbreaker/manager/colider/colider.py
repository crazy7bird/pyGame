from flatbreaker.manager.wall import wall
from flatbreaker.objects.ball import ball
from flatbreaker.objects.boat import boat

from flatbreaker.objects.drop.drop import *
import pyglet
from flatbreaker.manager.colider.ballColider import ballColider
from flatbreaker.manager.colider.dropColider import dropColider
from flatbreaker.manager.colider.bulletColider import bulletColider
from flatbreaker.objects.player import player
from flatbreaker.manager.invasion import invasion

class colider :
    wall : wall
    balls : list[ball]
    drops : list[drop]
    boat : boat
    

    def __init__(self,wall : wall, boat : boat, player : player,window : pyglet.window, invasion : invasion) -> None:
        self.drops = [] #@note drops are generated in the colider.
        self.wall = wall
        self.boat = boat
        self.player = player
        self.window = window
        self.dt = 0
        self.dropColider = dropColider(boat,player)
        self.ballColider = ballColider(wall,boat,self.dropColider,window,player)
        self.bulletColider = bulletColider(wall,boat,window,player, invasion)

    def shoot(self) -> None :
        self.bulletColider.creatBullet()
        pass

    def creatBall(self) -> None :
        self.ballColider.creatBall()
    
    def ballOnBoat(self) -> bool :
        for ball in self.ballColider.balls :
            if ball.locked :
                return True
        return False

    def unlockBalls(self) -> None :
        for ball in self.ballColider.balls :
            ball.unlock()
        
    def update(self,dt) -> None :
        self.dt = dt
        self.ballColider.updateBalls(self.dt)
        self.dropColider.updateDrops(self.dt)
        self.bulletColider.updateBullet(self.dt)

    def draw(self) -> None :
        self.ballColider.draw()
        self.dropColider.draw()
        self.bulletColider.draw()




