import pyglet 
from objects.boat import boat
from manager.wall import wall
from manager.input import keyboardControler
from manager.colider.colider import colider
from objects.player import player

ALLY_COLOR = (25,255,150,255)
ENEMY_COLOR = (140,87,140,255)

window = pyglet.window.Window()


window.set_fullscreen(True)

player = player()
theShip = boat(window)
wall = wall(window)
colider = colider(wall,theShip,window)
colider.creatBall()
keys = keyboardControler(theShip, colider, window, wall, player)




wall.fill(40)


@window.event
def on_draw():
    window.clear()
    theShip.draw()
    wall.draw()
    colider.draw()

def update(dt):
    keys.update(dt)
    #theShip.update(keys,dt)
    # blitzBall.update(theShip.getPosition(),wall,dt)
    # if blitzBall.isFinish() :
    #     print("LOST")
    #     #del(blitzBall)
    #     exit()
    colider.update(dt)

# hiding mouse
window.set_mouse_visible(False)

pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()





