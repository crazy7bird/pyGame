import pyglet 
from dataclasses import dataclass

ALLY_COLOR = (25,255,150,255)
ENEMY_COLOR = (140,87,140,255)

BRICK_WIDTH = 40
BRICK_HEIGHT = 27
class brick : 
    img : pyglet.shapes
    ax : int
    ay : int
    bx : int
    by : int
    width : int
    height : int

    def __init__(self, x,y,width = BRICK_WIDTH, height = BRICK_HEIGHT) -> None:
        self.img = pyglet.shapes.Rectangle(x,y,width,height, color = ALLY_COLOR)
        self.ax = x
        self.bx = x + width
        self.ay = y
        self.by = y + height
        self.width = width
        self.height = height
    
    def __del__(self):
        self.img.delete()

    def move(self, x,y, width = None, height = None) :
        if( width is not None):
            self.width = width
            self.img.width = width
        if ( height is not None):
            self.height = height
            self.img.height  = height
        self.img.x = x
        self.img.y = y
        self.ax = x
        self.bx = x + self.width
        self.ay = y
        self.by = y + self.height
    
    def draw(self) -> None :
        self.img.draw()
