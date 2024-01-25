import pyglet 


window = pyglet.window.Window()
window.set_fullscreen(True) 


balle = pyglet.shapes.Circle(x=window.width/2,y=window.height/2, radius = 10, color=(255,0,0,255))


@window.event
def on_draw():
    window.clear()
    balle.draw()


pyglet.app.run()