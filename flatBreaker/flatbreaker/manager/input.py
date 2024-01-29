import pyglet
from pyglet.window import key
from objects.ball import ball
from objects.boat import boat
from manager.wall import wall
from manager.colider import colider

"""Get Keyboard inputs
"""
class keyboardControler :
    
    def __init__(self,boat :boat,colider : colider, window:pyglet.window,wall: wall) -> None:
        self.boat = boat
        #self.balls = [ball]
        self.colider = colider
        self.wall = wall
        self.keys = key.KeyStateHandler()
        window.push_handlers(self.keys)
        self.bMoveWall = False

    def update(self,dt) -> None :
        if self.keys[key.SPACE]:
            for ball in self.colider.balls :
                ball.unlock()
        if self.keys[key.A]:
            self.boat.moveLeft(dt)
        if self.keys[key.I] :
            self.boat.moveRight(dt)
        if self.keys[key.B] and not self.bMoveWall:
            self.wall.test_move_row()
            self.bMoveWall = True
        if not self.keys[key.B] :
            self.bMoveWall = False