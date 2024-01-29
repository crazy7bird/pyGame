from manager.wall import wall
from objects.ball import ball
from objects.boat import boat
from objects.brick import brick
from objects.drop.drop import *
import pyglet

class colider :
    wall : wall
    balls : list[ball]
    drops : list[drop]
    boat : boat
    

    def __init__(self,wall : wall, boat : boat, window : pyglet.window) -> None:
        self.balls = [] #@note player gives sent ball here.
        self.drops = [] #@note drops are generated in the colider.
        self.wall = wall
        self.boat = boat
        self.window = window
        self.dt = 0


    ## Ball colide management.
    def updateBallsWindowColide(self, ball) -> bool :
        if ball.dx < 0 or ball.dx > self.window.width :
            ball.x_speed = - ball.x_speed
            return True
        if ball.dy > self.window.height :
            ball.y_speed = - ball.y_speed
            return True
        return False
        
    def updateBallsBottomOrBoatColide(self, ball) -> bool :
        if (ball.dy <= self.boat.yMax and ball.img.y >self.boat.yMin) :
            if( (ball.dx >= self.boat.xMin) and 
                (ball.dx <= self.boat.xMax)
            ) :
                self.boatBounceControl(ball)
                return True
        if(ball.dy < self.boat.yMin) :
            if(ball.img.y + ball.radius < 0) :
                del ball
            return True
        return False

    def updateBallsBrickColide(self,ball) -> bool:
        #@note ball radius is not treated.
        #case not even in the wall aera
        if((ball.dy < self.wall.min_height) or
           (ball.dy > self.wall.max_height)
           ) :
            return False
        
        for brick,r,l in self.wall.flatWallGenerator(True) :
            #check if something is crossed 
            cross_left_in =    (ball.img.x < brick.ax and ball.dx > brick.ax)
            cross_right_in =   (ball.img.x > brick.bx and ball.dx < brick.bx)
            cross_bottom_in =  (ball.img.y < brick.ay and ball.dy > brick.ay)
            cross_top_in =     (ball.img.y > brick.by and ball.dy < brick.by)

            inside_aera = (ball.dx > brick.ax and 
                        ball.dx < brick.bx and
                        ball.dy > brick.ay and
                        ball.dy < brick.by)
            
            if(inside_aera):
                # coinX = (brick.ax + brick.bx) / 2
                # coinY = (brick.by + brick.ay) / 2
                # coinloc = coin.coin(coinX,coinY)
                # self.items.add(coinloc)
                del brick #Brutal destroy the brick
                
                self.wall.bricks[r][l] = None
                if(cross_top_in or cross_bottom_in) :
                    ball.y_speed = -ball.y_speed
                if(cross_left_in or cross_right_in):
                    ball.x_speed = -ball.x_speed
                return True
        return False
    
    def updateBalls(self) -> None:
        for ball in self.balls :
            #Test if locked
            if ball.locked :
                self.img.x = ( boat.xMin + boat.xMax ) / 2
                self.img.y = boat.yMax + (self.img.radius/2)
                return
            # Update next position.
            self.dx = self.img.x + (self.x_speed * self.dt)
            self.dy = self.img.y + (self.y_speed * self.dt)
            if self.updateBallsWindowColide(ball) :
                return
            if self.updateBallsBottomOrBoatColide(ball) :
                return
            self.updateBallsBrickColide(ball)
            return 
        
    def update(self) -> None :
        self.updateBalls(self)




