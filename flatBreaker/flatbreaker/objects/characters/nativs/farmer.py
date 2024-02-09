import pyglet 
from pathlib import Path

N_IMG_STILL = 3
N_IMG_MOVING =6
SPRIT_PATH = Path('./flatbreaker/sprites/Farmer/')
X_SIZE = 64
Y_SIZE = 64

class farmer():
    def __init__(self,x : int) -> None:
        # ImagePart.
        self.stillImg = []
        self.forwardImg = []
        self.backwardImg = []
        for i in range(N_IMG_STILL) :
            self.stillImg.append(pyglet.image.load(Path(SPRIT_PATH, f"Farmer{i}.png")))
        for i in range(N_IMG_MOVING) :
            self.forwardImg.append(pyglet.image.load(Path(SPRIT_PATH, f"Farmer{i+N_IMG_STILL}.png")))
        for i in range(N_IMG_MOVING) :
            self.backwardImg.append(pyglet.image.load(Path(SPRIT_PATH, f"Farmer{i+N_IMG_STILL}.png")))
            self.backwardImg[i] = self.backwardImg[i].get_texture().get_transform(True)

        self.stillAnim = pyglet.image.Animation.from_image_sequence(self.stillImg, duration=0.5, loop=True)
        self.forwardAnim = pyglet.image.Animation.from_image_sequence(self.forwardImg, duration=0.1, loop=True)
        self.backwardAnim = pyglet.image.Animation.from_image_sequence(self.backwardImg, duration=0.1, loop = True)
        self.spr = pyglet.sprite.Sprite(self.stillAnim, x=x, y=0)
    
    def standStill(self) -> None :
        self.spr = pyglet.sprite.Sprite(self.stillAnim, x=self.spr.x, y=0)

    def moveForward(self) -> None :
        self.spr = pyglet.sprite.Sprite(self.forwardAnim, x=self.spr.x, y=0)
    def moveBackward(self) -> None :
        self.spr = pyglet.sprite.Sprite(self.backwardAnim, x=self.spr.x, y=0)

    def move(self,x,y) -> None :
        self.spr.x += x
        self.spr.y += y
    
    def draw(self):
        self.spr.draw()