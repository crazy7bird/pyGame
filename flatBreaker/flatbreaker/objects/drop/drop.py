import pyglet

ITEM_RADIUS = 5
DEFAULT_ACC = 10
ENEMY_COLOR = (140,87,140,255)

class drop :
    x : int 
    y : int
    ySpeed : int
    yAcc : int
    end : bool

    def __init__(self, x : int, y : int, ySpeed = 0, yAcc = DEFAULT_ACC) -> None:
        self.x = x
        self.y = y
        self.ySpeed = ySpeed
        self.yAcc = yAcc
        self.img = pyglet.shapes.Circle(x,y,ITEM_RADIUS, color=ENEMY_COLOR)
        self.end = False

    def __del__(self) :
        self.img.delete()

    def isFinish(self) -> None :
        return self.end

    def update(self) -> None :
        if self.img.y < -(ITEM_RADIUS) : 
            self.end = True
            return
        self.img.y += self.ySpeed
        self.ySpeed += self.yAcc
    
    def draw(self) -> None :
        self.img.draw()

