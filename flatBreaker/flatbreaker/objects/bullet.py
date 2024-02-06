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
        self.img = [pyglet.shapes.Circle(x,y,BULLET_RADIUS, color=BULLET_COLOR),
                    pyglet.shapes.Circle(x,y,BULLET_RADIUS-1, color=BULLET_COLOR),
                    pyglet.shapes.Circle(x,y,BULLET_RADIUS-2, color=BULLET_COLOR),
                    pyglet.shapes.Circle(x,y,BULLET_RADIUS-3, color=BULLET_COLOR),
                    ]

    def __del__(self) :
        self.img.delete()
    
    def draw(self) -> None :
        for img in self.img :
            img.draw()
