# Do part for travelling with future brick and past brick
import pyglet
from objects.brick import brick
import pprint
#from brick import brick

BRICK_LINES = 7
PIXELS_SPACING = 1
PAST_BRICK_ROWS = 21
PAST_BRICK_LINES = 7

def flatWallGenerator(wall : list[list[brick]],FillEmptyAll = None):
    for r in range(PAST_BRICK_ROWS):
        for l in range(BRICK_LINES):
            if FillEmptyAll is None :
                #return everything
                pass
            elif FillEmptyAll and wall[r][l] is None :
                #FillEmptyAll is True so brick should be Fill for return it
                continue
            elif wall[r][l] is None :
                #FillEmptyAll is False and brick is empty so return it
                pass
            yield wall[r][l],r,l

class wallp :

    min_height : int
    max_height : int
    min_width : int
    max_width : int
    brick_height : list[int]
    brick_width : list[int]

    bricks : list[list[brick]]

    def __init__(self,brick_height:int ,window : pyglet.window) -> None:
        #self.bricks = generateArray()
        self.min_height = window.height * 1/2
        self.max_height = window.height * 13/16

        self.min_width = 0 
        self.max_width = window.width * 1/6        

        self.brick_height = self.generateBrickHeight()
        self.brick_width = self.generateBrickWidth()
        self.bricks = self.generateArray()

    def generateArray(self) -> list[list[brick]] :
        array = []
        for _ in range(PAST_BRICK_ROWS) :
            array.append([None]*BRICK_LINES)
        return array
    
    def generateBrickWidth(self) -> list[int]:
        brickWidth = []
        for i in range(PAST_BRICK_ROWS + 1) :
            baseBrickWidth = (i+1)*2
            brickWidth.append(baseBrickWidth)
        totalSize = sum(brickWidth)
        totalSize = self.max_width / totalSize # Give a coeff for resize width.
        brickWidth = [size * totalSize for size in brickWidth]
        return brickWidth
    
    def generateBrickHeight(self) -> list[int]:
        brickHeight = []
        for i in range(PAST_BRICK_LINES + 1) :
            baseBrickHeight = (i+1)*2
            brickHeight.append(baseBrickHeight)
        totalSize = sum(brickHeight)
        totalSize = (self.max_height - self.min_height) / totalSize # Give a coeff for resize width.
        brickHeight = [size * totalSize for size in brickHeight]
        return brickHeight
    
    def updateRow(self):
        #@note and lines…
        for brick,r,l in flatWallGenerator(self.bricks,True) :
            #x = self.max_width - ((self.brick_width[r] + PIXELS_SPACING))
            x = ((sum(self.brick_width[:r]) + r + PIXELS_SPACING))
            y = ((sum(self.brick_height[:l]) + l + PIXELS_SPACING))
            brick.move(x,y,width=self.brick_width[r],height=self.brick_height[l])


    #Set new positions in the array
    def worldForward(self,n_row:list = [None]*BRICK_LINES) -> None:
        #the first Row will go to the past zone.
        self.bricks.append(n_row)
        for brick in self.bricks.pop(0):
            del brick
        self.updateRow()
    
    def draw(self) :
        for brick,_,_ in flatWallGenerator(self.bricks,True) :
            brick.draw()


if __name__ == "__main__" :
    print("enviromentTravel .:TEST:.")
    window = pyglet.window.Window()
    window.set_fullscreen(True)
    wall = wallp(33, window)
    print(f"{wall.brick_width}")
    print(f"{wall.bricks}")

        
