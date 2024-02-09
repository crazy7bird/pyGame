import pyglet 
from objects.boat import boat
from manager.wall import wall
from manager.input import keyboardControler
from manager.colider.colider import colider
from objects.player import player
from manager.invasion import invasion

ALLY_COLOR = (25,255,150,255)
ENEMY_COLOR = (140,87,140,255)

window = pyglet.window.Window()


window.set_fullscreen(True)

player = player()
theShip = boat(window)
wall = wall(window)
invasion = invasion(window)
invasion.newInvader()
colider = colider(wall,theShip,player,window,invasion)
invasion.addBulletColider(colider.bulletColider)
colider.creatBall()
keys = keyboardControler(theShip, colider, window, wall, player)

wall.fill(40)

@window.event
def on_draw():
    window.clear()
    theShip.draw()
    wall.draw()
    colider.draw()
    invasion.draw()

def update(dt):
    keys.update(dt)
    colider.update(dt)
    invasion.update(dt)

def debugMsg(dt):
    print(f"Player coins : {player.getCoins()}")
    invasion.newInvader()

# hiding mouse
window.set_mouse_visible(False)

pyglet.clock.schedule_interval(update, 1/60)
pyglet.clock.schedule_interval(debugMsg, 5)
pyglet.app.run()






