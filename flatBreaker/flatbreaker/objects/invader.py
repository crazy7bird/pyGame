import pyglet 
from pathlib import Path

N_IMG_ANIM = 6
N_IMG_DEAD =3
SPRIT_PATH = Path('./flatbreaker/sprites/Invader/')
HALF_X_SIZE = 32
Y_EYE_SIZE = 24
X_SIZE = 64
Y_SIZE = 64

class invader():
    def __init__(self,x : int,window : pyglet.window) -> None:
        # ImagePart.
        self.images = []
        self.deadImages = []
        for i in range(N_IMG_ANIM) :
            self.images.append(pyglet.image.load(Path(SPRIT_PATH, f"Invader{i}.png")))
        for i in range(N_IMG_DEAD) :
            self.deadImages.append(pyglet.image.load(Path(SPRIT_PATH, f"Invader{i+N_IMG_ANIM}.png")))
        self.animation = pyglet.image.Animation.from_image_sequence(self.images, duration=0.5, loop=True)
        self.deadAnimation = pyglet.image.Animation.from_image_sequence(self.deadImages, duration=0.5, loop=False)
        self.spr = pyglet.sprite.Sprite(self.animation, x=x, y=(window.height - Y_SIZE))
        #stats part.
        self.hp = 100
        self.dead = False
        self.deadDt = 0

    def invaderDying(self) -> None :
        self.spr = pyglet.sprite.Sprite(self.deadAnimation, self.spr.x, self.spr.y)
        self.dead = True

    def invaderHit(self,x,y) -> bool :
        if ( x >= (self.spr.x + 10) and x <= (self.spr.x + 54) and
             y >= (self.spr.y + Y_EYE_SIZE) and y<= (self.spr.y + 56)
            ) :
            return True
        return False

    def invaderShootPosition(self) -> int :
        #return a point(x,y) where invader shoot should start.
        x = (self.spr.x + HALF_X_SIZE)
        y = (self.spr.y + Y_EYE_SIZE)
        return x,y
    
    def move(self,x,y) -> None :
        self.spr.x += x
        self.spr.y += y
    
    def draw(self):
        self.spr.draw()