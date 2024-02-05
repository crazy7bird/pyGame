import pyglet
from pyglet.window import key
from objects.boat import boat
from manager.wall import wall
from manager.colider.colider import colider
from objects.player import player

"""Get Keyboard inputs
"""
class keyboardControler :
    
    def __init__(self,boat :boat,colider : colider, window:pyglet.window,wall: wall, player : player) -> None:
        self.boat = boat
        self.colider = colider
        self.wall = wall
        self.keys = key.KeyStateHandler()
        window.push_handlers(self.keys)
        self.bMoveWall = False
        self.reloadBall = False
        self.player = player
        self.pressedKey = [key]

    def singlePushClean(self) -> None :
        # retains key if they still pushed.
        self.pressedKey = [key for key in self.pressedKey if self.keys[key]]

    def isReleased(self,key) -> bool :
        if key in self.pressedKey :
            return False
        #We add it cause we dont check it for nothing
        self.pressedKey.append(key)
        return True

    def update(self,dt) -> None :
        self.singlePushClean()
        if self.keys[key.SPACE] and self.isReleased(key.SPACE) :
            if(self.colider.ballOnBoat()):
                self.colider.unlockBalls()
            else :
                if(self.player.getMun()> 0) :
                    self.player.addMuns(-1)
                    self.colider.shoot()

        if self.keys[key.A]:
            self.boat.moveLeft(dt)
        if self.keys[key.I] :
            self.boat.moveRight(dt)

        if self.keys[key.B] and self.isReleased(key.B) :
            self.wall.test_move_row()
            #self.addPressedKey(key.B)

        if self.keys[key.O] and self.isReleased(key.O) :
            if(self.player.getBalls()>0 and self.colider.ballOnBoat() == False) :
                self.colider.creatBall()
                self.player.addBalls(-1)
                #self.addPressedKey(key.O)