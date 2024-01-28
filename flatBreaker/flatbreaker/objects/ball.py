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
    windowWidth : int
    windowHeight : int

    def __init__(self,window :pyglet.window,x = 0, y = 0, speed = 400,radius = BALL_RADIUS,locked = False) -> None:
        self.locked = locked
        self.x_speed = -speed + (random() * 2 * speed)
        self.y_speed = speed
        self.img = pyglet.shapes.Circle(x,y,BALL_RADIUS, color=ALLY_COLOR)
        self.lost = False
        self.dx = 0
        self.dy = 0
        self.radius = radius
        self.windowWidth = window.width
        self.windowHeight = window.height

    def __del__(self) :
        self.img.delete()
    
    def draw(self) -> None :
        self.img.draw()

    def unlock(self) -> None: 
        self.locked = False
    
    def isLost(self) -> bool :
        return self.lost

    def calculateBrickcolide(self,wall) -> bool :
        brick_colide = wall.colide(self.img.x, self.dx, self.img.y, self.dy)
        if(brick_colide>0) :
            #do ite
            if ( brick_colide == 1 or brick_colide == 3) :
                self.x_speed =-self.x_speed
            if (brick_colide == 2 or brick_colide == 3) :
                self.y_speed =-self.y_speed
            return True
        return False
    
    def boatBounceControl(self, boat : boatPosition) -> None :
        self.y_speed = abs(self.y_speed) # Mystical to be sure it goes up.
        boat_size = boat.xMax - boat.xMin
        bounce = self.img.x - boat.xMin
        bounce = ((bounce - ((boat_size)/2)) / boat_size) * self.y_speed
        self.x_speed += bounce
        self.dy = boat.height
    
    def calculateWindowColide(self, boat : boatPosition) -> bool :
        if(self.dx > self.windowWidth) :
            self.dx = self.windowWidth - (self.dx - self.windowWidth)
            self.x_speed = - self.x_speed
        elif (self.dx < 0) :
            self.dx = -self.dx
            self.x_speed = - self.x_speed

        if(self.dy > self.windowHeight) :
            self.dy = self.windowHeight - (self.dy - self.windowHeight)
            self.y_speed = - self.y_speed
        elif (self.dy <= boat.height and self.img.y >0) :
            if( (self.dx >= boat.xMin) and 
                (self.dx <= boat.xMax)
            ) :
                self.boatBounceControl(boat)
            else :
                #@note Ball is lost.
                self.dy = -10
                self.lost = True
    
    def update(self,boat : boatPosition,wall,keys,dt) -> None:
        # If the ball is locked on the boat
        if(self.locked) :
            self.img.x = ( boat.xMin + boat.xMax ) / 2
            self.img.y = boat.height + (self.img.radius/2)

        # Update next position.
        self.dx = self.img.x + (self.x_speed * dt)
        self.dy = self.img.y + (self.y_speed * dt)

        # Calculate colision with a brick
        if self.calculateBrickcolide(wall) :
            return #we found an object ball colide.

        # Calculate colision with border screen and boat.
        self.calculateWindowColide(boat)

        self.img.x = self.dx
        self.img.y = self.dy
