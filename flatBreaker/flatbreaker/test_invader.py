import pyglet 
from pathlib import Path

N_IMG_ANIM = 6
SPRIT_PATH = Path('./flatbreaker/sprites/Invader/')

class invader():
    def __init__(self) -> None:
        self.images = []
        for i in range(N_IMG_ANIM) :
            self.images.append(pyglet.image.load(Path(SPRIT_PATH, f"Invader{i}.png")))
        self.animation = pyglet.image.Animation.from_image_sequence(self.images, duration=0.5, loop=True)
        self.spr = pyglet.sprite.Sprite(self.animation, x=32, y=(window.height - 64))
    
    def draw(self):
        self.spr.draw()


if __name__ == "__main__" :
    window = pyglet.window.Window()

    window.set_fullscreen(True)

    invader = invader()
    @window.event
    def on_draw():
        window.clear()
        invader.draw()

    # hiding mouse
    window.set_mouse_visible(False)
    pyglet.app.run()




