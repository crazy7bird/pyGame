import pyglet
from pyglet.window import key
from objects.ball import ball
from objects.boat import boat

"""Get Keyboard inputs
"""
class keyboardControler :
    
    def __init__(self,boat :boat,ball :ball, window:pyglet.window) -> None:
        self.boat = boat
        self.balls = [ball]
        self.keys = key.KeyStateHandler()
        window.push_handlers(self.keys)

    def update(self,dt) -> None :
        if self.keys[key.SPACE]:
            for ball in self.balls :
                ball.unlock()
        if self.keys[key.A]:
            self.boat.moveLeft(dt)
        if self.keys[key.I] :
            self.boat.moveRight(dt)