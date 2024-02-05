import pyglet
from pyglet.window import key
from objects.boat import boat
from manager.wall import wall
from manager.colider.colider import colider
from objects.player import player

"""Get Keyboard inputs
"""
class keyboardControler :
    
    def __init__(self,boat :boat,colider : colider, window:pyglet.window,wall: wall, player : player) -> None:
        self.boat = boat
        self.colider = colider
        self.wall = wall
        self.keys = key.KeyStateHandler()
        window.push_handlers(self.keys)
        self.bMoveWall = False
        self.reloadBall = False
        self.player = player

    def update(self,dt) -> None :
        if self.keys[key.SPACE]:
            if(self.colider.ballOnBoat()):
                self.colider.unlockBalls()
            else :
                if(self.player.getMun()> 0) :
                    self.player.addMuns(-1)
                    self.colider.shoot()
        if self.keys[key.A]:
            self.boat.moveLeft(dt)
        if self.keys[key.I] :
            self.boat.moveRight(dt)

        if self.keys[key.B] and not self.bMoveWall:
            self.wall.test_move_row()
            self.bMoveWall = True
        elif  not self.keys[key.B]:
            self.bMoveWall = False

        if self.keys[key.O] and not self.reloadBall :
            if(self.player.getBalls()>0 and self.colider.ballOnBoat() == False) :
                self.colider.creatBall()
                self.player.addBalls(-1)
                self.reloadBall = True
        elif not self.keys[key.O] :
            self.reloadBall = False