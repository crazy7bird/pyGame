from manager.wall import wall
from objects.ball import ball
from objects.boat import boat
from objects.brick import brick
from objects.drop.drop import *
import pyglet
from manager.colider.ballColider import ballColider

class colider :
    wall : wall
    balls : list[ball]
    drops : list[drop]
    boat : boat
    

    def __init__(self,wall : wall, boat : boat, window : pyglet.window) -> None:
        self.drops = [] #@note drops are generated in the colider.
        self.wall = wall
        self.boat = boat
        self.window = window
        self.dt = 0
        self.ballColider = ballColider(wall,boat,window)

    def creatBall(self) -> None :
        self.ballColider.creatBall()

    def unlockBalls(self) -> None :
        for ball in self.ballColider.balls :
            ball.unlock()
        
    def update(self,dt) -> None :
        self.dt = dt
        self.ballColider.updateBalls(self.dt)

    def draw(self) -> None :
        self.ballColider.draw()




