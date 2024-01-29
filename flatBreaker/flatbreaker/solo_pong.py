import pyglet 
from objects.ball import ball
from objects.boat import boat
from manager.wall import wall
from manager.input import keyboardControler
from objects.itemList import itemList

ALLY_COLOR = (25,255,150,255)
ENEMY_COLOR = (140,87,140,255)

window = pyglet.window.Window()

listOfObjects = itemList()

window.set_fullscreen(True)
blitzBall = ball(locked=True,window=window)
theShip = boat(window)
wall = wall(window,listOfObjects)
keys = keyboardControler(theShip, blitzBall, window, wall)


wall.fill(40)


@window.event
def on_draw():
    window.clear()
    blitzBall.draw()
    theShip.draw()
    wall.draw()
    listOfObjects.draw()

def update(dt):
    keys.update(dt)
    #theShip.update(keys,dt)
    blitzBall.update(theShip.getPosition(),wall,dt)
    if blitzBall.isFinish() :
        print("LOST")
        #del(blitzBall)
        exit()
    listOfObjects.update()

# hiding mouse
window.set_mouse_visible(False)

pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()





