import pyglet 

BULLET_RADIUS = 5
BULLET_COLOR = (255,175,50,175)

class bullet:
    lost : bool
    y_speed : int
    x : int
    y : int
    img : pyglet.shapes

    def __init__(self,x : int, y : int) -> None:
        self.y_speed = 1000
        self.img = pyglet.shapes.Circle(x,y,BULLET_RADIUS, color=BULLET_COLOR)

    def __del__(self) :
        self.img.delete()
    
    def draw(self) -> None :
        self.img.draw()
