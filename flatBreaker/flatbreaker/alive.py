from typing import Any
import pyglet 
from pyglet.window import key
from pathlib import Path
from dataclasses import dataclass

# @note : 
# - Animations for living creature
# - Stand : maybe make them breath ?
# - Move : Walk animation.
# - Jump : (useful for path chose, like jump other house)
N_ANIMATION_IMG = 3

@dataclass
class humanoid :
    animation_imgs : list[pyglet.image]
    animation : pyglet.image
    img_state : int
    spr : pyglet.sprite

    def __init__(self,sprite_path) -> None:
        self.animation_imgs = []
        for i in range(N_ANIMATION_IMG) :
            self.animation_imgs.append(pyglet.image.load(Path(sprite_path, f"{i}.png")))
            self.animation_imgs[i].anchor = 10
            self.animation_imgs[i].width = -20
        self.animation = pyglet.image.Animation.from_image_sequence(self.animation_imgs,.2,True)
        #self.spr = pyglet.sprite.Sprite(self.animation, x=32, y=32)
        self.spr = pyglet.sprite.Sprite(self.animation_imgs[0], x=32, y=32)
        self.spr.update(scale = 10)
    
    def revertAnimmation(self,left : bool) -> None :
        dir = 20 * (-1 * left)
        for el in animation_imgs :
            self.animation_imgs[i].width = dir

    def update(self, keys):
        if keys[key.I]:
            self.revertAnimmation(False)
            self.spr.x += 5
            if(self.spr.image != self.animation) :
                self.spr.image = self.animation
        elif(keys[key.A]):
            self.revertAnimmation(True)
            self.spr.x -= 5
            if(self.spr.image != self.animation) :
                self.spr.image = self.animation
        else :
            self.spr.image = self.animation_imgs[0]
        


window = pyglet.window.Window()

window.set_fullscreen(True)
print(Path())
H = humanoid(Path('./flatbreaker/sprites/H/'))
@window.event
def on_draw():
    window.clear()
    H.spr.draw()

#Keyboard :
keys = key.KeyStateHandler()
window.push_handlers(keys)

def update(dt):
    H.update(keys)

pyglet.clock.schedule_interval(update, 1/60)

# hiding mouse
window.set_mouse_visible(False)
pyglet.app.run()
