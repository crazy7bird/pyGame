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

            min_ball_x = ball.dx - ball.radius
            max_ball_x = ball.dx + ball.radius
            min_ball_y = ball.dy - ball.radius
            max_ball_y = ball.dy + ball.radius

            inside_aera = (max_ball_x > brick.ax and 
                           min_ball_x < brick.bx and
                           max_ball_y > brick.ay and
                           min_ball_y < brick.by )

            if(inside_aera):
                dist_right = abs(max_ball_x - brick.ax)
                dist_left  = abs(min_ball_x - brick.bx)
                dist_top   = abs(min_ball_y - brick.by)
                dist_bot   = abs(max_ball_y - brick.ay)

                cross_vert = min(dist_right, dist_left)
                cross_horz = min(dist_bot, dist_top)

                if cross_horz < cross_vert :
                    ball.y_speed = -ball.y_speed
                    ball.dy -= cross_horz
                else :
                    ball.x_speed = -ball.x_speed
                    ball.dx -= cross_vert

                brick.hp -= self.player.atk
                if(brick.hp <= 0) :
                    self.generateDrop(brick)
                    del brick
                    self.wall.bricks[r][l] = None
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

