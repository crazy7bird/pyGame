import pyglet 
from random import random 
from objects.boat import boatPosition
BALL_RADIUS = 5
ALLY_COLOR = (25,255,150,255)
ENEMY_COLOR = (140,87,140,255)

class ball:
    locked : bool
    lost : bool
    x_speed : int
    y_speed : int
    img : pyglet.shapes
    dx : int #used to calcul next position.
    dy : int

    def __init__(self,x = 0, y = 0, speed = 400,radius = BALL_RADIUS,locked = False) -> None:
        self.locked = locked
        self.x_speed = (-speed*2) + (random() * 4 * speed)
        self.y_speed = speed
        self.img = pyglet.shapes.Circle(x,y,BALL_RADIUS, color=ALLY_COLOR)
        self.lost = False
        self.dx = 0
        self.dy = 0
        self.radius = radius

    def __del__(self) :
        self.img.delete()
    
    def draw(self) -> None :
        self.img.draw()

    def unlock(self) -> None: 
        self.locked = False
    
    def isFinish(self) -> bool :
        return self.lost