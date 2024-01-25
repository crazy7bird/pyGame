"""The wall is the grid that contain brick
        Wall objectif :
        - Set brick 
        - calculate colisions with brick
"""
import pyglet 
from pyglet.window import key
from dataclasses import dataclass
from random import random
from objects.brick import brick
import pprint

BRICK_LINES = 7
BRICK_ROWS = 21
MAX_BRICK = BRICK_LINES * BRICK_ROWS
PIXELS_SPACING = 1

def generateArray() -> list[list[brick]] :
    el = [[]]
    for l in range(BRICK_LINES) :
        el.append([None])
        for r in range(BRICK_ROWS) :
            el[l].append(None)
    return el

def flatWallGenerator(wall : list[list[brick]],FillEmptyAll = None):
    """flatWallGenerator is a python generator for parse every element on the 2D list of bricks

    Args:
        wall (list[list[brick]]): 2D list of bricks 
        FillEmptyAll (_type_, optional): True return only setted brick, False return only empty brick, None return all. Defaults to None.

    Yields:
        brick : The next brick that should be treated.
        l : line number
        r : row number
    """
    for l in range(BRICK_LINES):
        for r in range(BRICK_ROWS):
            if FillEmptyAll is None :
                #return everything
                pass
            elif FillEmptyAll and wall[l][r] is None :
                #FillEmptyAll is True so brick should be Fill for return it
                continue
            elif wall[l][r] is None :
                #FillEmptyAll is False and brick is empty so return it
                pass

            yield wall[l][r],l,r

@dataclass 
class colideReport :
    top : bool
    bottom : bool
    left : bool
    right : bool

class wall :
    """_summary_ class wall to manages briks
    """
    min_height : int
    max_height : int
    min_width : int
    max_width : int
    brick_height : int
    brick_width : int

    bricks : list[list[brick]]

    def __init__(self, window : pyglet.window) -> None:
        self.bricks = generateArray()
        self.min_height = window.height * 1/2
        self.max_height = window.height * 13/16
        self.min_width = window.width * 1/6
        self.max_width = window.width * 5/6
        self.brick_height = (( self.max_height - self.min_height - PIXELS_SPACING) / (BRICK_LINES + 1))
        self.brick_width =  (( self.max_width - self.min_width - PIXELS_SPACING ) /(BRICK_ROWS + 1))
    
    def empty(self) :
        for brick in self.bricks :
            brick.img.delete()
        self.bricks.clear()

    def fill(self, n: int) :
        for l in range(BRICK_LINES) :
            for r in range(BRICK_ROWS) :
                x = self.min_width + (r * (self.brick_width + PIXELS_SPACING))
                y = self.min_height + (l * (self.brick_height + PIXELS_SPACING))
                self.bricks[l][r] = brick(x,y,self.brick_width,self.brick_height)
    
    def draw(self) :
        for brick,l,r in flatWallGenerator(self.bricks,True) :
            brick.img.draw()
            

    # return brick side colided : 0 none, 1 top_or_botom, 2 left_or_righ, 3 corner.
    def colide(self,x,dx,y,dy) -> int :
        #@note ball radius is not treated.
        #case not even in the wall aera
        if((dy < self.min_height) or
           (dy > self.max_height)
           ) :
            return -1
        
        for brick,l,r in flatWallGenerator(self.bricks,True) :
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
                self.bricks[l][r] = None
                return (cross_top_in or cross_bottom_in)*2 + (cross_left_in or cross_right_in) # brick found.

        return -1

