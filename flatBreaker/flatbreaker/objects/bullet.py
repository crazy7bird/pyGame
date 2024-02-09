import pyglet 

BULLET_RADIUS = 5
BULLET_COLOR = (255,175,50,175)
BULLET_SPEED = 1000

class bullet:
    lost : bool
    y_speed : int
    x : int
    y : int
    img : pyglet.shapes

    def __init__(self,x : int, y : int, y_speed : int = BULLET_SPEED, color = BULLET_COLOR) -> None:
        self.y_speed = y_speed
        self.img = [pyglet.shapes.Circle(x,y,BULLET_RADIUS, color=color),
                    pyglet.shapes.Circle(x,y,BULLET_RADIUS-1, color=color),
                    pyglet.shapes.Circle(x,y,BULLET_RADIUS-2, color=color),
                    pyglet.shapes.Circle(x,y,BULLET_RADIUS-3, color=color),
                    ]

    def __del__(self) :
        for img in self.img :
            img.delete()
    
    def draw(self) -> None :
        for img in self.img :
            img.draw()
