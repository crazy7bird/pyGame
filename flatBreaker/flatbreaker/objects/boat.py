import pyglet 
from pyglet.window import key
from dataclasses import dataclass

ALLY_COLOR = (25,255,150,255)
ENEMY_COLOR = (140,87,140,255)

@dataclass
class boatPosition :
    xMin : int
    xMax : int
    height : int

class boat :
    img : pyglet
    size : int
    height : int
    window_max_x : int
    speed : int #px/sec

    def __init__(self, window) -> None:
        self.window_max_x = window.width
        self.height = 10
        self.size = 200
        self.img = pyglet.shapes.Rectangle(window.width/2, 0, self.size, self.height, color = ALLY_COLOR)
        self.speed = 1000

    def moveRight(self, dt) -> None :
        self.img.x += self.speed * dt
        if(self.img.x + self.size > self.window_max_x) :
            self.img.x = self.window_max_x - self.size

    def moveLeft(self,dt) -> None :
        self.img.x -= self.speed * dt
        if(self.img.x < 0 ) :
            self.img.x = 0
    
    def getPosition(self) -> boatPosition :
        return boatPosition(self.img.x, self.img.x +self.size, self.height)
