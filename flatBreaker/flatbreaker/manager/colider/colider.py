from manager.wall import wall
from objects.ball import ball
from objects.bullet import bullet
from objects.boat import boat

from objects.drop.drop import *
import pyglet
from manager.colider.ballColider import ballColider
from manager.colider.dropColider import dropColider
from manager.colider.bulletColider import bulletColider
from objects.player import player

class colider :
    wall : wall
    balls : list[ball]
    drops : list[drop]
    boat : boat
    

    def __init__(self,wall : wall, boat : boat, player : player,window : pyglet.window) -> None:
        self.drops = [] #@note drops are generated in the colider.
        self.wall = wall
        self.boat = boat
        self.player = player
        self.window = window
        self.dt = 0
        self.dropColider = dropColider(boat,player)
        self.ballColider = ballColider(wall,boat,self.dropColider,window,player)
        self.bulletColider = bulletColider(wall,boat,window,player)

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




