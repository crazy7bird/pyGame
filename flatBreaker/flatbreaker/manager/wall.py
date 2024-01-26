"""The wall is the grid that contain brick
        Wall objectif :
        - Set brick 
        - calculate colisions with brick
"""
import pyglet 
from objects.brick import brick
from objects.environementTravel import wallp

BRICK_LINES = 7
BRICK_ROWS = 21
PIXELS_SPACING = 1

def flatWallGenerator(wall : list[list[brick]],FillEmptyAll = None):
    """flatWallGenerator is a python generator for parse every element on the 2D list of bricks

    Args:
        wall (list[list[brick]]): 2D list of bricks 
        FillEmptyAll (_type_, optional): True return only setted brick, False return only empty brick, None return all. Defaults to None.

    Yields:
        brick : The next brick that should be treated.
        r : row number
        l : line number
    """
    for r in range(BRICK_ROWS):
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


class wall :
    """_summary_ class wall to manages briks
    """
    min_height : int
    max_height : int
    min_width : int
    max_width : int
    brick_height : int
    brick_width : int
    wallPast : wallp

    bricks : list[list[brick]]

    def __init__(self, window : pyglet.window) -> None:
        self.bricks = self.generateArray()
        self.min_height = window.height * 1/2
        self.max_height = window.height * 13/16
        self.min_width = window.width * 1/6
        self.max_width = window.width * 5/6
        self.brick_height = (( self.max_height - self.min_height - PIXELS_SPACING) / (BRICK_LINES + 1))
        self.brick_width =  (( self.max_width - self.min_width - PIXELS_SPACING ) /(BRICK_ROWS + 1))
        self.wallPast = wallp(self.brick_height, window)

    def generateArray(self) -> list[list[brick]] :
        array = []
        for _ in range(BRICK_ROWS) :
            array.append([None]*BRICK_LINES)
        return array
      
    def updateRow(self):
        for brick,r,l in flatWallGenerator(self.bricks,True) :
            x = self.min_width + (r * (self.brick_width + PIXELS_SPACING))
            y = self.min_height + (l * (self.brick_height + PIXELS_SPACING))
            brick.move(x,y)

    #Set new positions in the array
    def worldForward(self,n_row:list = [None]*BRICK_LINES) -> list :
        #the first Row will go to the past zone.
        self.bricks.append(n_row)
        retiredRow = self.bricks.pop(0)
        self.updateRow()
        return retiredRow
    
    def test_move_row(self) :
        # for brick in self.worldForward() :
        #     #delet them for now
        #     if brick is not None :
        #         brick.img.delete()
        self.wallPast.worldForward(self.worldForward())

    def fill(self, n: int) :
        for r in range(BRICK_ROWS) :
            for l in range(BRICK_LINES) :
                x = self.min_width + (r * (self.brick_width + PIXELS_SPACING))
                y = self.min_height + (l * (self.brick_height + PIXELS_SPACING))
                self.bricks[r][l] = brick(x,y,self.brick_width,self.brick_height)
    
    def draw(self) :
        for brick,r,l in flatWallGenerator(self.bricks,True) :
            brick.img.draw()
        self.wallPast.draw()
            

    # return brick side colided : 0 none, 1 top_or_botom, 2 left_or_righ, 3 corner.
    def colide(self,x,dx,y,dy) -> int :
        #@note ball radius is not treated.
        #case not even in the wall aera
        if((dy < self.min_height) or
           (dy > self.max_height)
           ) :
            return -1
        
        for brick,r,l in flatWallGenerator(self.bricks,True) :
            #check if something is crossed 
            cross_left_in =    (x < brick.ax and dx > brick.ax)
            cross_right_in =   (x > brick.bx and dx < brick.bx)
            cross_bottom_in =  (y < brick.ay and dy > brick.ay)
            cross_top_in =     (y > brick.by and dy < brick.by)

            inside_aera = (dx > brick.ax and 
                        dx < brick.bx and
                        dy > brick.ay and
                        dy < brick.by)
            
            if(inside_aera):
                brick.img.delete()
                self.bricks[r][l] = None
                return (cross_top_in or cross_bottom_in)*2 + (cross_left_in or cross_right_in) # brick found.

        return -1

