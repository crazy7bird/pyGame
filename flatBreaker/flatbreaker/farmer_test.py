import pyglet 
from objects.characters.nativs.farmer import farmer




if __name__ == "__main__" :
    window = pyglet.window.Window()

    window.set_fullscreen(True)

    farmer = farmer( x= window.width/2)
    farmer.moveForward()
    farmer.moveBackward()
    @window.event
    def on_draw():
        window.clear()
        farmer.move(-5,0)
        farmer.draw()

    # hiding mouse
    window.set_mouse_visible(False)
    pyglet.app.run()

