import pyglet 
from dataclasses import dataclass

ALLY_COLOR = (25,255,150,255)
ENEMY_COLOR = (140,87,140,255)

#@todo : adapt brick size with an external element.
BRICK_WIDTH = 40
BRICK_HEIGHT = 27
class brick : 
    hp : int
    material : int
    img : pyglet.shapes
    ax : int
    ay : int
    bx : int
    by : int 

    def __init__(self, x,y,width = BRICK_WIDTH, height = BRICK_HEIGHT) -> None:
        self.hp = 100
        self.img = pyglet.shapes.Rectangle(x,y,width,height, color = ALLY_COLOR)
        self.ax = x
        self.bx = x + width
        self.ay = y
        self.by = y + height
