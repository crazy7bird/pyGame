""" functions colides and results for balllls 
"""
from objects.ball import ball
from objects.boat import boat
from objects.player import player
from manager.wall import wall
import pyglet
import random
from manager.colider.dropColider import dropColider

class ballColider :
    balls : list [ball]

    def __init__(self,wall : wall, boat : boat, dropColider : dropColider, window : pyglet.window, player : player) -> None:
        self.balls = [] #@note player gives sent ball here.
        self.wall = wall
        self.boat = boat
        self.window = window
        self.dropColider = dropColider
        self.dt = 0
        self.player = player

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
    
    def generateDrop(self,brick) :
        dropX = (brick.ax + brick.bx) / 2
        dropY = (brick.by + brick.ay) / 2
        match brick.__class__.__name__ :
            case "brick" :
                rad = random.random()
                if(rad>0.66):
                    self.dropColider.creatLife(dropX,dropY)
                elif rad > 0.33 :
                    self.dropColider.creatAmmunation(dropX,dropY)
                else :
                    self.dropColider.creatNewBall(dropX,dropY)
            case "commonBrick" :
                self.dropColider.creatCoin(dropX,dropY)
                pass
        pass

    def updateBallsBrickColide(self,ball) -> bool:
        #@note ball radius is not treated.
        #case not even in the wall aera
        if((ball.dy < self.wall.min_height) or
           (ball.dy > self.wall.max_height)
           ) :
            return False
        
        for brick,r,l in self.wall.flatWallGenerator(True) :
            #check if something is crossed 
            cross_left_in =    (ball.dx > brick.ax and ball.dx < brick.bx)
            cross_right_in =   (ball.dx < brick.bx)
            cross_bottom_in =  (ball.dy  > brick.ay)
            cross_top_in =     (ball.dy  < brick.by)

            #@note check only if between ax bx and change x direction 
            #@note check if cross bot or top in the same and change y dir

            inside_aera = (ball.dx> brick.ax and 
                        ball.dx  < brick.bx and
                        ball.dy  > brick.ay and
                        ball.dy  < brick.by)
            
            if(inside_aera):
                print(f"l {cross_left_in}, r {cross_right_in}, b {cross_bottom_in}, t {cross_top_in}")
                brick.hp -= self.player.atk
                if(brick.hp <= 0) :
                    #@Note : the drop creation should be move
                    self.generateDrop(brick)
                    #WITH HP NOW
                    del brick
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
                continue
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
            continue 
        
    def draw(self) -> None :
        for ball in self.balls :
            ball.draw()

