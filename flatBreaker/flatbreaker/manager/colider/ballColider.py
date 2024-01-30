""" functions colides and results for balllls 
"""
from objects.ball import ball
from objects.boat import boat
from manager.wall import wall
import pyglet

class ballColider :
    balls : list [ball]

    def __init__(self,wall : wall, boat : boat, window : pyglet.window) -> None:
        self.balls = [] #@note player gives sent ball here.
        self.drops = [] #@note drops are generated in the colider.
        self.wall = wall
        self.boat = boat
        self.window = window
        self.dt = 0

    def creatBall(self) -> None :
        self.balls.append(ball(locked=True))

    ## Ball colide management.
    def updateBallsWindowColide(self, ball) -> bool :
        if ball.dx < 0 or ball.dx > self.window.width :
            ball.x_speed = - ball.x_speed
            return True
        if ball.dy > self.window.height :
            ball.y_speed = - ball.y_speed
            return True
        return False
    
    def boatBounceControl(self, ball) -> None :
        ball.y_speed = abs(ball.y_speed) # Mystical to be sure it goes up.
        boat_size = self.boat.size
        bounce = ball.img.x - self.boat.img.x
        bounce = ((bounce - ((boat_size)/2)) / boat_size) * ball.y_speed
        ball.x_speed += bounce
        ball.dy = (self.boat.minY + self.boat.height)
        
    def updateBallsBottomOrBoatColide(self, ball) -> bool :
        if (ball.dy <= (self.boat.minY + self.boat.height)  and ball.img.y >self.boat.minY) :
            if( (ball.dx >= self.boat.img.x) and 
                (ball.dx <= (self.boat.img.x +self.boat.size))
            ) :
                self.boatBounceControl(ball)
                return True
        if(ball.dy < self.boat.minY) :
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
    
    def updateBalls(self, dt) -> None:
        self.dt = dt
        for ball in self.balls :
            #Test if locked
            if ball.locked :
                ball.img.x = ( self.boat.img.x + (self.boat.img.x +self.boat.size) ) / 2
                ball.img.y = (self.boat.minY + self.boat.height) + (ball.img.radius/2)
                return
            # Update next position.
            ball.dx = ball.img.x + (ball.x_speed * self.dt)
            ball.dy = ball.img.y + (ball.y_speed * self.dt)
            if self.updateBallsWindowColide(ball) :
                pass
            elif self.updateBallsBottomOrBoatColide(ball) :
                pass
            else :
                self.updateBallsBrickColide(ball)
            ball.img.x = ball.dx
            ball.img.y = ball.dy
            return 
        
    def draw(self) -> None :
        for ball in self.balls :
            ball.draw()

