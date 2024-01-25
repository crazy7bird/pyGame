import pyglet 
from pyglet.window import key
from dataclasses import dataclass
from random import random
from objects.ball import ball
from objects.boat import boat
from objects.brick import brick
from manager.wall import wall
from manager.input import keyboardControler

ALLY_COLOR = (25,255,150,255)
ENEMY_COLOR = (140,87,140,255)

window = pyglet.window.Window()

window.set_fullscreen(True)
blitzBall = ball(locked=True,window=window)
theShip = boat(window)
wall = wall(window)
keys = keyboardControler(theShip, blitzBall, window, wall)

wall.fill(40)


@window.event
def on_draw():
    window.clear()
    blitzBall.img.draw()
    theShip.img.draw()
    wall.draw()

def update(dt):
    keys.update(dt)
    #theShip.update(keys,dt)
    blitzBall.update(theShip.getPosition(),wall,keys,dt)

# hiding mouse
window.set_mouse_visible(False)

pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()





